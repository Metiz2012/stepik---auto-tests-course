objects=[500,2,500,2,555,323223,34544,75747,6535355,356353553,6333566,6758685,5621414,43323223,878878778,433323,545454,1,2,3,65566556,776767676767]

temp=[]

def my_contains(array, element):
    contain = False
    for i2 in array:
        if i2 is element:
            contain = True

    return contain

for i in objects:
    if not my_contains(temp, i):
        temp.append(i)

print(len(temp))