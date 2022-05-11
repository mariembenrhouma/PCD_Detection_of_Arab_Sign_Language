from Controller.controleur import *
from Controller.controleur  import Image,ImageTk
from tkinter import *

##################### definition ########################
source = ""
destination = ""
t = ""
font = ("Myriad Arabic",16)


def Traduct(event):
    return Traduire(txt)
########################### principal code ##############################################
def sourde():
    root.destroy()
    global window,txt,frame
    window = Tk()
    window.title("application")
    window.geometry('1125x750')
    window.resizable(False,False)
    background,sound_img=declarationimage()
    img = Label(window,image=background,bg="#9AE1F5",anchor=CENTER)
    img.place(x=0,y=0)
    box_list_language = Combobox(window,values=('fr','ar','en','عربية'),font= font,justify=CENTER,height=10,width=13)
    box_list_language.current(1)
    box_list_language.place(x=50,y=193)
    def ComboAction(event):
        return comboAction(box_list_language)
    box_list_language.bind("<<ComboboxSelected>>", ComboAction)
    txt = scrolledtext.ScrolledText(window, width=29, height=7, background="#3580b1",font=("Myriad Arabic",16))
    txt.place(x=30.5, y=331)
    createButton(window, None, None, "#3580b1",play, 341, 579, 42, 42, sound_img,txt,box_list_language)
    createButton(window, '?', font, '#c2c2c2', '?',53,522,30,30,None,txt,None)
    createButton(window, '!', font, '#c2c2c2', '!',120,522,30,30,None,txt,None)
    createButton(window, '.', font, '#c2c2c2', '.',187,522,30,30,None,txt,None)
    createButton(window, ',', font, '#c2c2c2', ',', 254, 522, 30, 30,None,txt,None)
    createButton(window, 'supp', font, '#c2c2c2', 'supprime', 334, 522, 50, 30, None, txt, None)
    frame = Label(window, bg="#3580b1")
    frame.place(x=434, y=174)
    show_frames(frame)
    txt.bind("<Return>", Traduct)
    window.mainloop()
#__________________________________________#
def start_nas():
    root.destroy()
    nas = Tk()
    nas.title("نص")
    nas.geometry('1125x750')
    nas.resizable(False, False)
    nasback,nas_btn,img2 = declarationimagenas()
    img = Label(nas, image=nasback, bg="#9AE1F5", anchor=CENTER)
    img.place(x=0, y=0)
    text_to_img = scrolledtext.ScrolledText(nas, width=43, height=20, background="#3580b1")
    text_to_img.place(x=737, y=259)
    frame = Label(nas, bg="#3580b1")
    frame.place(x=57, y=230, width=645, height=420)
    btn=createButton(nas, None, None, "#3580b1",ajout, 841, 603, 153, 53,nas_btn,text_to_img,frame)
    nas.mainloop()
#__________________________________________#
def start_app():
    global root
    root = Tk()
    root.title("application")
    root.geometry('650x430')
    root.resizable(False, False)
    rootback,ichara,nas = declarationimageroot()
    img = Label(root,image=rootback,bg="#9AE1F5",anchor=CENTER)
    img.place(x=0,y=0)
    buton = Button(root, command=lambda: sourde(),background="#6169df", image=ichara)
    buton.place(x=64, y=181, width=225, height=75)
    buton = Button(root, command=lambda: start_nas(), background="#6169df", image=nas)
    buton.place(x=355, y=181, width=225, height=75)
    root.mainloop()
#__________________________________________#
start_app()