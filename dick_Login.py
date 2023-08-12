from tkinter import *
from tkinter import messagebox
import ast
import subprocess

#region fill
f = open("G:/Python/Group/dick_List.txt","r")
dick_List = []
line = f.readlines()
Dick_Fill = line
for er in range(len(line)):
    Dick_Data = ast.literal_eval("{" + Dick_Fill[er] + "}")
    dick_List.append(Dick_Data)
#endregion

tk = Tk()
tk.geometry("350x470")
tk.title("Login")
tk.resizable(False,False)
icon_img = PhotoImage(file="G:/Python/image/icon-spades64.ico")
tk.wm_iconphoto(False,icon_img)
tk.configure(bg="#000")

img_lock128 = PhotoImage(file="G:/Python/image/lock128.png")

j=0
r=10
for i in range(100):
    c=str(111111+r)
    Frame(tk,width=10,height=800,bg="#"+c).place(x=j,y=0)   
    j=j+7                                                  
    r=r+1

Back = Frame(tk,width=224,height=370,bg="#fff")
Back.place(x=63,y=50)

text_font = ("휴먼편지체 보통",12,"bold")
Entry_font = ("휴먼편지체 보통",15,"bold")

location = 180

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
ID_Text = Label(Back,text="ID",bg=Text_background_color,fg=font_color_Text,font=text_font).place(x=12,y=location)
Pass_Text = Label(Back,text="Password",bg=Text_background_color,fg=font_color_Text,font=text_font).place(x=12,y=location+60)
#endregion
#region Entry
ID_Entry = Entry(Back,bg=background_color,fg=font_color,font=Entry_font,insertbackground="#000",bd=0,width=18)
ID_Entry.place(x=12,y=location+25)

Pass_Entry = Entry(Back,bg=background_color,fg=font_color,font=Entry_font,insertbackground="#000",bd=0,width=18,show="●")
Pass_Entry.place(x=12,y=location+85)
#endregion
#region Frame
ID_Frame = Frame(Back,width=200,height=2,bg="#000")
ID_Frame.place(x=12,y=location+52)
Pass_Frame = Frame(Back,width=200,height=2,bg="#000")
Pass_Frame.place(x=12,y=location+112)
#endregion

def Entry_Get():
    IDput = ID_Entry.get()
    Passput = Pass_Entry.get()
    Status = ''
    for ern in range(len(dick_List)):
        if IDput in dick_List[ern] and dick_List[ern][IDput]["Password"] == Passput:
            Status = dick_List[ern][IDput]
    if Status:
        Status_Name = Status["Name"]
        Status_Lv = Status["Lv"]
        Status_Xp = Status["Xp"]
        Status_XpMax = Status["XpMax"]
        
        text = '{'+f'"ID":"{IDput}","Password":"{Passput}","Name":"{Status_Name}","Lv":{Status_Lv},"Xp":{Status_Xp},"XpMax":{Status_XpMax}'+'}'

        with open('G:/Python/save.txt','w',encoding='UTF-8') as f:
            if line:
                f.write(text)
                
        subprocess.run(["python","G:/Python/Python code Two/page.py"])
        #subprocess.run("D:/Project/My project/Build/Eat Coins To Increase Your Strength.exe")
    else:
        messagebox.showerror("알림","제대로 입력해주세요.")


b = Button(Back,text="Ok",font=("휴먼편지체 보통",15,"bold"),bd=0,fg=white,bg=black,width=16,height=1,command=Entry_Get)
b.place(y=315,x=13)


#messagebox.showinfo("알림",f"{Status[0]}님의 상태\n\nLv.{Status_Lv}\n{Status_Xp}/{Status_XpMax}")


tk.mainloop()