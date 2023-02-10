def LineSkip(file_path, n):
    with open(file_path, "r", encoding='utf-8') as file:
        lines = file.readlines()
        
    with open(file_path, "w", encoding='utf-8') as file:
        for i, line in enumerate(lines):
            if (i + 1) % n != 0:
                file.write(line)

file_path = "example.txt"
n = 3

LineSkip(file_path, n)

print("Operation completed successfully!")
