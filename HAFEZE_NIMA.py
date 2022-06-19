list_momrize = [{}]
def memorize(**kwargs):
    sorted_dict = {}

    #print(kwargs)
    def inner():

        nonlocal sorted_dict




        list_key = sorted(kwargs)
        sorted_dict = {i: kwargs[i] for i in list_key}
        list_1 = sorted_dict


        for key, val in list_1.items():
            val = val.split(', ')
            val = sorted(val, key=lambda x: (len(x), x))
            list_1[key] = val

        #print(sorted_dict)
        list_momrize.append(sorted_dict)
        #print('list_momrize= ',list_momrize)



    return inner()





if __name__ == '__main__':
    exec(input().replace('\\n', '\n'))

for i in range(len(list_momrize)-1):
    if list_momrize[i] == {}:
        print('None')

    for key, val in list_momrize[i].items():
        print(f'{key}: {", ".join(val)}')

    print()