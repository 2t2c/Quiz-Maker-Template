from tkinter import *
import tkinter.font as font
from PIL import ImageTk,Image


root = Tk()
# add your own image directory for app icon

#root.iconbitmap("C:/Users/YourName/PycharmProjects/Project/Epic Psych Quiz/meow.ico")
#img = Image.open("C:/Users/YourName/PycharmProjects/Project/Epic Psych Quiz/cat.jpg")
#img.thumbnail((300,300),Image.ANTIALIAS)
#img = ImageTk.PhotoImage(img)

root.configure(background='white')
root.state('zoom')
#root.iconify()
root.title("Epic Psych Quiz")

#change your fonts accordingly
font1 = font.Font(family="Bebas Neue",size = 70)
font2 = font.Font(family="Bebas Neue",size = 40)
font3 = font.Font(family="Bison Bold",size = 30)
font4 = font.Font(family="Bebas Kai",size = 20)
font5 = font.Font(family="LibelSuitRg-Regular",size = 18)
font6 = font.Font(family="LibelSuitRg-Regular",size = 25)


#root.geometry("600x600")

label1 = Label(root,text = "WELCOME TO THE QUIZ MAKER",anchor = CENTER,bg = "white")
label1["font"] = font1
label1.pack()

label2 = Label(root,text = "Rules To Be Followed",anchor = W,justify = LEFT,bg = "white")
label2["font"] = font2
label2.pack(pady=75)

label3 = Label(root,text = '''
• Rule 1
• Rule 2
• Rule 3
• Rule 4
• Rule 5
• Rule 6
• Rule 7
• Rule 8
• Rule 9
• Rule 10
''',justify = LEFT,anchor = CENTER,bg = "white")
label3["font"] = font3
label3.pack()

def ques1():
    label1.pack_forget()
    label2.pack_forget()
    label3.pack_forget()
    button_next.destroy()

    global frame1
    frame1 = LabelFrame(root, text = "Question 1",padx=250,pady=230,bg = "white")
    frame1["font"] = font4
    frame1.pack(pady=80)

    global label4
    label4 = Label(frame1, text="Question 1 ?",bg="white",anchor=CENTER)
    label4["font"] = font6
    label4.pack(pady=10)

    r = IntVar()
    rb1 = Radiobutton(frame1, text = "Option 1", variable = r, value = 1,bg = "white", command = lambda: ans1(r.get()))
    rb2 = Radiobutton(frame1, text = "Option 2", variable = r, value = 2,bg = "white",command = lambda: ans1(r.get()))
    rb3 = Radiobutton(frame1, text = "Option 3", variable = r, value = 3,bg = "white",command = lambda: ans1(r.get()))
    rb4 = Radiobutton(frame1, text = "Option 4", variable = r, value = 4,bg = "white",command = lambda : ans1(r.get()))

    rb1.pack(anchor = W)
    rb2.pack(anchor = W)
    rb3.pack(anchor = W)
    rb4.pack(anchor = W)
    rb1["font"] = font5
    rb2["font"] = font5
    rb3["font"] = font5
    rb4["font"] = font5

    global button_next1
    button_next1 = Button(frame1, text="Next", bg="white", padx=15,pady=0, state = DISABLED)
    button_next1['font'] = font4
    button_next1.pack(pady=15)
    button_next1.configure(command = lambda : ques2())

#change the "value" according to your correct answer

def ans1(value):
    if value == 3:
        global score1,flag1
        flag1 = 1
        score1 = 1
        return button_next1.configure(state = NORMAL)
    else:
        global flag2
        flag2 = 1
        score1 = 0
        return button_next1.configure(state=NORMAL)


