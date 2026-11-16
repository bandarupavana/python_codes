d={"name":"python","age":1991,"trend":"yes"}
'''
print(d)
print(d["trend"])
#print(d["marks"]) #thows key error
print(d.get("marks"))# using makes if key isnt presnt then it thows none else it gives the value
print(d.keys())
print(d.values())
print(d.items())
'''
'''
d.update(name="pfs",age=22)
print(d)
d.update({"role": "ds"})
print(d)
'''
'''
d.update([("city","hyd")])
print(d)
d.update([("1","55")])
print(d)
'''
d.update({"1":"done"})
print(d)
'''
d.setdefault("age",2000)
print(d)
d.setdefault("practice","done")
print(d)
'''
'''
d.setdefault("time")
print(d)
'''
