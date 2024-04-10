def complement(sequence):

    """返回DNA序列的反向互补序列。"""
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N', 'a': 't', 't': 'a', 'c': 'g', 'g': 'c', 'n': 'n'}
    return ''.join(complement_dict[base] for base in sequence[::-1])

def extract_sequences(blast_results_path, genome_sequence_path, output_path):
    # 读取BLAST结果
    with open(blast_results_path, 'r') as file:
        blast_lines = file.readlines()

    # 读取基因组序列文件
    with open(genome_sequence_path, 'r') as file:
        genome_data = file.read()
        genome_sequences = {}
        for entry in genome_data.split('>')[1:]:  # 跳过第一个空条目
            lines = entry.split('\n')
            header = lines[0].split()[0]  # 只获取序列ID
            sequence = ''.join(lines[1:])
            genome_sequences[header] = sequence

    # 提取和写入序列
    with open(output_path, 'w') as output_file:
        for line in blast_lines:
            parts = line.strip().split('\t')
            subject_id = parts[1]
            start = int(parts[8]) - 1  # 转换为0-based索引
            end = int(parts[9])         # 结束位置为闭区间
            if start <= end:
                extracted_sequence = genome_sequences[subject_id][start:end]  # 包括终止位置
            else:  # 如果起始位置大于终止位置，提取反向互补序列
                extracted_sequence = complement(genome_sequences[subject_id][end-1:start+1].upper())  # 包括两个端点
            output_file.write(f">{subject_id}\n{extracted_sequence}\n")

# 设置文件路径
blast_results_path = '007.txt'
genome_sequence_path = 'genome.fna'
output_path = '008.txt'

# 运行函数
extract_sequences(blast_results_path, genome_sequence_path, output_path)
