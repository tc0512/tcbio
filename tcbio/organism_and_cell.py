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
def on_click9():
    messagebox.showinfo("9 粗准焦螺旋", "快速、大幅度地升降镜筒，从而在观察时迅速找到物像的大致位置")
def on_click10():
    messagebox.showinfo("10 细准焦螺旋", "让物像更清晰，小范围移动镜筒")
def on_click11():
    messagebox.showinfo("11 底座", "支持和稳定镜身")
def 单目显微镜的结构():
    root = tk.Tk()
    root.title("tcbio")
    root.geometry("600x800")
    img = Image.open("单目显微镜.png")
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
    button9 = tk.Button(canvas, text="9", command=on_click9)
    canvas.create_window(150, 150, window=button9)
    button10 = tk.Button(canvas, text="10", command=on_click10)
    canvas.create_window(50, 200, window=button10)
    button11 = tk.Button(canvas, text="11", command=on_click11)
    canvas.create_window(110, 200, window=button11)
    rich.print("[green]·显微镜的放大倍数是目镜放大倍数与物镜放大倍数的乘积[/green]")
    rich.print("[green]·转换物镜应转动转换器[/green]")
    rich.print("[green]·换用高倍镜后，视野亮度会变小，可选用大光圈，凹面镜[/green]")
    rich.print("[green]·物像不清晰调节细准焦螺旋[/green]")
    rich.print("[green]·目镜越短，放大倍数越大，物镜反之[/green]")
    rich.print("[green]·放大倍数越大，观察到的细胞数量越少，视野越暗[/green]")
    rich.print("[green]·光线充足或低倍镜用平面镜，光线弱或高倍镜用凹面镜[/green]")
    root.mainloop()
def 单目显微镜的使用():
    rich.print("[bold green]1.对光调光（三转）[/bold green]")
    rich.print("[green]·转转换器[/green]")
    rich.print("[green]·转遮光器[/green]")
    rich.print("[green]·转反光镜，看到圆形的明亮视野即为成功[/green]")
    rich.print("[bold green]2.调焦观察（一放三转）[/bold green]")
    rich.print("[green]·放玻片标本[/green]")
    rich.print("[green]·转粗准焦螺旋，使镜筒下降*[/green]")
    rich.print("[red]*眼睛要从侧面看着物镜，目的是避免标本被物镜压碎[/red]")
    rich.print("[green]·转粗准焦螺旋，使镜筒上升[/green]")
    rich.print("[green]·转细准焦螺旋，使物像更加清晰[/green]")
def 双目显微镜的使用():
    root = tk.Tk()
    root.title("tcbio")
    root.geometry("700x600")
    img = Image.open("双目显微镜.jpg")
    img = img.resize((700, 600))
    photo = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(root, width=700, height=600)
    canvas.pack()
    canvas.create_image(0, 0, image=photo, anchor="nw")
    rich.print("[green]·双目显微镜用底光源代替反光镜，两个目镜间距离可以调节[/green]")
    rich.print("[green]·放玻片标本后调整移动手轮，使标本移至通光孔中心，转粗准焦螺旋，使载物台上升，眼睛从侧面看着物镜，再转粗准焦螺旋，使载物台下降，直到看清物像，转细准焦螺旋，使物像清晰[/green]")
    root.mainloop()
双目显微镜的使用()
