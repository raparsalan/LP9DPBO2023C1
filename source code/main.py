from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk,Image

hunians = []
hunians.append(Apartemen("Bintang", 2, "Bintang dan Fahru", "10x13m", "Pribadi", 3, "apart1.jpg"))
hunians.append(Rumah("Rayhan", "Jalu", 1, "10x18m", "Sewa", 2, "rumah1.jpg"))
hunians.append(Indekos("Ibu Indah", "Cantika", "Putri", 1, "4x3m", "Sewa", "kosan1.jpg"))
hunians.append(Rumah("Rifqi", "Rifqi dan Syifa", 2, "13x21m", "Pribadi", 3, "rumah2.jpg"))

root = Tk()
root.title("Praktikum DPBO Python")

foto_hunian=[]

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())
    
    d_frame = LabelFrame(top, text="Data Hunian", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    img = Image.open("D:/C/DPBO/Praktikum 9/latihan/assets/" + hunians[index].get_foto())  
    img = img.resize((200, 200))  
    photo_img = ImageTk.PhotoImage(img)
    foto_hunian.append(photo_img)  
    img_label = Label(d_frame, image=photo_img)
    img_label.grid(row=1, column=0)

    data_hunian = Label(d_frame, text="Detail Hunian : \n" + hunians[index].get_details(), anchor="w").grid(row=0, column=0, sticky="w")

    
def list_hunian():
    label.destroy()
    frame_landing.destroy()
    img_label.destroy()
    button.destroy()
    frame = LabelFrame(root, text="Data Seluruh Hunian", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    idx = Label(frame, text="", width=5, borderwidth=1, relief="solid")
    idx.grid(row=0, column=0)

    type = Label(frame, text="Jenis Hunian", width=15, borderwidth=1, relief="solid")
    type.grid(row=0, column=1)
    
    name = Label(frame, text="Penghuni", width=40, borderwidth=1, relief="solid")
    name.grid(row=0, column=2)

    b_detail = Label(frame, text="Action", width=10, borderwidth=1, relief="solid")
    b_detail.grid(row=0, column=3)
    
    index = 1
    for i, h in enumerate(hunians):
        idx = Label(frame, text=str(index), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)
        
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=i: details(index))
        b_detail.grid(row=index, column=3)
        index+=1

label = Label(root, text="Welcome", font=('Arial', 16))
label.pack()
    
#setting foto
img = Image.open("D:/C/DPBO/Praktikum 9/latihan/assets/logo.jpg")
img = img.resize((200, 200))
photo_img = ImageTk.PhotoImage(img)
foto_hunian.append(photo_img)
frame_landing = Frame(root, padx=30, pady=30)
frame_landing.pack(padx=30, pady=30)
img_label = Label(frame_landing, image=photo_img)
img_label.pack()

# button  Main Page
button = Button(root, text='List Hunian', font=('Arial', 16), command=list_hunian)
button.pack(side=BOTTOM)
root.mainloop()