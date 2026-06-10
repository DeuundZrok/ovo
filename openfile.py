import tkinter as tk
from tkinter import filedialog

def select_file():
    """打开文件选择对话框，返回所选文件路径"""
    # 隐藏主窗口
    root = tk.Tk()
    root.withdraw()
    
    # 打开文件选择对话框
    file_path = filedialog.askopenfilename(
        title="请选择一个文件",
        filetypes=[
            ("所有文件", "*.*"),
            ("文本文件", "*.txt"),
            ("图片文件", "*.jpg;*.png;*.bmp"),
            ("PDF文件", "*.pdf"),
        ]
    )
    
    if file_path:
        print(f"你选择的文件是：{file_path}")
    else:
        print("没有选择任何文件")
    
    return file_path

if __name__ == "__main__":
    selected = select_file()