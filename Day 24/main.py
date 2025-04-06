# file = open("my_file.txt")
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
    # file.close()

# with open("my_file.txt", mode="a") as file:
#     contents = file.write("\nNew text.")
#     print(contents)

# with open("new_file.txt", mode="w") as file:
#     file.write("New text.")

# code for challenge in Understand Relative and Absolute File Paths
# # using absolute file path
# with open("/Cloud Storage/GoogleDrive_Gmail/Programming/100 Days of Code Python Udemy/new_file.txt") as file:
#     contents = file.read()
#     print(contents)

# using relative file path
with open("../new_file.txt") as file:
    contents = file.read()
    print(contents)