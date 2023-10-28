from operator import truediv
from tkinter import *
import numpy as np
import math
import tkinter.messagebox
import random
root = Tk()         
root.title("软件2102 20216854董兆辉")
f1=Frame(root)
f1.pack()
w1 = Canvas(f1, width=580,height=580,background='lightcyan')
w1.pack()


for i in range(0, 4):
    w1.create_line(i * 180 + 20, 20, i * 180 + 20, 560)
    w1.create_line(20, i * 180 + 20, 560, i * 180 + 20)
num = 0
A = np.full((3, 3), 0)


def dawn(event):#找的代码,这一行貌似是鼠标点击才能触发的函数
    global w1
    global num, A
    #找的代码,应该是创建棋盘
    for i in range(0, 3):
        for j in range(0, 3):
            if 20 + j * 180 < event.y and event.y <= 20 + (j+1) * 180:
                break
        if 20 + i * 180 <= event.x and event.x <= 20 + (i+1) * 180:
            break

    #找的代码,应该是先手人方开始下 人X 机O 因为是createline函数嘛 有个line
    if A[i][j] == 0:
        A[i][j] = 1
        w1.create_line(110 + 180 * i - 45 * math.sqrt(2),     110 + 180 * j - 45 * math.sqrt(2),
                       110 + 180 * i + 45 * math.sqrt(2),     110 + 180 * j + 45 * math.sqrt(2))
        w1.create_line(110 + 180 * i + 45 * math.sqrt(2),     110 + 180 * j - 45 * math.sqrt(2),
                       110 + 180 * i - 45 * math.sqrt(2),     110 + 180 * j + 45 * math.sqrt(2))
    else:
        return
    
    #自己写的,底层逻辑是机器寻找能直接把人干掉的位置下子,9个格子二重循环遍历,如果格子为空,就先把子下在这,赢不了就换,直到赢了为止
    #赢不了就守,如果下一步人找到位置下子直接赢的话,机器会在那个地方提前下子阻止人获胜
    #上面两个都不行,就随便下吧,二重循环遍历二维数组,有空位置就下
    judge = 0
    advancejudge = 0
    for i in range(3):
        for j in range(3):
            if  A[i][j]==0: 
                A[i][j]=2
                if A[0][0] == A[0][1] == A[0][2] == 2 or A[1][0] == A[1][1] == A[1][2] == 2 or A[2][0] == A[2][1] == A[2][
        2] == 2 or \
            A[0][0] == A[1][0] == A[2][0] == 2 or A[0][1] == A[1][1] == A[2][1] == 2 or A[0][2] == A[1][2] == \
            A[2][
                2] == 2 or \
            A[0][0] == A[1][1] == A[2][2] == 2 or A[2][0] == A[1][1] == A[0][2] == 2:
                    advancejudge=1
                    w1.create_oval(20 + 180 * i, 20 + 180 *j, 20 + 180 * (i + 1), 20 + 180 * (j+1))
                    break
                else:
                    A[i][j]=0
                    continue             
        if advancejudge==1:
            break
    protect=0
    if advancejudge==0:
        for i in range(3):
            for j in range(3):  
                if  A[i][j]==0:
                    A[i][j]=1
                    if A[0][0] == A[0][1] == A[0][2] == 1 or A[1][0] == A[1][1] == A[1][2] == 1 or A[2][0] == A[2][1] == A[2][
            2] == 1 or \
                A[0][0] == A[1][0] == A[2][0] == 1 or A[0][1] == A[1][1] == A[2][1] == 1 or A[0][2] == A[1][2] == \
                A[2][
                    2] == 1 or \
                A[0][0] == A[1][1] == A[2][2] == 1 or A[2][0] == A[1][1] == A[0][2] == 1:
                        A[i][j]=2
                        protect=1
                        w1.create_oval(20 + 180 * i, 20 + 180 *j, 20 + 180 * (i + 1), 20 + 180 * (j+1))
                        break
                    else:
                        A[i][j]=0
                        continue
            if protect==1:
                break


    if protect==0 and advancejudge==0:
        for i in range(3):
            for j in range(3):
                if A[i][j]==0:
                    w1.create_oval(20 + 180 * i, 20 + 180 *j, 20 + 180 * (i + 1), 20 + 180 * (j+ 1))
                    judge=1
                    A[i][j]=2
                    break
            if judge==1:
                break
            


    



                #找的代码,应该是判断获胜
    if A[0][0] == A[0][1] == A[0][2] == 1 or A[1][0] == A[1][1] == A[1][2] == 1 or A[2][0] == A[2][1] == A[2][
        2] == 1 or \
            A[0][0] == A[1][0] == A[2][0] == 1 or A[0][1] == A[1][1] == A[2][1] == 1 or A[0][2] == A[1][2] == \
            A[2][
                2] == 1 or \
            A[0][0] == A[1][1] == A[2][2] == 1 or A[2][0] == A[1][1] == A[0][2] == 1:
        tkinter.messagebox.showinfo('提示','你成功了')
    elif A[0][0] == A[0][1] == A[0][2] == 2 or A[1][0] == A[1][1] == A[1][2] == 2 or A[2][0] == A[2][1] == A[2][
        2] == 2 or \
            A[0][0] == A[1][0] == A[2][0] == 2 or A[0][1] == A[1][1] == A[2][1] == 2 or A[0][2] == A[1][2] == \
            A[2][
                2] == 2 or \
            A[0][0] == A[1][1] == A[2][2] == 2 or A[2][0] == A[1][1] == A[0][2] == 2:
        tkinter.messagebox.showinfo('提示','你失败了')
    elif A[0][0]!=0 and A[0][1]!=0 and A[0][2]!=0 and A[1][0]!=0 and A[1][1]!=0 and A[1][2]!=0 and A[2][0]!=0 and A[2][1]!=0 and A[2][2]!=0 :
        tkinter.messagebox.showinfo('提示','平局')
    #上面那个elif显示平局是我加的,棋盘九个格子全都有子,但是谁也没赢不就平局了吗


w1.bind("<Button -1>", dawn)
w1.bind("<Button -1>", dawn)
def quit():
    root.quit()
#自己写的,底层逻辑是重建棋盘,把二维数组的值全置为0
def again():
    for i in range(0, 3):
        for j in range(0, 3):
            A[i][j]=0
    w1.delete("all")
    for i in range(0, 4):
        w1.create_line(i * 180 + 20, 20, i * 180 + 20, 560)
        w1.create_line(20, i * 180 + 20, 560, i * 180 + 20)


button1 = Button(root, text="退出", font=('楷体', 20), command=quit)
button1.pack()
button2 = Button(root, text="重开", font=('楷体', 20), command=again)
button2.pack()
root.mainloop()

