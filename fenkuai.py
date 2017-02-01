#date: 2017-1-21
#author: bird

import sys

f = open('simple.txt','r')
file = f.readlines()

def lines(file) :
    for line in file :
        yield line
    yield '\n'

def blocks(file) :
    block = []
    for line in lines(file) :
        if line != '\n' :
            block.append(line)
        else:
            yield block
            block = []
        # print block
print '<html><head><title>jishibiaoji</title></head><body>'
for block in blocks(sys.stdin):
    print '<h1>'
    print block
    print '</h1>'
print '</body></html>'