def ques2():
    frame1.pack_forget()
    button_next1.destroy()
    label4.pack_forget()

    global frame2
    frame2 = LabelFrame(root, text = "Question 2",padx=250,pady=230,bg = "white")
    frame2["font"] = font4
    frame2.pack(pady=80)

    global label5
    label5 = Label(frame2, text="Question 2 ?",bg="white",anchor=CENTER)
    label5["font"] = font6
    label5.pack(pady=10)

    r = IntVar()
    rb1 = Radiobutton(frame2, text = "Option 1", variable = r, value = 1,bg = "white", command = lambda: ans2(r.get()))
    rb2 = Radiobutton(frame2, text = "Option 2 ", variable = r, value = 2,bg = "white",command = lambda: ans2(r.get()))
    rb3 = Radiobutton(frame2, text = "Option 3", variable = r, value = 3,bg = "white",command = lambda: ans2(r.get()))
    rb4 = Radiobutton(frame2, text = "Option 4", variable = r, value = 4,bg = "white",command = lambda : ans2(r.get()))

    rb1.pack(anchor = W)
    rb2.pack(anchor = W)
    rb3.pack(anchor = W)
    rb4.pack(anchor = W)
    rb1["font"] = font5
    rb2["font"] = font5
    rb3["font"] = font5
    rb4["font"] = font5

    global button_next2
    button_next2 = Button(frame2, text="Next", bg="white", padx=15,pady=0, state = DISABLED)
    button_next2['font'] = font4
    button_next2.pack(pady=15)
    button_next2.configure(command = lambda : ques3())

def ans2(value):

    if value == 2:
        global score2
        score2 = 1
        return button_next2.configure(state = NORMAL)
    else:
        score2 = 0
        return button_next2.configure(state = NORMAL)

def ques3():
    frame2.pack_forget()
    button_next2.destroy()
    label5.pack_forget()

    global frame3
    frame3 = LabelFrame(root, text = "Question 3",padx=250,pady=230,bg = "white")
    frame3["font"] = font4
    frame3.pack(pady=80)

    global label6
    label6 = Label(frame3, text="Question 3 ?",bg="white",anchor=CENTER)
    label6["font"] = font6
    label6.pack(pady=10)

    r = IntVar()
    rb1 = Radiobutton(frame3, text = "Option 1", variable = r, value = 1,bg = "white", command = lambda: ans3(r.get()))
    rb2 = Radiobutton(frame3, text = "Option 2", variable = r, value = 2,bg = "white",command = lambda: ans3(r.get()))
    rb3 = Radiobutton(frame3, text = "Option 3", variable = r, value = 3,bg = "white",command = lambda: ans3(r.get()))
    rb4 = Radiobutton(frame3, text = "Option 4", variable = r, value = 4,bg = "white",command = lambda : ans3(r.get()))

    rb1.pack(anchor = W)
    rb2.pack(anchor = W)
    rb3.pack(anchor = W)
    rb4.pack(anchor = W)
    rb1["font"] = font5
    rb2["font"] = font5
    rb3["font"] = font5
    rb4["font"] = font5

    global button_next3
    button_next3 = Button(frame3, text="Next", bg="white", padx=15,pady=0, state = DISABLED)
    button_next3['font'] = font4
    button_next3.pack(pady=15)
    button_next3.configure(command = lambda : ques4())

def ans3(value):

    if value == 1:
        global score3
        score3 = 1
        return button_next3.configure(state = NORMAL)
    else:
        score3 = 0
        return button_next3.configure(state = NORMAL)

def ques4():
    frame3.pack_forget()
    button_next3.destroy()
    label6.pack_forget()

    global frame4
    frame4 = LabelFrame(root, text = "Question 4",padx=250,pady=230,bg = "white")
    frame4["font"] = font4
    frame4.pack(pady=80)

    global label7
    label7 = Label(frame4, text="Question 4 ?",bg="white",anchor=CENTER)
    label7["font"] = font6
    label7.pack(pady=10)

    r = IntVar()
    rb1 = Radiobutton(frame4, text = "Option 1", variable = r, value = 1,bg = "white", command = lambda: ans4(r.get()))
    rb2 = Radiobutton(frame4, text = "Option 2", variable = r, value = 2,bg = "white",command = lambda: ans4(r.get()))
    rb3 = Radiobutton(frame4, text = "Option 3", variable = r, value = 3,bg = "white",command = lambda: ans4(r.get()))
    rb4 = Radiobutton(frame4, text = "Option 4", variable = r, value = 4,bg = "white",command = lambda : ans4(r.get()))

    rb1.pack(anchor = W)
    rb2.pack(anchor = W)
    rb3.pack(anchor = W)
    rb4.pack(anchor = W)
    rb1["font"] = font5
    rb2["font"] = font5
    rb3["font"] = font5
    rb4["font"] = font5

    global button_next4
    button_next4 = Button(frame4, text="Next", bg="white", padx=15,pady=0, state = DISABLED)
    button_next4['font'] = font4
    button_next4.pack(pady=15)
    button_next4.configure(command = lambda : ques5())

