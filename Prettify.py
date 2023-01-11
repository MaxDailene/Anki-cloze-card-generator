def process_file(filepath):
    definitions = []
    with open(filepath, "r") as file:
        headword = file.readline().strip()
        for line in file:
            line = line.strip()
            if line:
                definitions.append(line)
    with open("output.txt", "w") as file:
        file.write(f"Headword: {headword}\n")
        for i, definition in enumerate(definitions):
            file.write(f"Definition{i + 1}: {definition}\n")

filepath = "output.txt"
process_file(filepath)