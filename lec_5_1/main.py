# def modify_list(my_list):
#     my_list.append(10)  # Modifies the list in place

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # Output: [1, 2, 3, 10] - List was modified







# def modify_value(x):
#     x = x + 1  # This creates a new integer, does not modify the original

# x = 5
# modify_value(x)
# print(x)  






# def print_args(*args):
#     for arg in args:
#         print(arg)

# print_args(1, 2, 3, "Hello", [4, 5])



# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")

# print_kwargs(name="Alice", age=30, job="Engineer")




# ## kwargs example

# def log_event(event_type, *args, **kwargs):
#     print(f"Event: {event_type}")
#     print("Details:", args)
#     print("Extra info:", kwargs)

# log_event("Error", "File not found", "Path: /files", code=404, urgent=True)





# original_list = [1, 2, 3, 4, 5]
# sliced_list = original_list[1:4]

# print(sliced_list)  # Output: [2, 3, 4]





# original_list = [1, 2, 3, 4, 5]
# sliced_list = original_list[1:4]
# sliced_list[0] = 10

# print(original_list)  # Output: [1, 2, 3, 4, 5]
# print(sliced_list)    # Output: [10, 3, 4]



# original_list = [[1, 2], [3, 4], [5, 6]]
# sliced_list = original_list[:]

# # Modify the first inner list in the sliced list
# sliced_list[0][0] = 10

# print(original_list)  # Output: [[10, 2], [3, 4], [5, 6]]
# print(sliced_list)    # Output: [[10, 2], [3, 4], [5, 6]]

# #### shallow copy and deep copy



# import copy

# deep_copied_list = copy.deepcopy(original_list)
