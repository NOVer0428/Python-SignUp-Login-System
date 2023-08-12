from tkinter import *
from tkinter import messagebox
import ast
import random

f = open("G:/Python/Group/dick_List.txt","r")

dick_List = []
line = f.readlines()
Dick_Fill = line
for er in range(len(line)):
    Dick_Data = ast.literal_eval("{" + Dick_Fill[er] + "}")
    dick_List.append(Dick_Data)

Windows = Tk()
Windows.geometry("350x530")
Windows.resizable(False,False)
Windows.title("Sign Up")
icon_img = PhotoImage(file="G:/Python/image/icon-spades64.ico")
Windows.wm_iconphoto(False,icon_img)
Windows.configure(bg="#000")

j=0
r=10
for i in range(100):
    c=str(111111+r)
    Frame(Windows,width=10,height=800,bg="#"+c).place(x=j,y=0)   
    j=j+7                                                  
    r=r+1

img_lock128 = PhotoImage(file="G:/Python/image/lock128.png")

Back = Frame(Windows,width=224,height=430,bg="#fff")
Back.place(x=63,y=50)

text_font = ("휴먼편지체 보통",12,"bold")
Entry_font = ("휴먼편지체 보통",15,"bold")

location = 240

#region color
black = "#000"
white = "#fff"

font_color_Text = black
font_color = black

Text_background_color = white
background_color = white
#endregion

Main_img = Label(Back,image=img_lock128,bg=white)
Main_img.place(x=48,y=32) 

#region Text
Name_Text = Label(Back,text="NICKNAME",bg=Text_background_color,fg=font_color_Text,font=text_font).place(x=12,y=location-60)
ID_Text = Label(Back,text="ID",bg=Text_background_color,fg=font_color_Text,font=text_font).place(x=12,y=location)
Pass_Text = Label(Back,text="PASSWORD",bg=Text_background_color,fg=font_color_Text,font=text_font).place(x=12,y=location+60)
#endregion
#region Entry
Name_Entry = Entry(Back,bg=background_color,fg=font_color,font=Entry_font,insertbackground="#000",bd=0,width=18)
Name_Entry.place(x=12,y=location-35)

ID_Entry = Entry(Back,bg=background_color,fg=font_color,font=Entry_font,insertbackground="#000",bd=0,width=18)
ID_Entry.place(x=12,y=location+25)

Pass_Entry = Entry(Back,bg=background_color,fg=font_color,font=Entry_font,insertbackground="#000",bd=0,width=18,show="●")
Pass_Entry.place(x=12,y=location+85)
#endregion
#region Frame
Name_Frame = Frame(Back,width=200,height=2,bg="#000")
Name_Frame.place(x=12,y=location-8)
ID_Frame = Frame(Back,width=200,height=2,bg="#000")
ID_Frame.place(x=12,y=location+52)
Pass_Frame = Frame(Back,width=200,height=2,bg="#000")
Pass_Frame.place(x=12,y=location+112)
#endregion



def Sign():
    Nameput = Name_Entry.get()
    IDput = ID_Entry.get()
    Passput = Pass_Entry.get()

    Allowed = False
    for ern in range(len(dick_List)):
        if IDput in dick_List[ern]:
            Allowed = True
            break
            
    if Allowed == False:
        Num = ''
        for w in range(4):
            Num += str(random.randrange(1,10))

        text = f'"{IDput}":'+'{'+f'"ID":"{IDput}","Password":"{Passput}","Name":"{Nameput}#{Num}","Lv":1,"Xp":0,"XpMax":100'+'}'

        with open('G:/Python/Group/dick_List.txt','a',encoding='UTF-8') as f:
            if line:
                f.write("\n" + text)

        messagebox.showinfo("알림",f"◆ ID : {IDput}\n◆ Password : {Passput} 기억하세요.")
        Name_Entry.delete(0,END)
        ID_Entry.delete(0,END)
        Pass_Entry.delete(0,END)
    else:
        messagebox.showerror("알림","이미 있는 계정입니다")


f.close()
b = Button(Back,text="Ok",font=("휴먼편지체 보통",15,"bold"),bd=0,fg=white,bg=black,width=16,height=1,command=Sign)
b.place(y=location+135,x=13)
Windows.mainloop()