def ans4(value):

    if value == 3:
        global score4
        score4 = 1
        return button_next4.configure(state = NORMAL)
    else:
        score4 = 0
        return button_next4.configure(state = NORMAL)

def ques5():
    frame4.pack_forget()
    button_next4.destroy()
    label7.pack_forget()

    global frame5
    frame5 = LabelFrame(root, text = "Question 5",padx=250,pady=230,bg = "white")
    frame5["font"] = font4
    frame5.pack(pady=80)

    global label8
    label8 = Label(frame5, text="Question 5 ?",bg="white",anchor=CENTER)
    label8["font"] = font6
    label8.pack(pady=10)

    r = IntVar()
    rb1 = Radiobutton(frame5, text = "Option 1", variable = r, value = 1,bg = "white", command = lambda: ans5(r.get()))
    rb2 = Radiobutton(frame5, text = "Option 2", variable = r, value = 2,bg = "white",command = lambda: ans5(r.get()))
    rb3 = Radiobutton(frame5, text = "Option 3", variable = r, value = 3,bg = "white",command = lambda: ans5(r.get()))
    rb4 = Radiobutton(frame5, text = "Option 4", variable = r, value = 4,bg = "white",command = lambda : ans5(r.get()))

    rb1.pack(anchor = W)
    rb2.pack(anchor = W)
    rb3.pack(anchor = W)
    rb4.pack(anchor = W)
    rb1["font"] = font5
    rb2["font"] = font5
    rb3["font"] = font5
    rb4["font"] = font5

    global button_next5
    button_next5 = Button(frame5, text="Next", bg="white", padx=15,pady=0, state = DISABLED)
    button_next5['font'] = font4
    button_next5.pack(pady=15)
    button_next5.configure(command = lambda : ques6())

def ans5(value):

    if value == 4:
        global score5
        score5 = 1
        return button_next5.configure(state = NORMAL)
    else:
        score5 = 0
        return button_next5.configure(state = NORMAL)

def ques6():
    frame5.pack_forget()
    button_next5.destroy()
    label8.pack_forget()

    global frame6
    frame6 = LabelFrame(root, text = "Question 6",padx=250,pady=230,bg = "white")
    frame6["font"] = font4
    frame6.pack(pady=80)

    global label9
    label9 = Label(frame6, text="Question 6 ?",bg="white",anchor=CENTER)
    label9["font"] = font6
    label9.pack(pady=10)

    r = IntVar()
    rb1 = Radiobutton(frame6, text = "Option 1", variable = r, value = 1,bg = "white", command = lambda: ans6(r.get()))
    rb2 = Radiobutton(frame6, text = "Option 2", variable = r, value = 2,bg = "white",command = lambda: ans6(r.get()))
    rb3 = Radiobutton(frame6, text = "Option 3", variable = r, value = 3,bg = "white",command = lambda: ans6(r.get()))
    rb4 = Radiobutton(frame6, text = "Option 4", variable = r, value = 4,bg = "white",command = lambda : ans6(r.get()))

    rb1.pack(anchor = W)
    rb2.pack(anchor = W)
    rb3.pack(anchor = W)
    rb4.pack(anchor = W)
    rb1["font"] = font5
    rb2["font"] = font5
    rb3["font"] = font5
    rb4["font"] = font5

    global button_next6
    button_next6 = Button(frame6, text="Next", bg="white", padx=15,pady=0, state = DISABLED)
    button_next6['font'] = font4
    button_next6.pack(pady=15)
    button_next6.configure(command = lambda : ques7())

def ans6(value):

    if value == 2:
        global score6
        score6 = 1
        return button_next6.configure(state=NORMAL)
    else:
       score6 = 0
       return button_next6.configure(state=NORMAL)

