# Dictionary

# copy
Original_dictionary = {"name:""Yoge","age:"'30',"city:""Newyork"}
# creating shallow copy using dictionary
copied_dictionary = Original_dictionary.copy()
print("Origional_dictionary:",Original_dictionary)
print("copied_dictionary:",copied_dictionary)

# clear
Original_dictionary = {"name:""Yoge","age:"'30',"city:""Newyork"}
print("Original_dictionary:",Original_dictionary)
print("Original_dictionary length:",len(Original_dictionary))
Original_dictionary.clear()
print("Original_dictionary:",Original_dictionary)
print("Original_dictionary length:",len(Original_dictionary))

#pop
Original_dictionary = {"name:""Yoge","age:"'30',"city:""Newyork"}
print("Original_dictionary:",Original_dictionary)
print("Remove:",Original_dictionary.pop( ))
print("remove items:",Original_dictionary)

# values
emp = {'name':'kevin','age':25,'job':'hr','sal':72500}
print(emp)
values = emp.values()
print('values:',values)

# items
emp = {'name':'kevin','age':25,'job':'hr','sal':72500}
print('origional_emp:',emp)
print("items:",emp.items())
emp={}
print('empty_items:',emp)

# keys
emp = {'name':'kevin','age':25,'job':'hr','sal':72500}
print('original:',emp)
print('keys:',emp.keys())
emp={}
print('empty key:',emp)

# get
dname = {1:'apple',2:'mango',3:'kiwi',4:'orange'}
print('origional_dname:',dname)
print("get 1st item:",dname.get(1))
print("get 2st item:",dname.get(2))
print("get 3st item:",dname.get(3))
print("get 4st item:",dname.get(4))

# fromkeys
keys = {'a','b','c','d','e'}
oh = dict.fromkeys(keys)
print(oh)

# update
my_dict = {1:'apple',2:'mango'}
my_newdict = {3:'banana',4:'kiwi'}
my_dict.update(my_newdict)
print(my_dict)

# setdefault
emp = {'name':'kevin','age':25,'job':'hr','sal':72500}
print(emp.setdefault('name',None))
print(emp.setdefault('age',None))

# min and max value
r1 = {'a':25,'b':65,'h':10}
e=min(r1.values())
print(e)
f=max(r1.values())
print(f)