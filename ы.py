objects=[1,2,3,555,323223,34544,75747,6535355,356353553,6333566,6758685,5621414,43323223,878878778,433323,545454,1,2,3]


temp = []
for obj in objects:
    contains = False
    for tobj in temp:
        if not contains and tobj == obj:
            contains = True

    if not contains:
        temp.append(obj)

print(len(temp))

