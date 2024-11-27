import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import tkinter.font as tkFont


class MainMenu():

    def __init__(self, controller, root = 0):

        self.controller = controller

        #Check for root parameter
        if root:
            self.fenetre = root
            #delete every child
            for el in self.fenetre.winfo_children():
                el.destroy()
        else:
            self.fenetre = tk.Tk()


        #General settings
        self.fenetre.title("CROWN CONQUEST")
        self.fenetre.geometry("600x600")
        self.fenetre.configure(bg="#f0f0ed")
        self.fenetre.resizable(False, False)
        font_path = "fonts/MedievalTimes-AL7l6.ttf"
        custom_font = tkFont.Font(family=font_path, size=24)
        #Music settings
        mixer.init()
        sound = mixer.Sound("Music/music.mp3")
        sound.play(-1)  #-1 = infinite loop

        menu = tk.Menu(self.fenetre)
        self.fenetre.config(menu=menu)
        
        
        img = tk.PhotoImage(file="image/manette.png")
        start_btn = tk.Button(self.fenetre,image=img,compound="top", text="Play", command=self.play, width=120, height=60, bg="#0a82db", fg="#f0f0ed")
        start_btn.image = img
        
        
        self.user1 = tk.Entry(self.fenetre, width=30, bd=3, relief="sunken", font=("Arial", 14), fg="grey")
        self.user2 = tk.Entry(self.fenetre, width=30, bd=3, relief="sunken", font=("Arial", 14), fg="grey")
        
        title = tk.Label(self.fenetre, text="CROWN CONQUEST", font=custom_font, fg="#0a82db", bg="#f0f0ed")
        title.place(x=100,y=20)
        subtitle = tk.Label(self.fenetre, text="Dominate the Empire", font=("Arial", 15, "italic"), fg="red", bg="#f0f0ed")
        subtitle.place(x=200,y=70)

        choix = tk.Label(self.fenetre, text="Choisissez la taille du plateau :", font=("Arial", 15),bg="#f0f0ed", fg="#0a82db")
        choix.place(x=170, y=180)

        self.cpt=tk.StringVar()
        self.cpt.set('6')
        lbl=tk.Label(self.fenetre, width='10', textvariable=self.cpt, font='Arial 20 bold',bg="#f0f0ed", fg="#0a82db")
        lbl.place(x=210, y=220)

        '''Buttons to change the size of the board'''
        btn_plus=tk.Button(self.fenetre, text="+", command=self.plus, width='3', height='1',bd= 0,bg="#1cb40d", fg="#ffffff",font=("Arial", 15, "bold"))
        btn_plus.place(x=330, y=220)
        btn_moins=tk.Button(self.fenetre, text="-", command=self.moins, width='3', height='1',bd=0, bg="#d5041d", fg="#ffffff",font=("Arial", 15, "bold"))
        btn_moins.place(x=220, y=220)   #Used to be y=225


        '''Load Save button'''
        img2 = tk.PhotoImage(file="image/importer.png") 
        load_save = tk.Button(self.fenetre, image=img2, compound="top", text="Load Saved Game", width=120, height=60, borderwidth=2,bg="#0a82db",fg="#f0f0ed" ,command=self.load_game)
        load_save.image = img2 
        load_save.place(x=320, y=530) #220, 570

        user1_text = tk.Label(self.fenetre, text="Player 1 :", font=("Arial"),bg="#f0f0ed", fg="#0a82db")
        user1_text.place(x=10, y=355)

        user2_text = tk.Label(self.fenetre, text="Player 2 :", font=("Arial"),bg="#f0f0ed", fg="#0a82db")

        self.user1.place(x=120, y=355)
        self.user2.place(x=120, y=405)

        user2_text.place(x=10, y=405)
        start_btn.place(x=130, y=530)

        '''Placeholders'''
        self.user1.config(fg="grey")
        self.user1.insert(0, "Enter username here")
        self.user1.bind("<FocusIn>", self.entry_focus_in)
        self.user1.bind("<FocusOut>", self.entry_focus_out)

        self.user2.config(fg="grey")
        self.user2.insert(0, "Enter username here")
        self.user2.bind("<FocusIn>", self.entry_focus_in2)
        self.user2.bind("<FocusOut>", self.entry_focus_out2)

        self.fenetre.mainloop()

###################################################################################

    def entry_focus_in(self,event):
        if self.user1.get() == "Enter username here":
            self.user1.delete(0, "end")
            self.user1.config(fg="black")

###################################################################################

    def entry_focus_out(self,event):
        if self.user1.get() == "":
            self.user1.insert(0, "Enter username here")
            self.user1.config(fg="grey")

###################################################################################

    def entry_focus_in2(self,event):
        if self.user2.get() == "Enter username here":
            self.user2.delete(0, "end")
            self.user2.config(fg="black")

###################################################################################

    def entry_focus_out2(self,event):
        if self.user2.get() == "":
            self.user2.insert(0, "Enter username here")
            self.user2.config(fg="grey")        

###################################################################################

    def plus(self):
        if int(self.cpt.get()) < 12:
            self.cpt.set(int(self.cpt.get()) + 2)

###################################################################################

    def moins(self):
        if int(self.cpt.get()) > 6:
            self.cpt.set(int(self.cpt.get()) - 2)

###################################################################################
      
    def getUsername1(self):
        if self.user1.get() == "Enter username here" or "":
            return "Player 1"
        else:
            return self.user1.get()
        
###################################################################################

    def getUsername2(self):
        if self.user2.get() == "Enter username here" or "":
            return "Player 2"
        else:
            return self.user2.get()

###################################################################################

    def load_game(self):
        '''Use to select a file, read it and launch the game with those parameters'''
        file_path = filedialog.askopenfilename()
        self.controller.launch_game(self.fenetre, path = file_path)


###################################################################################


    def play(self):
        '''Function to start the game, bind with the play button'''
        p1 = self.getUsername1()
        p2 = self.getUsername2()
        #Launch the game
        self.controller.launch_game(self.fenetre, int(self.cpt.get()), p1, p2)



if __name__ == "__main__":

    MainMenu()
