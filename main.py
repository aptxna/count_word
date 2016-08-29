import sys
import os
import string
import re
from collections import Counter

f = open('v_for_vendetta.txt', 'r')

str = f.read().strip()
str = re.split(r'[:,!;.\s]\s*', str)

s = r'^[Vv]\w+'
c = 0
result = []

for word in str:
	if re.match(s, word) and word not in result:
		result.append(word)

for w in result:
	c = c + 1
	print c, w