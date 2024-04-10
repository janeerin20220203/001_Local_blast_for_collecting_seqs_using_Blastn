# 读取blast_results.txt文件的内容并按照倒数第六列的数字进行排序
with open('blast_results.txt', 'r') as input_file:
    lines = input_file.readlines()

# 排序函数，根据倒数第六列的数字进行排序
def sort_key(line):
    columns = line.split('\t')
    return float(columns[-6])

# 按照排序函数对内容进行排序
lines.sort(key=sort_key)

# 将排序后的内容写入007.txt文件
with open('007.txt', 'w') as output_file:
    for line in lines:
        output_file.write(line)

print("排序完成并将结果写入007.txt文件。")
