def id_best_users(*args):
    results = []
    temp = {}
    flat = [i for arg in args for i in arg]
    unique = set(flat)
    for val in unique:
        if all([val in arg for arg in args]):
            counts = 0
            for arg in args:
                for i in arg:
                    if i == val:
                        counts += 1
            if counts not in temp:
                temp[counts] = [val]
            else:
                temp[counts].append(val)
                temp[counts] = sorted(temp[counts])
    if temp:
        results = [[k, v] for (k, v) in sorted(temp.items(), reverse=True)]
    return results


a1 = ['A042', 'B004', 'A025', 'A042', 'C025']
a2 = ['B009', 'B040', 'B004', 'A042', 'A025', 'A042']
a3 = ['A042', 'A025', 'B004']
print(id_best_users(a1, a2, a3))