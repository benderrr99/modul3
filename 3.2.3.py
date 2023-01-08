d={'name1':'id1', 'name2':'id2', 'name3':'id3',}
n_d = {}
for key, value in d.items():
    n_d[value] = key
print(n_d)