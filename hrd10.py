
import sys


n = int(raw_input().strip())


b = bin(n)

s = str(b)

print("the string: %s" % s)

curOneGroup = 0
maxOneGroup = 0
for i in range(0, len(s)):
  print("VAL: %s" % s[i])
  if (s[i] == '1'):
    curOneGroup += 1
    if curOneGroup > maxOneGroup:
      maxOneGroup = curOneGroup
  else:
    curOneGroup = 0

print("%d" % maxOneGroup)

