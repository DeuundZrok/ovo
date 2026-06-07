import cv2
from tkinter import filedialog
import tkinter as tk

# 创建一个隐藏的窗口（免得弹出两个窗口）
root = tk.Tk()
root.withdraw()

# 弹出文件选择框，让你手动选图片
file_path = filedialog.askopenfilenames(
    title="选择一张图片",
    filetypes=[("图片文件", "*.jpg *.jpeg *.png *.bmp")],
    multiple=True
)

if file_path:
    for i,path in enumerate(file_path):
        img = cv2.imread(path)  # 读取每张图片
        oo = f"图片{i+1}: {path.split('/')[-1]}"
        cv2.imshow(oo, img)      
    cv2.waitKey(0)                  
    cv2.destroyAllWindows()
else:
    print("你没有选任何文件")