"""
图像匹配问题。给出若干幅图像，图像的数据可以用矩阵表示。图像的数据范围是[0,255]。给出起始的图像x，在剩下任一图像中任选图像y，计算x的最后一列和y的第一列的欧氏距离。剩下图像中这种欧氏距离最小的图像是是最匹配的图像。假设最匹配图像为y0, 继续在余下的图像中寻找和y0最匹配的图像。重复这个过程，直到没有图像剩下。

现在给出p幅图像的数据，依次编号为1,2，...,p。 每幅图像的大小是m×n. 假设第一幅图像设置为编号x, 1≤x≤p. 按照前一段图像最匹配描述，计算最匹配的序列。

输入格式:
第一行输入四个整数m,n,p,x
第二行到到底m*p行，每一行有n个数据。
依次表示编号为1,2，...,p的图像数据。

输出格式:
输出最匹配序列，包括起始编号x

输入样例:
2, 2, 3, 2
33, 44
33, 44
55, 33
55, 33
44, 99
44, 99
输出样例:
2 1 3 
样例说明， 2, 2, 3, 2 表示图像大小为2×2, 共3幅图像，
起始图像编号是2。

第一幅图像数据

33, 44
33, 44

第二幅图像数据
55, 33
55, 33
第三幅图像数据
44, 99
44, 99

输出结果
2 1 3 表明起始图像x编号为2，图像2最匹配的是1，图像1最匹配的是3。
"""

import numpy as np
import sys


def distance(x, y):
    return np.sqrt(np.sum(np.square(x[:, -1] - y[:, 0])))


# 遍历所有图像，返回匹配序列
def scan_all(begin, arr):
    scanned_dic = {}
    for i in range(p):
        for j in range(p):
            if j == i or (i + 1, j + 1) in scanned_dic:
                pass
            else:
                scanned_dic[(i + 1, j + 1)] = distance(arr[i], arr[j])  # arr下标从0开始,而我们的图像编号从1开始
    # print(scanned_dic)
    result = {}
    for key, value in scanned_dic.items():  # 找到每个a所对应的最小值和对应的b
        a, b = key
        if a in result:
            if value < result[a][1]:  # 如果a已经在result中，且当前所遍历到的value小于result[a]即对应的(b,value)中的value
                result[a] = (b, value)
        else:
            result[a] = (b, value)  # 形成字典，a: (b, value),其中a为键,(b, value)为值
    final_result = [begin]  # 最终的匹配序列,begin = x,即第一张图
    for i in range(p - 1):
        x = final_result[-1]  # 获得最后一张图的编号, 即a, 即result中的键,再在result中找到对应的b, 也就是匹配的下一张图的序号
        y = result[x][0]  # result[x][0]即为对应的b(x为键, (b, value)为值), result[x][0]即为b
        final_result.append(y)
    return final_result


# 读入数据
lst = []
lst_new = []
for line in sys.stdin:
    # py.3中input（）只能输入一行  sys.stdin按下换行键然后ctrl+d程序结束
    lst_new = line.split()
    lst.extend(lst_new)  # 每一行组成的列表合并

# 转换数据格式
lst = [int(i.replace(',', '')) for i in lst]
m, n, p, x = lst[:4]
arr = np.array(lst[4:]).reshape(p, m, n)

# 计算匹配序列并输出
res = scan_all(x, arr)
print(' '.join(map(str, res)), end=' ')