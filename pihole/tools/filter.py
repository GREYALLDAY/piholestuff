def remove_duplicates(input_file, output_file):
    seen_lines = set()
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Check if the line has been seen before
            if line not in seen_lines:
                # If it's a new line, write it to the output file and add to the set
                outfile.write(line)
                seen_lines.add(line)

    print(f"Duplicate entries removed. Check '{output_file}' for the results.")

# Specify the input and output file names
input_filename = 'blacklist.txt'
output_filename = 'blacklist-nodupe.txt'

# Call the function to remove duplicates
remove_duplicates(input_filename, output_filename)

