def combine_lines_and_modify_fourth_line():
    # Initialize or clear the content of 015.fas
    with open('015.fas', 'w') as output_file:
        pass

    # Process query.fas and write the first two lines to 015.fas
    with open('015.fas', 'a') as output_file:
        with open('query.fas', 'r') as query_file:
            lines = query_file.readlines()[:2]
            output_file.writelines(lines)

    # Process 014.fas and append its third and fourth lines to 015.fas
    with open('015.fas', 'a') as output_file:
        with open('014.fas', 'r') as fas_file:
            lines = fas_file.readlines()[2:4]
            if len(lines) < 2:
                print("014.fas does not contain enough lines to add to 015.fas.")
            else:
                output_file.writelines(lines)

    # Modify the fourth line of 015.fas to replace 'N' with '-'
    with open('015.fas', 'r') as output_file:
        lines = output_file.readlines()

    if len(lines) >= 4:
        # Replace 'N' with '-' in the fourth line
        lines[3] = lines[3].replace('N', '-')
    
    # Rewrite the modified lines back to 015.fas
    with open('015.fas', 'w') as output_file:
        output_file.writelines(lines)

# Call the function to execute the operations
combine_lines_and_modify_fourth_line()