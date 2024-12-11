import re

# Pattern to match lines starting with "rr" or "r(n)" where n is a number from 1 to 99
pattern = re.compile(r"^r(r|\d{1,2})")

# Open the input file and create a new output file
with open('blacklist.txt', 'r') as infile, open('filtered_blacklist.txt', 'w') as outfile:
    for line in infile:
        # If the line does not start with the specified pattern, write it to the output file
        if not pattern.match(line):
            outfile.write(line)

print("Filtering complete. Check 'filtered_blacklist.txt' for the results.")

