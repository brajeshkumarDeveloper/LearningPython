def person(mame,age,job, **data):
    print(mame, age, job)
    print(data)
    for key,value in data.items():
        print(f"{key}: {value}")



person('Alice', 30, 'Engineer', city='New York', hobby='Painting')