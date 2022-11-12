from tkinter import *
from tkinter import ttk
uwu= Tk()

uwu.geometry("500x620")
uwu.resizable(False, False)

def run():
    list1 = [[1,2,5],[80,5,6]]
    def index_table(mylist, char):
        for sub_list in mylist:
            if char in sub_list:
                return (mylist.index(sub_list), sub_list.index(char))
    def plus(a,b):
        value[a][b] = value[a][b]+1
        list1[a][b] = create_btn(value[a][b],a,b)

    def get_button(a,b):
        print(a,b)
        plus(a,b)
        if b+1<5:
            plus(a,b+1)
        if b-1>=0:
            plus(a,b-1)
        if a-1>=0:
            plus(a-1,b)
        if a+1<5:
            plus(a+1,b)
    
    def create_btn(a,b,c):
        btn = Button(uwu,
                text =str(a),
                height= 2,
                width=5,
                command= lambda : get_button(b,c),
                font= ('Helvetica 20 bold '))

        btn.place(x=b*100, y=c*100)
        return btn

    value=[[0 for i in range(0,5)] for j in range(0,5)]

    list1 = [[create_btn(value[i][j],i,j) for i in range(0,5)] for j in range(0,5)]

run()

def restart():
    run()
btn = Button(uwu,
             text ="HERE IS YOUR RESTART BUTTON\n YOU WEAKLING!",
             height= 3,
             width=42,
             command= lambda : restart(),
             font= ('Helvetica 12 bold '))
btn.place(x=30, y=510)


uwu.mainloop()