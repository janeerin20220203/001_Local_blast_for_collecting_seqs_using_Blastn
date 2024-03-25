def process_fasta_file(input_file_path, output_file_path):
    # 用于存储序列号和序列的字典
    sequences = {}
    
    # 读取FASTA文件
    with open(input_file_path, 'r') as input_file:
        current_seq_id = ''
        for line in input_file:
            if line.startswith('>'):  # 序列标题行
                current_seq_id = line.strip()
                sequences[current_seq_id] = []
            else:  # 序列数据行
                sequences[current_seq_id].append(line.strip())
    
    # 写入新的FASTA文件
    with open(output_file_path, 'w') as output_file:
        for seq_id, seq_lines in sequences.items():
            # 合并序列行，并替换'-'为'N'
            seq = ''.join(seq_lines).replace('-', 'N')
            output_file.write(f"{seq_id}\n{seq}\n")

# 设置文件路径
input_file_path = '012.fas'
output_file_path = '013.fas'

# 调用函数
process_fasta_file(input_file_path, output_file_path)

# 输出新文件的路径
print("Processed file saved to:", output_file_path)

