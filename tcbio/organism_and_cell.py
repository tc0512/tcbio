import rich
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
def 生物的特征():
    CHARACTERISTIC = {1: "除病毒外，生物是由细胞构成的",
        2: "生物的生活需要营养",
        3: "生物能进行呼吸",
        4: "生物能对外界刺激做出反应",
        5: "生物能生长、发育和繁殖",
        6: "生物具有遗传和变异的特性",
        7: "生物能够排出体内产生的废物"
    }
    print(CHARACTERISTIC)
    rich.print("[green]Tip:细胞是生物结构与功能的基本单位[/green]")
def on_click1():
    messagebox.showinfo("1 目镜", "将物镜放大后的实像再次放大，形成一个放大的虚像供人眼观察")
def on_click2():
    messagebox.showinfo("2 镜筒", "连接目镜与物镜，提供稳定的光路通道，并保护成像光路")
def on_click3():
    messagebox.showinfo("3 转换器", "可以转换物镜")
def on_click4():
    messagebox.showinfo("4 物镜", "对观察的样本进行首次放大形成一个倒立放大实像")
def on_click5():
    messagebox.showinfo("5 遮光器", "调节光线强弱")
def on_click6():
    messagebox.showinfo("6 载物台", "安放需要观察的标本")
def on_click7():
    messagebox.showinfo("7 压片夹", "固定样品")
def on_click8():
    messagebox.showinfo("8 反光镜", "将外部光源的光线反射到显微镜的光学系统中，以照亮被观察的标本")
def 单目显微镜的结构():
    root = tk.Tk()
    root.title("tcbio")
    root.geometry("600x800")
    img = Image.open("t04624d8537ec5864f9.png")
    img = img.resize((600, 800), Image.Resampling.LANCZOS)
    bg = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(root, width=600, height=800)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg, anchor="nw")
    button1 = tk.Button(canvas, text="1", command=on_click1)
    canvas.create_window(50, 50, window=button1)
    button2 = tk.Button(canvas, text="2", command=on_click2)
    canvas.create_window(100, 50, window=button2)
    button3 = tk.Button(canvas, text="3", command=on_click3)
    canvas.create_window(150, 50, window=button3)
    button4 = tk.Button(canvas, text="4", command=on_click4)
    canvas.create_window(50, 100, window=button4)
    button5 = tk.Button(canvas, text="5", command=on_click5)
    canvas.create_window(100, 100, window=button5)
    button6 = tk.Button(canvas, text="6", command=on_click6)
    canvas.create_window(150, 100, window=button6)
    button7 = tk.Button(canvas, text="7", command=on_click7)
    canvas.create_window(50, 150, window=button7)
    button8 = tk.Button(canvas, text="8", command=on_click8)
    canvas.create_window(100, 150, window=button8)
    root.mainloop()
单目显微镜的结构()
