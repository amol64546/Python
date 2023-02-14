
# mode - "r", "w", "a", "r+"
text_file = open("file_handling/hello.txt","a")

text_file.write("\nHow your doing")

text_file = open("file_handling/hello.txt","r")
# print(text_file.readable())

# print(text_file.readline())
# print(text_file.readline())

print(text_file.readlines())

# print(text_file.readlines()[1])



text_file.close()