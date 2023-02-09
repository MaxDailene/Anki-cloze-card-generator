def LineSkip(file_path, n):
    with open(file_path, "r") as file:
        lines = file.readlines()
        
    with open(file_path, "w") as file:
        for i, line in enumerate(lines):
            if (i + 1) % n != 0:
                file.write(line)

file_path = input("Enter the path of the file: ")
n = int(input("Enter the value of n: "))

LineSkip(file_path, n)

print("Operation completed successfully!")
