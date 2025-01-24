#import tkinter as tk
from tkinter import *
import random
from numpy import insert

root = Tk()
root.title("윈도우 프로그래밍 연습")
root.geometry("640x480")

# #기본창 띄우기
# label = Label(root, text="안녕하세요")
# label.pack(side="left")

#레이아웃 pack()방식
# label1 = Label(root, text="TOP", bg="red", fg="white")
# label1.pack(side="top", fill="x", padx=10, pady=10)

# label2 = Label(root, text="BOTTOM", bg="blue", fg="white")
# label2.pack(side="bottom", fill="x", padx=10, pady=10)

# label3 = Label(root, text="LEFT", bg="green", fg="white")
# label3.pack(side="left", fill="y", padx=10, pady=10)


# label4 = Label(root, text="RIGHT", bg="yellow", fg="black")
# label4.pack(side="right", fill="y", padx=10, pady=10)

# label5 = Label(root, text="CENTER", bg="purple", fg="white")
# label3.pack(side="top", fill="both", expand=True, padx=10, pady=10)

# 레이아웃 Grid() 방식
# label1 = Label(root, text="label1", bg="red", fg="white")
# label1.grid(row=0, column=0, padx=10, pady=10)

# label2 = Label(root, text="label2", bg="blue", fg="white")
# label2.grid(row=0, column=1, padx=10, pady=10)

# label3 = Label(root, text="label3", bg="green", fg="white")
# label3.grid(row=1, column=0, padx=10, pady=10)

# label4 = Label(root, text="label4", bg="yellow", fg="black")
# label4.grid(row=1, column=1, padx=10, pady=10)

# label5 = Label(root, text="label5", bg="purple", fg="white")
# label5.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

"""

#위젯
#Label
label = Label(root, text="Hello, tkinter!", font=("Pretendard", 20), fg="blue")
label.pack()

#버튼
def on_click():
    print("Button Click")

button = Button(root, text="클릭", command=on_click).pack()

# 글씨입력
def show_text():
    #entry
    entried = entry.get()
    label.config(text=f"입력된 문자는 : {entried}")
    entry.delete(0, END) # 엔트리에있는 문자열 삭제

    #text
    print(text.get("1.0", END))




# 입력을 위해서는 레이아웃은 메서드체인을 사용할 수 없음
# Entry 한줄 입력
entry = Entry(root, width=30)
entry.pack()

#text 여러줄 입력
text = Text(root, width=30, height=10)
text.pack()

button = Button(root, text="버튼클릭", command=show_text).pack()

label = Label(root, text="")
label.pack()


# Frame
top_frame = Frame(root, bg="'lighble")
top_frame.pack(fill="x")
label(top_frame, text="top frame").pack(pady=30)

bottom_frame = Frame(root), bg="lightgreen")
bottom_frame.pack(fill="both", expand=True)
Label(bottom_frame, text="bottom frame").pack()

#checkbutton
def show_state():
    print(f"check는 {var,get()}")

var = IntVar
checkbtn = Checkbutton(root, text="동의"), variable=var, command=show_state).pack()
# radiobutton
var = StringVar(value="option1")
radio1 = Radiobutton(
    root, text="옵션1", variable=var, value="option1", command=show_state
).pack(pady=10)
radio2 = Radiobutton(
    root, text="옵션2", variable=var, value="option2", command=show_state
).pack(pady=10)


#listbox
def show_selected():
    selection = listbox.curselection()
    print(selection)
    if selection:
        print(f"선택된 과일을 : {listbox.get(selection[0])}")

listbox = Listbox(root)
listbox.pack(pady=10)
for item in ["사과", "바나나", "포도", "체리"]
    listbox.insert(END, item)

button = Button(root, text="선택", command=show_selected")
button.pack(pady=10)


#messagebox
from tkinter import messagebox

def show_message():
    messagebox.showinfo("경고", "메시지창 띄우기 연습")

button = Button(root, text="클릭", command=show_message)
button.pack(pady=10)
root.mainloop()


#메뉴
from tkinter import messagebox

def new_file():
    messagebox.showinfo("메뉴", "파일이 선택되었습니다")

def exit_app():
    root.quit() #윈도우창 종료

menubar = Menu(root)
               
filemenu = Menu(menubar, tearoff=0) #tearoff = 0 떼어내기를 막는다.
filemenu.add_command(label="New", command=new_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_app)

menubar.add_cascade(label="파일", menu=filemenu)
root.config(menu=menubar)
root.mainloop()
"""

#쿠폰추첨기
def on_click():
    name_list = ["김민경", "이동건", "최승우", "최영", "한수빈", "김혜은", "이채연", "조경록"]

    name = random.sample(name_list, 2)
    print(name)
    text.delete("1.0", END)
    text.insert(END, name)

window = Tk()
window.title("쿠폰추첨기")
window.geometry("640x480")

#이미지 넣기
label_img = Label(window)
img = PhotoImage(file="coupon.jpg")
label_img.config(image=img)
label_img.pack()

#추첨버튼
Button(window, text="추첨", command=on_click).pack()

#추첨된사람 출력
text = Text(window, width=40, height=5, bg="green")
text.pack()

window.mainloop()

