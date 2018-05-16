#!/usr/bin/python
"""learning mylist,tuple,dictionary"""
a={"sadma":"movie","language":"hindi","language":"telugu"}
print a["sadma"]
b=(123,"a","sri","anu","devops")
print b[-1]
print b[1:4]
#print b[-1:3]
print b[2:-1]
d="hello devops"
print d[2]
print d[2:7]
#print d[-1:-5]
print d[4:-3]
e={"course":[123,"java",{"lang":"php"}],"language":"c","language2":"java","language3":"php"}
print e["course"]
print e["course"][0]
#print e[0][0]
print e["course"][2]
print e['course'][2]['lang']
print e["course"][-1]["lang"]
