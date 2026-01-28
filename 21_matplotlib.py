import pandas
import matplotlib.pyplot as plt

data=pandas.read_csv('myFile.csv')
print(data)

# plt.plot(data.id,data.salary)
# plt.bar(data.id,data.salary)

# plt.scatter(data.id,data.salary)
# plt.xlabel('id')
# plt.ylabel('salary')
# plt.title('Id vs Salary')
# plt.show()

print('*'*60)
city_count=data.city.value_counts()

plt.bar(city_count.index,city_count.values)
plt.xlabel('city')
plt.ylabel('count')
plt.title('city vs no of users')
plt.show()
# print(city_count)
