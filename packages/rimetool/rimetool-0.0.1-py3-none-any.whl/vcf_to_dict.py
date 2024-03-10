from pypinyin import lazy_pinyin
import argparse

def main():
    `# 读取文件
    parser = argparse.ArgumentParser(description='Process a .vcf file.') # 创建一个解析器
    parser.add_argument('file', help='The .vcf file to process') # 添加一个命令行参数
    args = parser.parse_args()# 解析命令行参数


    # 从vcf文件中提取联系人姓名
    with open(args.file, 'r') as infile, open('contacts_extracted.txt', 'w') as outfile:
        # 遍历输入文件的每一行
        for line in infile:
            # 检查行是否以'FN:'开头
            if line.startswith('FN:'):
                # 获取'FN:'后面的内容
                content = line[3:]
                # 将内容写入输出文件
                outfile.write(content)


    # 去掉联系人姓名中的空格
    with open('contacts_output.txt', 'r') as infile, open('contacts_without_blank.txt', 'w') as outfile:
        # 遍历输入文件的每一行
        for line in infile:
            # 删除行尾的换行符
            line = line.rstrip('\n')
            # 分割行中的单词
            words = line.rsplit(' ', 1)
            # 如果行中有空格
            if len(words) > 1:
                # 将倒数第一个空格后面的内容移动到最前面，并删除这个空格
                new_line = words[1] + words[0] + '\n'
                # 将新的行写入输出文件
                outfile.write(new_line)
            else:
                # 如果行中没有空格，直接将行写入输出文件
                outfile.write(line + '\n')

    # 转化为rime词典格式
    with open('contacts_without_blank.txt', 'r') as infile, open('mycontacts.dict.yaml', 'w') as outfile:
        # 遍历输入文件的每一行
        for line in infile:
            # 删除行尾的换行符
            line = line.rstrip('\n')
            # 获取行的拼音
            pinyin = ''.join(lazy_pinyin(line))
            # 在行的内容后面加一个tab，然后加上它的拼音，再加一个tab，然后加上数字1
            new_line = line + '\t' + pinyin + '\t1\n'
            # 将新的行写入输出文件
            outfile.write(new_line)

if __name__ == "__main__":
    main()