#date: 2017-1-21
#author: bird

import sys,re

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
            yield ''.join(block).strip()
            block = []
        # print block
print '<html><head><title>jishibiaoji</title></head><body>'
title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*',r'<em><font color="#FF0000">\1</font></em>',block)
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title = False
    else:
        print '<p>'
        print block
        print '</p>'
print '</body></html>'