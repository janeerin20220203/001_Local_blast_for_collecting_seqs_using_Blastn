import os
import chardet

def detect_encoding(file_path):
    """Detect the file encoding"""
    with open(file_path, 'rb') as file:
        raw_data = file.read(10000)  # Read the first 10000 bytes to determine encoding
        result = chardet.detect(raw_data)
        return result['encoding']
 
def convert_to_utf8(file_path, original_encoding):
    """Converts the file to UTF-8 encoding"""
    with open(file_path, 'r', encoding=original_encoding) as file:
        content = file.read()
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_sequence(sequence):
    """Processes the sequence to ensure all bases remain at their original positions.
    Replaces bases in incomplete codons with '-'. A codon is incomplete if it includes at least one '-'."""
    processed_sequence = ""
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        # Replace each base in the incomplete codon with '-'
        if len(codon) < 3 or '-' in codon:
            processed_sequence += '-' * len(codon)  # Replace the number of bases in the codon
        else:
            processed_sequence += codon  # Keep complete codons unchanged
    return processed_sequence

def process_fasta_file(input_file_path, output_file_path):
    """Reads a FASTA file, processes the fourth line according to specific rules, then writes the result to a new file."""
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
    
    # Check if the file has at least four lines
    if len(lines) < 4:
        print("The input file does not meet the requirements; it needs at least 4 lines.")
        return
    
    # Process the fourth line sequence
    processed_sequence = process_sequence(lines[3].strip())
    
    # Write the first three lines and the processed fourth line to the output file
    with open(output_file_path, 'w') as output_file:
        for line in lines[:3]:
            output_file.write(line)
        output_file.write(processed_sequence + '\n')

# Specify the input and output file paths
input_file_path = '015.fas'
output_file_path = '016.fas'

# Detect and convert encoding to UTF-8 if necessary
file_encoding = detect_encoding(input_file_path)
if file_encoding != 'utf-8':
    convert_to_utf8(input_file_path, file_encoding)
    print(f"{input_file_path} has been converted to UTF-8.")

# Process the FASTA file
process_fasta_file(input_file_path, output_file_path)

print("File processing complete. Output saved in", output_file_path)

