


# # original_list = [1, 2, 3, 4, 5]
# # sliced_list = original_list[1:4]

# # print(sliced_list)  # Output: [2, 3, 4]





# # original_list = [1, 2, 3, 4, 5]
# # sliced_list = original_list[1:4]
# # sliced_list[0] = 10

# # print(original_list)  # Output: [1, 2, 3, 4, 5]
# # print(sliced_list)    # Output: [10, 3, 4]



# original_list = [[1, 2], [3, 4], [5, 6]]
# sliced_list = original_list[:]

# print(original_list)
# print(sliced_list)
# # Modify the first inner list in the sliced list
# sliced_list[0][0] = 10
# original_list[0][1] = 10000
# sliced_list[1] = 3000

# print(original_list)  # Output: [[10, 2], [3, 4], [5, 6]]
# print(sliced_list)    # Output: [[10, 2], [3, 4], [5, 6]]

# #### shallow copy and deep copy



# import copy

# print("----------------")
# print(original_list)

# deep_copied_list = copy.deepcopy(original_list)
# deep_copied_list[0][0] = 100
# print(original_list)


# l = [1, 2, 3, 4, 5, 6]

# import math
# def f(x):
#     # return complex math equation
#     return math.sqrt(x) + math.log(x) + math.sin(x)
    

# new_l1 = []
# for i in l:
#     new_l1.append(i*2)

# # check if i is even using comprehension
# new_l2 = [i*2 if i%2 == 0 else 0 for i in l]
# # keep only if statement
# new_l3 = [i*2 for i in l if i%2 == 0]
# new_l2[100]
# new_2 = [f(i) for i in l]

# print(new_l3)


# array_2d = [[1, 2, 3], 
#             [4, 5, 6], 
#             [7, 8, 9],
#             [10, 11, 12]] 
# for i in range(len(array_2d)):
#     for j in range(len(array_2d[i])):
#         print(array_2d[i][j], end=" ")
#     print()

import random

#random.seed(0)
print(random.randint(1, 10))
print(random.randrange(1, 10))
print(random.uniform(1, 10))
print(random.choice(['a', 'b', 'c', 'd']))
print(random.random())
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(l)
print(l)