def ques7():
    frame6.pack_forget()
    button_next6.destroy()
    label9.pack_forget()

    global frame7
    frame7 = LabelFrame(root, text = "Question 7",padx=250,pady=230,bg = "white")
    frame7["font"] = font4
    frame7.pack(pady=80)

    global label10
    label10 = Label(frame7, text="Question 7 ?",bg="white",anchor=CENTER)
    label10["font"] = font6
    label10.pack(pady=10)

    r = IntVar()
    rb1 = Radiobutton(frame7, text = "Option 1", variable = r, value = 1,bg = "white", command = lambda: ans7(r.get()))
    rb2 = Radiobutton(frame7, text = "Option 2", variable = r, value = 2,bg = "white",command = lambda: ans7(r.get()))
    rb3 = Radiobutton(frame7, text = "Option 3", variable = r, value = 3,bg = "white",command = lambda: ans7(r.get()))
    rb4 = Radiobutton(frame7, text = "Option 4", variable = r, value = 4,bg = "white",command = lambda : ans7(r.get()))

    rb1.pack(anchor = W)
    rb2.pack(anchor = W)
    rb3.pack(anchor = W)
    rb4.pack(anchor = W)
    rb1["font"] = font5
    rb2["font"] = font5
    rb3["font"] = font5
    rb4["font"] = font5

    global button_next7
    button_next7 = Button(frame7, text="Next", bg="white", padx=15,pady=0, state = DISABLED )
    button_next7['font'] = font4
    button_next7.pack(pady=15)
    button_next7.configure(command = lambda : ques8())

def ans7(value):

    if value == 4:
        global score7
        score7 = 1
        return button_next7.configure(state=NORMAL)
    else:
        score7 = 0
        return button_next7.configure(state=NORMAL)

def ques8():
    frame7.pack_forget()
    button_next7.destroy()
    label10.pack_forget()

    global frame8
    frame8 = LabelFrame(root, text = "Question 8",padx=250,pady=230,bg = "white")
    frame8["font"] = font4
    frame8.pack(pady=80)

    global label11
    label11 = Label(frame8, text="Question 8 ?",bg="white",anchor=CENTER)
    label11["font"] = font6
    label11.pack(pady=10)

    r = IntVar()
    rb1 = Radiobutton(frame8, text = "Option 1", variable = r, value = 1,bg = "white", command = lambda: ans8(r.get()))
    rb2 = Radiobutton(frame8, text = "Option 2", variable = r, value = 2,bg = "white",command = lambda: ans8(r.get()))
    rb3 = Radiobutton(frame8, text = "Option 3", variable = r, value = 3,bg = "white",command = lambda: ans8(r.get()))
    rb4 = Radiobutton(frame8, text = "Option 4", variable = r, value = 4,bg = "white",command = lambda : ans8(r.get()))

    rb1.pack(anchor = W)
    rb2.pack(anchor = W)
    rb3.pack(anchor = W)
    rb4.pack(anchor = W)
    rb1["font"] = font5
    rb2["font"] = font5
    rb3["font"] = font5
    rb4["font"] = font5

    global button_next8
    button_next8 = Button(frame8, text="Next", bg="white", padx=15,pady=0, state = DISABLED)
    button_next8['font'] = font4
    button_next8.pack(pady=15)
    button_next8.configure(command = lambda : ques9())

def ans8(value):

    if value == 3:
        global score8
        score8 = 1
        return button_next8.configure(state=NORMAL)
    else:
        score8 = 0
        return button_next8.configure(state=NORMAL)

def ques9():
    frame8.pack_forget()
    button_next8.destroy()
    label11.pack_forget()

    global frame9
    frame9 = LabelFrame(root, text = "Question 9",padx=250,pady=230,bg = "white")
    frame9["font"] = font4
    frame9.pack(pady=80)

    global label12
    label12 = Label(frame9, text="Question 9 ?",bg="white",anchor=CENTER)
    label12["font"] = font6
    label12.pack(pady=10)

    r = IntVar()
    rb1 = Radiobutton(frame9, text = "Option 1", variable = r, value = 1,bg = "white", command = lambda: ans9(r.get()))
    rb2 = Radiobutton(frame9, text = "Option 2", variable = r, value = 2,bg = "white",command = lambda: ans9(r.get()))
    rb3 = Radiobutton(frame9, text = "Option 3", variable = r, value = 3,bg = "white",command = lambda: ans9(r.get()))
    rb4 = Radiobutton(frame9, text = "Option 4", variable = r, value = 4,bg = "white",command = lambda : ans9(r.get()))

    rb1.pack(anchor = W)
    rb2.pack(anchor = W)
    rb3.pack(anchor = W)
    rb4.pack(anchor = W)
    rb1["font"] = font5
    rb2["font"] = font5
    rb3["font"] = font5
    rb4["font"] = font5

    global button_next9
    button_next9 = Button(frame9, text="Next", bg="white", padx=15,pady=0, state = DISABLED )
    button_next9['font'] = font4
    button_next9.pack(pady=15)
    button_next9.configure(command = lambda : ques10())

