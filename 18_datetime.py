# import datetime
from datetime import datetime,timedelta;

# current datetime
cur_datetime = datetime.now();
print(cur_datetime);
print(datetime.today());

# current date
print(cur_datetime.date())

# Date formatting 26/01/2026
formatted_date=cur_datetime.strftime('%m/%d/%Y %h-%M');
print(formatted_date);


# date arithmetic

future_date=cur_datetime + timedelta(days=10)
print(future_date);

future_date=cur_datetime - timedelta(days=10)
print(future_date);

year=cur_datetime.year;
print(year);
month=cur_datetime.month;
print(month);
day=cur_datetime.day;
print(day);

