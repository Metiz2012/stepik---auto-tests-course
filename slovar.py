def update_dictionary(d, key, value) :

    if key in d :
        d.setdefault(key,[]).append(value)

    elif (key not in d) and (key*2 in d) :
        d.setdefault(key*2,[]).append(value)
    else :
        d.setdefault(key*2, []).append(value)
