class DotDict(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError:
            raise AttributeError(key)
        
def printd(N, text):
    if N >=4: return
    print(text)

from importlib import import_module

def load_func(dotpath : str):
    """ load function in module.  function is right-most segment """
    module_, func = dotpath.rsplit(".", maxsplit=1)
    m = import_module(module_)
    return getattr(m, func)

import re
def compile_jq(expression, data):
    l1, l2 = 3, 4

    def prepend_path(item_path_pair, edge):

        if isinstance(item_path_pair, tuple):
            item, path = item_path_pair
            return (item, f'{edge}.{path}')
        elif isinstance(item_path_pair, str):
            return (item_path_pair, f'{edge}')
        elif isinstance(item_path_pair, list):
            return [prepend_path(ip, edge) for ip in item_path_pair]
        elif isinstance(item_path_pair, dict):
            return (item_path_pair, f'{edge}')
        else:
            #return (item_path_pair, f'{edge}')
            raise ValueError(f'prepend_path: unknown input {item_path_pair}')
        
    def traverse(obj, path):
        printd(l1, f'path = {path}')
        if len(path) == 0:
            return obj
        key = path[0]
        printd(l1, f'key = {key}, obj={type(obj)}')
        if isinstance(obj, dict):
            print(l1, 'obj dict')
            if key in obj:
                return prepend_path(traverse(obj[key], path[1:]), key)
            else:
                raise ValueError(f'Invalid: key = {key}, obj={obj}')
        elif isinstance(obj, list):
            printd(l1, 'obj list')
            if key == '[]':
                item_path_pairs = [prepend_path(
                                    traverse(item, path[1:]), pos
                                ) 
                               for pos, item in enumerate(obj)]
                return item_path_pairs
            else:
                key = int(key) 
                obj_ = obj[key]
                return prepend_path(traverse(obj_, path[1:]), key)
        else:
            return obj

    def parse(expression):
        expression_array = re.findall(r'\w+|\[\]', expression) #split f.e[].d
        printd(l1, expression_array)
        return expression_array

    path = parse(expression)
    ret = traverse(data, path)
    if isinstance(ret, tuple):
        ret = [ret]
    assert isinstance(ret, list) #always returns lists of items
    printd(l2, f'traverse return: {ret}')
    return ret