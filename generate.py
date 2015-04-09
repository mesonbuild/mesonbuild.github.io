#!/usr/bin/env python

pages = [('Main page', 'index'),
         ('Download', 'download'),
         ('Videos', 'videos'),
         ('Documentation', 'documentation'),
         ('Development', 'development'),
         ('Community', 'community'),
         ('Legal', 'legal')]

pref = open('prefix.html').read()
suf = open('suffix.html').read()

repl = ''
for p in pages:
    repl += '<li><a href="%s.html">%s</a></li>\n' % (p[1], p[0])

pref = pref.replace('@@@', repl)


for p in pages:
    ifile = p[1] + '.shtml'
    ofile = p[1] + '.html'
    cur = open(ifile).read()
    open(ofile, 'w').write(pref + cur + suf)


