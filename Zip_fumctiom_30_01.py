

names =("Alice", "Bob", "Charlie")
comps=("Google", "Microsoft", "Amazon")

zipped= list(zip(names, comps))
# zipped_set= set(zip(names, comps))
# print("set",zipped_set)
# print("list",zipped)
#
# zipped_dic = dict(zip(names, comps))
# print("dict",zipped_dic)

for (a,b) in zipped:
    print(a,"works at",b)


