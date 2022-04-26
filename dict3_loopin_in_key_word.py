# check in code which values are stored in dict that was present or not
'''user_info={
    'Name':'Shubham',
    'Age':'22',
    'Fav_movies':['Tiranga'],
    'Fav_tune':['Mahadev'],
    }
print(user_info)
if 'Name' in user_info:
    print("Present")
else:
    print("Not present")

'''
# check value in dict by looping
user_info={
    'Name':'shubham',
    'Age':'22',
    'Fav_movies':['Tiranga'],
    'Fav_tune':['Mahadev'],
    }
if 'shubham' in user_info.values():
    print("Present")
else:
    print("Not present")
