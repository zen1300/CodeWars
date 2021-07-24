def name_list(s):
    names = [i['name'] for i in s]
    last = len(names[-1])
    joined = ', '.join(names)
    joined = joined[:-last-2] + ' & ' + names[-1]
    print(joined)

name_list([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
