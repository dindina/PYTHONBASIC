import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args , **kwargs)
        end_time = time.time()
        execution_time = round(end_time-start_time)
        print(f" time taken  {execution_time} seconds")
        return result
    return wrapper

@timer
def function1():
    time.sleep(2)
    return "Over"

@timer
def function2():
    time.sleep(1)
    return "Over"

function1()
