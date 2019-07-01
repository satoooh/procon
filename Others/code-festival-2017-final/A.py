"""
正規表現を利用する。
"""

import re
l = re.compile("^A?KIHA?BA?RA?$").findall(input())
if l:
	print("YES")
else:
	print("NO")