def ans9(value):

    if value == 1:
        global score9
        score9 = 1
        return button_next9.configure(state=NORMAL)
    else:
        score9 = 0
        return button_next9.configure(state=NORMAL)

def ques10():
    frame9.pack_forget()
    button_next9.destroy()
    label12.pack_forget()

    global frame10
    frame10 = LabelFrame(root, text = "Question 10",padx=250,pady=230,bg = "white")
    frame10["font"] = font4
    frame10.pack(pady=80)

    global label13
    label13 = Label(frame10, text="Question 10 ?",bg="white",anchor=CENTER)
    label13["font"] = font6
    label13.pack(pady=10)

    r = IntVar()
    rb1 = Radiobutton(frame10, text = "Option 1", variable = r, value = 1,bg = "white", command = lambda: ans10(r.get()))
    rb2 = Radiobutton(frame10, text = "Option 2", variable = r, value = 2,bg = "white",command = lambda: ans10(r.get()))
    rb3 = Radiobutton(frame10, text = "Option 3", variable = r, value = 3,bg = "white",command = lambda: ans10(r.get()))
    rb4 = Radiobutton(frame10, text = "Option 4", variable = r, value = 4,bg = "white",command = lambda : ans10(r.get()))

    rb1.pack(anchor = W)
    rb2.pack(anchor = W)
    rb3.pack(anchor = W)
    rb4.pack(anchor = W)
    rb1["font"] = font5
    rb2["font"] = font5
    rb3["font"] = font5
    rb4["font"] = font5

    global button_next10
    button_next10 = Button(frame10, text="Finish", bg="white", padx=15,pady=0, state = DISABLED)
    button_next10['font'] = font4
    button_next10.pack(pady=15)
    button_next10.configure(command = lambda : result())

def ans10(value):

    if value == 4:
        global score10
        score10 = 1
        return button_next10.configure(state=NORMAL)
    else:
        score10 = 0
        return button_next10.configure(state=NORMAL)


def result():
    frame10.pack_forget()
    button_next10.destroy()
    label3.pack_forget()

    global FinalScore
    FinalScore = score1+score2+score3+score4+score5+score6+score7+score8+score9+score10

    global frame11
    frame11 = LabelFrame(root, text = "Result",padx=250,pady=230,bg = "white")
    frame11["font"] = font4
    frame11.pack(pady=80)

    #image at the end for result
    #label20 = Label(frame11,image = img,anchor = N)
    #label20.pack()

    if FinalScore <=2:
        global label15
        label15 = Label(frame11, text = "Very Poor Performance", bg = "white", anchor = CENTER)
        label15["font"] = font3
        label15.pack()

    elif FinalScore > 2 and FinalScore <=5:
        global label16
        label16 = Label(frame11, text = "Poor Performance", bg = "white", anchor = CENTER)
        label16["font"] = font3
        label16.pack()

    elif FinalScore > 5 and FinalScore <= 7:
        global label17
        label17 = Label(frame11, text="Average Performance", bg="white", anchor=CENTER)
        label17["font"] = font3
        label17.pack()

    elif FinalScore > 7 and FinalScore <=9:
        global label18
        label18 = Label(frame11, text = "Good Performance", bg = "white", anchor = CENTER)
        label18["font"] = font3
        label18.pack()

    elif FinalScore == 10:
        global label19
        label19 = Label(frame11, text = "Excellent Performance", bg = "white", anchor = CENTER)
        label19["font"] = font3
        label19.pack()


    global label14
    label14 = Label(frame11, text=("Result:",FinalScore,"/","10") ,bg="white",anchor=CENTER)
    label14["font"] = font6
    label14.pack(pady=10)

    global button_next11
    button_next11 = Button(frame11, text="Exit", bg="white", padx=15,pady=0, command = root.quit)
    button_next11['font'] = font4
    button_next11.pack(pady=10)


button_next = Button(root,text = "Next",bg = "white",padx=20,command = ques1)
button_next['font'] = font4
button_next.pack(anchor = S)


root.mainloop()