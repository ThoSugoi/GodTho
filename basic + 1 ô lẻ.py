from tkinter import *

uwu= Tk()
uwu.title('Puzzle Mathrathon')
uwu.geometry("500x620")
uwu.resizable(False, False)
uwu2= Canvas(uwu, width= 500, height= 620, bg='#58D68D')
uwu2.create_text(235, 600, text="Ủng hộ coder Thỏ Sugoi tại momo 0969976678", fill="black", font=('Helvetica 10 '))
uwu2.pack()
def run():
    turns = []
    colors = ['#fbf6f8','#f2dee7','#ebccd9','#e5bacc','#dea9bf','#d797b2','#d185a5','#ca7398','#c3628b','#bd507e','#b14372','#9f3c66','#8e355b','#7c2e4f','#6a2844','#5e233c']

    def plus(a,b):
        value[a][b] = value[a][b]+1
        list1[a][b] = create_btn(value[a][b],a,b)

    def do(a,b):
        turns.append([a,b])
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
    
    def minus(a,b):
        value[a][b] = value[a][b]-1
        list1[a][b] = create_btn(value[a][b],a,b)
    
    def undo():

        if len(turns) >0:
            p = turns[-1][0]
            q = turns[-1][1]
            minus(p,q)
            if q+1<5:
                minus(p,q+1)
            if q-1>=0:
                minus(p,q-1)
            if p-1>=0:
                minus(p-1,q)
            if p+1<5:
                minus(p+1,q)
            turns.pop()
    
    def create_btn(a,b,c):
        m = a
        if m< 15:
            btn = Button(uwu,
                    #bg='#B3DAFF',
                    text =str(m),
                    bg = colors[m],
                    height= 2,
                    width=5,
                    command= lambda : do(b,c),
                    font= ('Helvetica 20 bold '))
        else: 
            btn = Button(uwu,
                    #bg='#B3DAFF',
                    text =str(m),
                    bg = colors[14],
                    height= 2,
                    width=5,
                    command= lambda : do(b,c),
                    font= ('Helvetica 20 bold '))            

        btn.place(x=b*100, y=c*100)
        return btn

    value=[[0 for i in range(0,5)] for j in range(0,5)]
    value[3][1] = 1
    btn = Button(uwu,
             text ="UNDO",
             height= 3,
             width=21,
             command= lambda : undo(),
             font= ('Helvetica 12 bold '))
    btn.place(x=250, y=510)


    list1 = [[create_btn(value[i][j],i,j) for i in range(0,5)] for j in range(0,5)]

    

run()

def restart():
    print("RESTARTED!")
    run()
btn = Button(uwu,
             text ="RESTART",
             height= 3,
             width=21,
             command= lambda : restart(),
             font= ('Helvetica 12 bold '))
btn.place(x=20, y=510)


uwu.mainloop()