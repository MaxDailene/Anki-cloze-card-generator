# A script that removes all cloze deletion cards from a given .txt file.

import re

input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as f_in, open(output_file, "w") as f_out:

    for line in f_in:

        line = re.sub(r"{{c\d+::(.*?)}}", r"\1", line)

        f_out.write(line)
