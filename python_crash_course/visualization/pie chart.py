import matplotlib.pyplot as plt

# 设置每个充分因果饼图的数据
labels = ['APOE-ε4', 'Advanced Age', 'Chronic Inflammation', 'Brain Injury', 'Smoking',
          'Hypertension', 'Diabetes', 'Environmental Exposure', 'Cognitive Inactivity', 'Sedentary Lifestyle',
          'Depression', 'Social Isolation', 'Sleep Disorders']

# 定义每个饼图的组成部分比例
sizes_1 = [15, 10, 8, 8]  # 第一个饼图：遗传因素、高龄、慢性炎症、脑外伤
sizes_2 = [15, 6, 6, 6]  # 第二个饼图：遗传因素、吸烟、高血压、糖尿病
sizes_3 = [15, 5, 5, 5]  # 第三个饼图：遗传因素、环境暴露、认知缺乏、久坐
sizes_4 = [15, 5, 5, 5]  # 第四个饼图：遗传因素、抑郁、社会隔离、睡眠障碍

# 设置颜色
colors = ['#e89da0', '#88cee6', '#f6c8a8', '#b2d3a4']

# 创建子图
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# 第一个充分因果饼图
axs[0, 0].pie(sizes_1, labels=labels[:4], colors=colors, startangle=140)
axs[0, 0].set_title('Causal Pie Chart 1')

# 第二个充分因果饼图
axs[0, 1].pie(sizes_2, labels=labels[:4], colors=colors, startangle=140)
axs[0, 1].set_title('Causal Pie Chart 2')

# 第三个充分因果饼图
axs[1, 0].pie(sizes_3, labels=labels[:4], colors=colors, startangle=140)
axs[1, 0].set_title('Causal Pie Chart 3')

# 第四个充分因果饼图
axs[1, 1].pie(sizes_4, labels=labels[:4], colors=colors, startangle=140)
axs[1, 1].set_title('Causal Pie Chart 4')

# 添加整体标题
fig.suptitle("Causal Pie Chart - Alzheimer's Disease", fontsize=16)
# 确保饼图是圆形的
plt.tight_layout(rect=(0, 0, 1, 0.95))  # 调整子图以防止标题与图表重叠
plt.show()
