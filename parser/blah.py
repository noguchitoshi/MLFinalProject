a = dict()
a["hello"] = 2
try:
  a["hello"] += 1
except:
  a["hello"] = 1


try:
  a["blah"] += 1
except:
  a["blah"] = 1

print a["hello"]
print a["blah"]
