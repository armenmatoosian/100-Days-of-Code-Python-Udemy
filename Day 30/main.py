#FileNotFound
#with open("a_file.txt) as file:
#   file.read()

# try:
#     file = open("a_file.text")
#     a_dictionary = {"key": "value"}
#     # print(a_dictionary["sdfsdf"])
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.text", "w")
#     file.write("Something")
# # except KeyError:
# #     print("That key does not exist")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed")
#     raise TypeError("This is an error I made up.")

#KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key]

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

# code for Raising your own Exceptions

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 metres.")

bmi = weight / height ** 2
print(bmi)