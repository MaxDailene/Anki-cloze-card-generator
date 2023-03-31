n = 3  # number of previous words to insert
input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    prev_words = []  # buffer to store previous 'n' words
    first_line = True  # flag to skip prefix for first line
    for line in f_in:
        words = line.strip().split()
        if not first_line:
            prefix = "[...]"
            last_n_words = prev_words[-n:] if prev_words else []
            prev_line = " ".join(last_n_words)
            new_line = f"{prefix} {prev_line} {' '.join(words)}"
        else:
            new_line = " ".join(words)
        f_out.write(new_line + "\n")
        prev_words = words  # update previous words buffer
        first_line = False  # unset flag for first line
