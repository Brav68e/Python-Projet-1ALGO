import tkinter as tk
from tkinter import filedialog
from pygame import mixer


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
        self.fenetre.resizable(False, False)
        #Music settings
        mixer.init()
        sound = mixer.Sound("Music/music.mp3")
        sound.play(-1)  #-1 = infinite loop

        menu = tk.Menu(self.fenetre)
        self.fenetre.config(menu=menu)
        
        '''Rolling Menu For Saved Games'''
        rolling_menu = tk.Frame(self.fenetre, borderwidth=3, bg="lightgrey")
        rolling_menu.pack(fill=tk.X)

        '''File Tab'''
        file_menu = tk.Menubutton(rolling_menu, text="File", width='20',borderwidth=2, bg='white', activebackground='grey', relief='raised')
        file_menu.grid(row=0, column=0)

        '''File Tab Options'''
        file_rolling_menu = tk.Menu(file_menu, tearoff=0)
        file_menu.config(menu=file_rolling_menu)
        file_rolling_menu.add_command(label="Load Game", command=self.load_game)
        
        start_btn = tk.Button(self.fenetre, text="Play", command=self.play, width=12, height=3)
        
        
        self.user1 = tk.Entry(self.fenetre, width=20)
        self.user2 = tk.Entry(self.fenetre, width=20)
        
        title = tk.Label(self.fenetre, text="CROWN CONQUEST", font=("Fast Drag Demo", 30, "bold"), fg="red")
        title.place(x=115,y=60)

        choix = tk.Label(self.fenetre, text="Choisissez la taille du plateau :", font=("Arial", 15))
        choix.place(x=170, y=130)

        self.cpt=tk.StringVar()
        self.cpt.set('6')
        lbl=tk.Label(self.fenetre, width='10', textvariable=self.cpt, font='Arial 20 bold')
        lbl.place(x=210, y=170)

        '''Buttons to change the size of the board'''
        btn_plus=tk.Button(self.fenetre, text="+", command=self.plus, width='3', height='1')
        btn_plus.place(x=320, y=175)
        btn_moins=tk.Button(self.fenetre, text="-", command=self.moins, width='3', height='1')
        btn_moins.place(x=250, y=175)   #Used to be y=225


        user1_text = tk.Label(self.fenetre, text="Player 1 :", font=("Arial"))
        user1_text.place(x=10, y=350)

        user2_text = tk.Label(self.fenetre, text="Player 2 :", font=("Arial"))

        self.user1.place(x=120, y=355)
        self.user2.place(x=440, y=355)

        user2_text.place(x=330, y=350)
        start_btn.place(x=250, y=500)

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
