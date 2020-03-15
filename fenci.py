import jieba
import os

# 待分词的文本路径
sourceTxt = 'txt'
# 分好词后的文本路径
targetTxt = 'output'

files = os.listdir(sourceTxt)

# 对文本进行操作
for file in files:
    with open(sourceTxt+os.sep+file, 'r', encoding = 'utf-8') as File, open(targetTxt+os.sep+file, 'a+', encoding = 'utf-8') as targetFile:
        for line in File:
            seg = jieba.cut(line.strip(), cut_all = False)
            # 分好词之后之间用空格隔断
            output = ' '.join(seg)
            targetFile.write(output)
            targetFile.write('\n')
        print('写入成功！')
