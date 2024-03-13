from typing import List
from pathlib import Path
import os

from .common import printd, compile_jq, load_func
from .common import DotDict

def get_fpath_items(fpath, D): 
    item_path_pairs = compile_jq(fpath, D)
    #print(items[:5])
    items, item_paths = [list(tupleObj) for tupleObj in zip(*item_path_pairs)]

    printd(3, f'get_fpath_items = {type(items)}, {len(items)}')
    return DotDict(els=items, paths=item_paths)

def compute_and_index_representations(D, config):
    '''
    compute:
    recursively Q, transcript
    index:
    each field, rep name -> 
        - index yes? index_reps -> create list(vec), list(metadata) or df[vec, field*] -> store in vec db
            - options: which field to include?
        - index no? mem_reps[field, rep_name] -> vector

    '''
    from .rag_components import compute_rep

    #def resolve_field(field, D): #TODO: return absolute jq? path(s) to field in D
        #return f'transcript.*.{field}'
    #    return field

    def hash_field_repname(fpath, repname):
        return f'{fpath}#{repname}'
    
    def _compute_index_reps(fpath, D, C, is_query=False):
        #fpath: path to to-be-rep node in O, O: parent object, C: config
        _reps = {}
        for repname, properties in C.items():
            #printd(3, f'rep for : {repname}')
            props = DotDict(properties)
            storage = props.get('storage', None)
            print(fpath, repname, f': storage={storage}, encoder={props.encoder}')
            items_path_pairs = get_fpath_items(fpath, D)
            items, item_paths = items_path_pairs.els, items_path_pairs.paths
            #field_reps = items

            field_reps: 'List[rep]' = compute_rep(items, props.encoder, repname=repname, is_query=is_query)
            rep_key = hash_field_repname(fpath, repname)
            _reps[rep_key] = list(zip(field_reps, item_paths)) #(rep, item) pair. TODO: if indexed, get ??
        return _reps
        
    reps = {} #'Chunk.content' -> dense -> rep=(doc, <vec>)
    #field, rep_name -> (collection_path | rep)

    for field, C in config.representations.items(): 
        printd(3, f'compute_index: field={field}, config={C}')
        is_query = 'query' in field
        #fpath = field.split('.')[-1] if is_query else field
        fpath = field
        _reps = _compute_index_reps(fpath, D, C, is_query=is_query)
        reps.update(_reps)



    return reps

from llama_index.core import QueryBundle
from llama_index.core.schema import NodeWithScore
from llama_index.core.retrievers import BaseRetriever, VectorIndexRetriever

def show_docs(docs):
    try:
        for doc in docs:
            print(doc.node.id_, doc.score, doc.node.metadata['file_path'], doc.node.text[:100])
    except:
        print(docs)


def compute_bridge_scores(reps, D, bridge_config):
    '''
    compute score expr for each pair of field-repname, limit by N
    assume bridge of form (mem rep - vecdb rep), use vecdb apis
    score['b1'] = [(doc, score)] 
    b1: 
     repnodes: Query.text#dense, chunk#dense
     limit: 10
    '''
    def get_reps(qkey, reps):
        keys = list(reps.keys())
        for key in keys:
            if qkey in key:
                printd(3, f'get_reps match: {qkey}, {key}')
                return reps[key]

        raise ValueError(f'unable to find {qkey} in reps')


    def rep_bridge_score(repkey1, repkey2, reps, limit=10)-> List[NodeWithScore]:
        #https://docs.llamaindex.ai/en/stable/examples/query_engine/CustomRetrievers.html
        #TODO: move this func to BackendEngine
        rep_query = get_reps(repkey1, reps)[0] #encoding for query, FIXME: generalize!
        query_bundle = QueryBundle(query_str=D.query.text, embedding=rep_query)
        
        rep2_pairs = get_reps(repkey2, reps) #VectorIndex for doc nodes, build on the fly. TODO: load persisted index
        rep2_index = [rp[0] for rp in rep2_pairs] #rp = (rep_value, rep_item_path)
        retriever2 = VectorIndexRetriever(index=rep2_index, similarity_top_k=limit)
        vector_nodes = retriever2.retrieve(query_bundle)
        #vector_ids = {n.node.node_id for n in vector_nodes}

        return vector_nodes

    docs_retrieved = {}
    printd(3, f'bridge config: {bridge_config}')
    printd(3, f'reps keys: {list(reps.keys())}')

    for bridge_name, properties in bridge_config.items():
        props = DotDict(properties)
        repkey1, repkey2 = map(lambda x: x.strip(), props.repnodes.split(','))
        printd(2, f'==== now bridging {repkey1}, {repkey2}')
        matchfn_key = props.get('matchfn')
        if matchfn_key is not None:
            rep1 = get_reps(repkey1, reps)
            rep2 = get_reps(repkey2, reps)
            matchfn = load_func(matchfn_key)
            docpath_scores = matchfn(rep1, rep2)
            print(f'bridge: docpath_scores = {docpath_scores}')
            #each doc_path here is concrete so doc_path = 1 doc/node
            docs = [(get_fpath_items(doc_path, D).els[0], score) for doc_path, score in docpath_scores]
        else:
            docs = rep_bridge_score(repkey1, repkey2, reps, limit=props.limit)
        
        docs_retrieved[bridge_name] = docs

        #show_docs(docs)

    return docs_retrieved #may or not have scores associated with docs. normalize how?



def rank_paths(scores, rank_config):
    '''
    for each query rep_name: 
        - start from query, end at doc leaves? get score. rank docs by score
    ranked_scores[rep_name] = [(doc, score)]
    ranks[rep_name] = [doc-sc, doc-sc, doc-sc]

    results: List[Result] = fuse_ranks(ranked_scores, ranks) 
    #Result = [doc, score]*

    rank: 
        expr: b1
        limit: 10

    '''
    def eval_score_expr(expr, scores):
        #TODO: generalize! 
        #use expr to gen new scores for each doc common across all bridge_names. sort.
        return scores[expr] 
    rank_config = DotDict(rank_config)
    doc_with_scores = eval_score_expr(rank_config.expr, scores)
    return doc_with_scores


def bridge_query_doc(query_text, D, config):
    Q = DotDict(text=query_text)
    D.query = Q
    reps = compute_and_index_representations(D, config)
    path_scores = compute_bridge_scores(reps, D, config.bridge) #repNode1, repNode2 -> score.
    ranked_doc_with_scores = rank_paths(path_scores, config.rank) 
    return ranked_doc_with_scores
