#dict lopala list
#s={101:["hari","cse","1year","1-2"],102:["sai","ece","1year","1-2"],103:["prasad","cse","2year","1-1"]}
#print(s)
#roll_no=int(input("enter roll_no: "))
#print(s.get(roll_no))
#print(s.get(roll_no),"not available")
#print(s.values())
'''
names=list(s.values())
print(names [0][0])
print(s.keys())
'''
#print(len(s)) #or print(len(s.keys()))
#dic lo set accept cheyyadhu
#ippudu list lopala dict
'''
s=[{101:"hari",22,"cse"},{102:"sai",23,"ece"},{103:"prasad",21,"cse"}]
print(s) #this is wrong methods or form to do 
'''
'''
l=[{"name":"hari","age":22,"group":"cse"},
   {"name":"dinesh","age":24,"group":"ece"}]
print(l)

print(l[0])
print(l[0]["age"])
#print(l.keys()) #get error as list doesnt contain key
print(l[0].items()) #output: dict_items([('name', 'hari'), ('age', 22), ('group', 'cse')])

l.append({"name":"ramya","group":"cse"})
print(l)
'''
# list lo dic, dict lo malli list for values
data=[{101:[5050,5]},{102:['mariegold',5]}]
print(data)
print(data[1].values())
