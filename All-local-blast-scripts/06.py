def process_fasta_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    # 假设文件格式正确，并且包含至少两条序列
    seq1_header = lines[0]  # 第一条序列的标题
    seq1 = lines[1]  # 第一条序列
    seq2_header = lines[2]  # 第二条序列的标题
    seq2 = lines[3]  # 第二条序列

    new_seq1 = seq1  # 第一条序列保持不变
    new_seq2 = []  # 初始化处理后的第二条序列

    # 遍历第二行的每个字符
    for i in range(len(seq1)):
        if i < len(seq2) and seq1[i] != 'N':  # 如果当前字符不是N，则保留
            new_seq2.append(seq2[i])
        elif i >= len(seq2):  # 如果第二序列较短，跳出循环
            break

    # 将处理后的序列和未变化的序列写入新文件
    with open(output_file_path, 'w') as output_file:
        output_file.write(seq1_header)
        output_file.write(''.join(new_seq1))
        output_file.write(seq2_header)
        output_file.write(''.join(new_seq2))

# 调用函数处理文件
input_file_path = '013.fas'
output_file_path = '014.fas'
process_fasta_file(input_file_path, output_file_path)
