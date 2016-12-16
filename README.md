# instanceTest

def try_multiple_operations(items):
    for item in items:
        try:
            api.my_operation(item)
        except:
            print('error with item')

executor = concurrent.futures.ProcessPoolExecutor(10)
futures = [executor.submit(try_multiple_operations, group) 
           for group in grouper(5, items)]
concurrent.futures.wait(futures)
