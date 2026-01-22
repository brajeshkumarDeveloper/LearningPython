#Ordered Sequence of different type of values
name='brajesh';
print(name);
"""
user_list=['brajesh','john','jane'];
print(user_list);
print(user_list[2]);
# print(user_list[3]); out of index throwing error

# add new user in list
user_list.append("paul");
print(user_list);

#remove the user in list
user_list.remove("brajesh");
print(user_list);

#modify the value from a list

user_list[0]=('kumar');
print(user_list);

user_list.insert(0,'sanu')
print(user_list);

del user_list[2]
print(user_list);

#length of list
print(len(user_list));

#sorting the items in list
user_list.sort();
print(user_list);

#reverse sorting
# user_list.sort(reverse=True);
user_list.reverse()
print(user_list);


#popping the item in list
# user_list.pop();
removed_value=user_list.pop();
print(user_list);
print(removed_value);

# getting first item\
# user_list[:1]
print(user_list[0:1]);

print(user_list[1:2]);

print(user_list[-2]);
"""

#Numeric List
marks=[2,5,56,8,3.5,23,65,39];
# Getting the min or max
print(min(marks));
print(max(marks));
print(sum(marks));
print(len(marks));

mix_list=['paul',10,100.21, True];
print(mix_list);



