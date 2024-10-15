def modify_list(my_list):
    new_list = my_list.copy() 
    new_list.append(10)  # Modifies the list in place

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  


def modify_value(x):
    x = x + 1  # This creates a new integer, does not modify the original

x = 5
modify_value(x)
print(x)  


def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3, "Hello", [4, 5])



def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_kwargs(name="Alice", age=30, job="Engineer")




# ## kwargs example

def log_event( *args, **kwargs):
    print("Details:", args)
    print("Extra info:", kwargs)

log_event("Error", "File not found", "Path: /files", code=404, urgent=True)
