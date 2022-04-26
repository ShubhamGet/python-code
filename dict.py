# Dictionary Define:-
# A dictionary is an unordered,Changeable and indexed collection that have "key" and "value".
# In dict duplicated key are omited.
# In py dict are written with CURLY bracket like as {}
# syntax-------------------dict={"key:"value"}
'''
names={'Shubham','maan','Singh'}
print(names)
print(type(names))'''


#Another method to create dictionary alos called as dict.

'''user=dict(name='shubham',age='22')
print(user)'''


# switch case (using dict)
'''
switch={
    1:"Maan",
    2:"Shubham",
    3:"Golu",
    4:"Arnav",
  }
num=int(input("Enter user ur own choice:\n"))
if num<5:
    print("valid number:")
else:
    print("\n:Invalid number:")
print(switch.get(num))

'''
#1.method
'''
user_info={
    'Name':'Shubham',
    'Age':'22',
    'Fav_movies':['Tiranga'],
    'Fav_tune':['Mahadev'],
    }
print(user_info)
for key,value in user_info.items():
    print(f"{key}:{value}")

#2. method

    user_info={
    'Name':'Shubham',
    'Age':'22',
    'Fav_movies':['Tiranga'],
    'Fav_tune':['Mahadev'],
    }
print(user_info)
for key,value in user_info.items():
    print(f"{key}:{value}")
'''    
# How to access/show items which are stored in dict.
user_info={
    'Name':'Shubham',
    'Age':'22',
    'Fav_movies':['Tiranga'],
    'Fav_tune':['Mahadev'],
    }
print(user_info)
print("\n")
print(user_info['Fav_tune'])
print(user_info['Fav_movies'])
