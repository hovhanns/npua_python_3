# # reading and writing text files
# # write a code that reads a file and writes it to another file
import os

# file_path = "lec_7.txt"
# f = open(file_path, "r")
# data = f.read()
# print(data)

# f.seek(5)
# print(f.read(10))
# print("---------------")

# f.seek(0)
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)

# while line:
#     print(line, end="")
#     line = f.readline()

# print("line", line)

# f.seek(0)
# lines = f.readlines()
# print(lines)

# # write to a file

# f = open("write.txt", "a")
# f.write("barev\n")
# f.write("vonc eq?")
# f.close()


# os.remove("write.txt")

# os.chdir("../")
# f = open("write.txt", "a")
# f.write("barev\n")
# f.close()

# os.remove("write.txt")

# print(os.getcwd())

try:
    f = open("write.txt", "r")
    os.remove("write.txt")
    a = 10 / 0
except FileNotFoundError as e:
    print("IN file not found", e)
except ZeroDivisionError as e:
    print("IN zero division", e)
except Exception as e:
    print("IN exception", e)
else:
    print("file removed successfully")
finally:
    f.close()
    print("this is always executed")
