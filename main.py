# Opens a file, Does same as code below but automatically closes when done
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

#file = open("my_file.txt")
#contents = file.read()
#print(contents)
#file.close()

# Writes to files, w-replaces current text, a-appends(adds to current text)
#with open("my_file.txt", mode="a") as file:
#    file.write("\nNew text.")

# creates new file
with open("new_file.txt", mode="w") as file:
    file.write("New textaroni.")
