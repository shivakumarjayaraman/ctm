#!/usr/bin/env python

from math import *

def create_voting_dict(strlist) :
    d = {}
    for line in strlist :
        entries = line.split()
        d[entries[0]] = [int(x) for x in entries[3:]]
    return d
    
def policy_compare(sen_a, sen_b, voting_dict) :
    v1 = voting_dict[sen_a]
    v2 = voting_dict[sen_b]
    return sum(a*b for a, b in zip(v1, v2))
    
def most_similar(sen, voting_dict) :
    similar_dude = ""
    similar_count = -inf
    for sens in voting_dict.keys() :
        if (sen == sens) : continue
        similarity = policy_compare(sen, sens, voting_dict)
        if (similarity > similar_count) :
            similar_dude = sens
            similar_count = similarity
    return similar_dude, similar_count
        
f = open("voting_record_dump109.txt")
d = create_voting_dict(list(f))
print (most_similar('Chafee', d))


