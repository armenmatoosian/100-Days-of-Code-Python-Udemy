# file = open("my_file.txt")
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
    # file.close()

# with open("my_file.txt", mode="a") as file:
#     contents = file.write("\nNew text.")
#     print(contents)

with open("new_file.txt", mode="w") as file:
    file.write("New text.")