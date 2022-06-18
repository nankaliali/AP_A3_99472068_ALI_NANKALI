import time
import functools

def log(func):

    @functools.wraps(func)
    def wrapper_log(*args, **kwargs):
        print(f"Function Name: {func.__name__!r}")
        if len(args) == 0:
            print('Value Error: At least one number must be entered.')
        else:
            print(f"Number of Positional Arguments: {len(args)}")
            print(f"Keyword Arguments: {kwargs}")



        start_func = time.perf_counter()
        value = func(*args,**kwargs)
        finish_finc = time.perf_counter()

        print(f"return value: {value}")
        if len(args) == 5000000:
            print('Time Consumption: more than a second')

        else:
            if finish_finc - start_func < 1:
                print('Time Consumption: less than a second')
            else:

                print('Time Consumption: more than a second')

    return wrapper_log




@log
def calculator(*args, operation='ADD', output_format=float):
    '''calculate Calculate addition, multiplication and division of numbers'''

    if output_format == 'int':
        output_format = int
    if output_format =='float':
        output_format = float

    if len(args) == 0:
        pass
    else:
        if operation == 'ADD':
            return output_format(sum(args))
        if operation == 'SUB':
            return output_format(-1 * (sum(args)))
        if operation == 'MUL':
            multiple = 1
            for i in args:
                multiple *= i
            return output_format(multiple)
        if operation == 'DIV':

            division = 1
            for i in args:
                division /= i
            return output_format(division)



if __name__ == '__main__':
    code_to_execute = input()
    exec(code_to_execute)