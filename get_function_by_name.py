def get_function_by_name(function_name):

    file_functions = globals().copy()
    file_functions.update(locals())
    function = file_functions.get(function_name)
    if not function:
        return lambda: ...
    else:
        return function


def function_with_weird_name():
    print('I am a function with a weird name')


function_founded = get_function_by_name('function_with_weird_name')

function_founded()
