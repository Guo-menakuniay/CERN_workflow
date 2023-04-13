import uproot
import os
import matplotlib.pyplot as plt

# 定义ROOT文件所在的文件夹
folder = "Rootdata"

# 获取文件夹内所有ROOT文件
root_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".root")]

# 设置画布和子图
fig, ax = plt.subplots()

# 遍历所有ROOT文件
for root_file in root_files:
    try:
        with uproot.open(root_file) as f:
            # 获取nEvents直方图
            hist = f["nEvents"]

            # 提取bin内容和边缘
            bin_contents, bin_edges = hist.to_numpy()

            # 绘制直方图
            ax.step(bin_edges[:-1], bin_contents, where="post", label=root_file)
    except Exception as e:
        print(f"Error processing {root_file}: {e}")

# 设置图例和轴标签
ax.legend()
ax.set_xlabel("Bin")
ax.set_ylabel("nEvents")

# 保存并显示图像
plt.savefig("nEvents_histograms.png")
plt.show()

