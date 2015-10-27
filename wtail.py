# -*- coding: utf-8 -*-
import tailer
from sys import argv

script, filename = argv

for original in tailer.tail(open(filename),50):
    print original

for line in tailer.follow(open(filename)):
    print line
