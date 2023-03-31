n = 3  # number of previous words to insert
input_file = "input.txt"

with open(input_file, "r+") as f:
    prev_words = []  # buffer to store previous 'n' words
    first_line = True  # flag to skip prefix for first line
    lines = f.readlines()
    f.seek(0)
    f.truncate()
    for line in lines:
        words = line.strip().split()
        if not first_line:
            prefix = "[...]"
            last_n_words = prev_words[-n:] if prev_words else []
            prev_line = " ".join(last_n_words)
            new_line = f"{prefix} {prev_line} {' '.join(words)}"
        else:
            new_line = " ".join(words)
        f.write(new_line + "\n")
        prev_words = words  # update previous words buffer
        first_line = False  # unset flag for first line
