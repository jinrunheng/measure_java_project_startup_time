import matplotlib.pyplot as plt

# 给定的 list
data_list = [1, 3, 2, 4, 6, 5, 7, 9, 8]

# 创建索引
indexes = range(len(data_list))

# 绘制折线图，红色线段，带有圆点标记
plt.figure(figsize=(10, 5))
plt.plot(indexes, data_list, color='red', marker='o', linestyle='-')

# 设置标题和坐标轴标签
plt.title('List Value Plot')
plt.xlabel('Index')
plt.ylabel('Value')

# 显示图形
plt.show()
