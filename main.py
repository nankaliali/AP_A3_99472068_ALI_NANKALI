def average_tuple(two_dimentional_tuple):
    return tuple(map(lambda x: sum(x)/len(x), list(zip(*two_dimentional_tuple))))



if __name__ == '__main__':
    expression_to_evaluate = input()
    print(eval(expression_to_evaluate))