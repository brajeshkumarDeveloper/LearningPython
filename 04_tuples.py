#same as list , however you can't modify the item of tuple. immutable and ordered

days=('mon','tue','wed','thur','fri','sat','sun','mon');
print(days);
print(days[0:4]);
print(type(days));
# days[1]='brajesh'; can't to modify the value
print(days.count('mon'));
days=(1,2,3)
print(days);
print(days.index(3))