what_is_this = input("please input a function in vanilla Python: ")
function = eval(what_is_this)
print(function.__doc__)
help(function)
