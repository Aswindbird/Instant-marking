#coding=utf-8
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
print unicode('<html><head><title>文本标记结果</title></head><body>', 'utf-8').encode('gbk')
title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*',r'<em><font color="#FF0000">\1</font></em>',block)
    block = re.sub(r'([a-zA-Z]+@[A-Za-z\.]+[A-Za-z]+)',r'<a href="mailto:\1">\1</a>',block)
    block = re.sub(r'(http://[\./a-zA-Z]+)',r'<a href="\1">\1</a>',block)
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title = False
    else:
        if len(block) <= 70 and not block[-1] == ':':
            print '<h2>'
            print block
            print '</h2>'
        else:
            if block[0] == '-':
                print '<li>'
                print block[1:]
                print '</li>'
            else:
                print '<p>'
                print block
                print '</p>'
print '</body></html>'