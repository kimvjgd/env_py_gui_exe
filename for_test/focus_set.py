from tkinter import *
from tkinter.ttk import *
# master =Tk()
# e1 = Entry(master)
# e1.pack(expand=1, fill=BOTH)
# e1.focus_set()

root = Tk()
root.title('Dongpakka')
root.geometry("800x480")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(0, '한 줄만 입력하세요')

def btncmd():
    print(txt.get("1.0", END))          # 첫번째 라인, 0 : 0번쨰 column 위치

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()

