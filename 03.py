from collections import defaultdict
from Bio import SeqIO

def complement(sequence):
    """返回DNA序列的反向互补序列。"""
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N', 'a': 't', 't': 'a', 'c': 'g', 'g': 'c', 'n': 'n'}
    return ''.join(complement_dict[base] for base in sequence[::-1])

def read_blast_results(blast_results_path):
    """从BLAST结果文件读取并返回序列的起始、结束位点及对应的序列ID。"""
    positions = []
    with open(blast_results_path, 'r') as blast_file:
        for line in blast_file:
            parts = line.strip().split('\t')
            seq_id, start, end = parts[1], int(parts[8]), int(parts[9])
            pos = int(parts[-6])  # 假设倒数第六列为起始位置
            positions.append((seq_id, start, end, pos))
    return positions

def concatenate_sequences(positions, genome_sequence_path, output_path):
    # 读取基因组序列文件
    genome_sequences = SeqIO.to_dict(SeqIO.parse(genome_sequence_path, "fasta"))
    
    # 初始化用于存储每行拼接序列的字典
    concatenated_sequences = defaultdict(str)
    # 记录处理过的位置，以处理重叠和重复
    processed_positions = set()
    
    # 按照位置排序并处理序列
    for seq_id, start, end, pos in sorted(positions, key=lambda x: x[3]):
        seq_record = genome_sequences.get(seq_id)
        if seq_record:
            seq = seq_record.seq[min(start, end)-1:max(start, end)]  # 提取序列片段
            if start > end:
                seq = complement(seq)  # 获取反向互补序列
            # 处理重叠和重复的逻辑，简化为只处理重复的情况
            if pos in processed_positions:
                # 查找一个未使用的行
                line = 1
                while line in concatenated_sequences and pos in processed_positions:
                    line += 1
                concatenated_sequences[line] += seq
            else:
                concatenated_sequences[0] += seq
            processed_positions.add(pos)
        else:
            print(f"Warning: Sequence ID {seq_id} not found in genome sequence file.")
    
    # 写入结果
    with open(output_path, 'w') as file:
        for line in sorted(concatenated_sequences):
            file.write(f">Concatenated_Sequence_{line}\n{concatenated_sequences[line]}\n")

# 设置文件路径
blast_results_path = '007.txt'
genome_sequence_path = 'genome.fna'
output_path = '009.txt'

# 获取位点信息
positions = read_blast_results(blast_results_path)
# 执行拼接
concatenate_sequences(positions, genome_sequence_path, output_path)
