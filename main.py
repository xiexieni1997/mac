import tkinter as tk
from tkinter import messagebox

# 创建主窗口
root = tk.Tk()
root.withdraw()

# 弹出消息框
messagebox.showinfo(title='提示', message='欢迎使用弹窗小应用！')

# 关闭主窗口
root.destroy()