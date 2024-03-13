from llama_index.core.schema import TextNode
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.fastembed import FastEmbedEmbedding
from llama_index.embeddings.clip import ClipEmbedding

from . import llm_bridge

def compute_rep(items, encoder_name, repname=None, is_query=False) -> 'List[rep]':
    if encoder_name.startswith('llm'):
        return llm_bridge.transform(items, encoder_name, is_query=is_query)
    if encoder_name == 'copy_field':
        print('computing rep copy_field')
        _repname = repname[1:] # _header -> header
        reps = [item[_repname] for item in items]
        return reps
    
    encoder = None
    match encoder_name:
        case "BAAI/bge-small-en-v1.5":
            text_embed_model = FastEmbedEmbedding(model_name="BAAI/bge-small-en-v1.5")
            encoder = text_embed_model
        case "ViT-B/32":
            image_embed_model = ClipEmbedding(model_name="ViT-B/32")
            encoder = image_embed_model
        case _:
            raise ValueError("unknown encoder: {encoder_name}")
    #print(type(items[0]), items[0])
    if is_query: #based on data type, call different encoders
        #node = TextNode(text=items[0], id_="_query_")
        reps = [encoder.get_text_embedding(item) for item in items]
    else:
        assert isinstance(items, list), f"items is {type(items)}"
        reps = VectorStoreIndex.from_documents(items, embed_model=encoder, show_progress=True)
    return reps

def contains(q, d): return q in d

def tindex_from_scratch(output_folder): #learned to do via Documents
    out = Path(output_folder)
    node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=10)
    txts = list(out.glob('*.txt'))

    with open(txts[0], 'r') as f:
        text = f.read();
    text_nodes = node_parser.get_nodes_from_documents(
        [Document(text=text)], show_progress=True
    )
    tindex = VectorStoreIndex(text_nodes, embed_model=text_embed_model, show_progress=True)

def LI_doc_embed(txts, imgs):
    tindex, iindex = None, None
    txt_docs, img_docs = None, None

    #documents = SimpleDirectoryReader(output_folder).load_data()
    txt_docs = SimpleDirectoryReader(input_files=map(str, txts)).load_data() #add sentence splitter here
    tindex = VectorStoreIndex.from_documents(txt_docs, embed_model=text_embed_model, show_progress=True)
    #tindex.as_query_engine, tindex.as_retriever
    
    #img_nodes = [ImageDocument(image_path=str(img_path)).load_file() for img_path in imgs]
    img_docs = SimpleDirectoryReader(input_files=map(str, imgs)).load_data()
    iindex = VectorStoreIndex.from_documents(img_docs, embed_model=image_embed_model, show_progress=True)

    #documents = [Document(node=node) for node in text_nodes]

    #iindex = VectorStoreIndex(img_nodes, embed_model=image_embed_model, show_progress=True)
    return dict(tindex=tindex, iindex=iindex, txt_docs=txt_docs, img_docs=img_docs)

'''
from pydantic import BaseModel

class Query(BaseModel):
    text: str
class Chunk(BaseModel):
    doc: Document 
class Transcript(BaseModel):
    chunks: List[Chunk] #chunks: List[LN]

class Clip(BaseModel):
    img: ImageDocument
class Clips(BaseModel):
    clips: List[Clip]
'''