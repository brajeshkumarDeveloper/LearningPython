marks={'Hindi':80,'English':90};
print(marks);
print(type(marks));
print(marks['English']);

car={'brand':'Ford','model':'Mustang','year':2007}
print('Brand of card is',car['brand']);
print('Model is ' +car['model']);

print(marks.get('Hindi'));
print(marks.get('Maths'));
# add dictionary
marks['Maths']=98;
print(marks);
print(marks.get('Maths'));

# delete dictionary
del marks['Hindi'];
print(marks);

# getting no. of key-value dictionary
print(len(marks));