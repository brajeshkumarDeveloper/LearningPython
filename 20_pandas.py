import pandas

data= pandas.read_csv('myFile.csv')
# print(data.salary)
# print(data.salary.min())
# print(data.salary.max())
# print(data.salary.sum())
print(data[data.id==1098])
# print(data[data.salary==data.salary.max()])
# print(data[data.salary==data.salary.min()])
# print(data.salary.mean())
# print('*'*60)
# emp_id_1036= data[data.id==1036]
# print(emp_id_1036.firstname.values[0],emp_id_1036.lastname.values[0]);

# print(data.salary.to_list())
# print(data.to_dict())
# update the salary
# data.loc[data.id==1098, 'salary']= 8000
# print(data)

# remove the data

# mariann_index=data.index[data.id==100].to_list()[0]
# print(mariann_index)
# data =data.drop(mariann_index)
# print(data)

# sorting the salary des
# data = data.sort_values(by='salary',ascending=False)
# print(data)

# data['bonus']= data.salary *0.1
# print(data)

# data=data.drop('salary',axis=1)
# print(data)

# data.to_csv('myFile_modified.csv')

