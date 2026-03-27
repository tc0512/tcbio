import rich
import tkinter as tk
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
def 单目显微镜的结构():
