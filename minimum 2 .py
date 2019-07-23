def update_dictionary(d, key, value) :

    if key in d :
        d.setdefault(key , []).append(value)

    elif (key not in d) and (key*2 in d) :
        d.setdefault(key * 2, []).append(value)
    else :
        d.setdefault(key*2,[]).append(value)

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}