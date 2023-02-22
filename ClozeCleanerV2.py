import fileinput
import re

with fileinput.FileInput("filename.txt", inplace=True) as file:

    for line in file:

        line = re.sub(r"{{c\d+::(.*?)}}", r"\1", line)

        print(line, end="")
