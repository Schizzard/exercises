# Step 5

# Solve 1 (my)
def update_dictionary(d, key, value):
    if key in d: 
        d[key]+=[value]
    else: 
        if key*2 in d:
            d[key*2]+=[value]
        else:
            d[key*2]=[value]


# Solve 2 (from comments)
def update_dictionary(d: dict, k, v):
    if k in d:
        d.setdefault(k, []).append(v)
    else:
        d.setdefault(k*2, []).append(v)

# Solve 3 (from comments)
def update_dictionary(d: dict, key, value):
    key += key * (key not in d)
    d[key] = d.get(key, []) + [value]