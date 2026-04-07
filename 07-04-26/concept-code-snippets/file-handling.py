# write to file
with open("data.txt", "w") as f:
    f.write("Hello World")

# read from file
with open("data.txt", "r") as f:
    print(f.read())