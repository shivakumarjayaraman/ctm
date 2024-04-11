# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): 
    return [dct[x] for x in keylist]

def list2dict(L, keylist):
    return {x : y for x, y in zip(keylist, L)}

def listrange2dict(L) :
    return {i:j for i, j in enumerate(L)}
