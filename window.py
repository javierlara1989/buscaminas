from Tkinter import *
import time, random


class Buscaminas(Frame):

    Matriz = [[None] * 10] * 10
    Matriz_prima = [[None] * 10] * 10
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Busca minas")
        self.pack(fill=BOTH, expand=1)
        self.menu()

    def menu(self):
        self.clear_canvas()
        self.button_easy = Button(self, text="Facil", command= lambda: self.game('e'))
        self.button_easy.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.button_medium = Button(self, text="Medio", command= lambda: self.game('m'))
        self.button_medium.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.button_hard = Button(self, text="Dificil", command= lambda: self.game('h'))
        self.button_hard.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.button_quit = Button(self, text="Salir", command=self.quit)
        self.button_quit.place(relx=0.5, rely=0.6, anchor=CENTER)

    def game(self, difficulty):
        self.clear_canvas()

        if(difficulty == 'e'):
            ancho = 5
            largo = 5
            self.create_matrix([1,0,0,0], ancho, largo)
        if(difficulty == 'm'):
            ancho = 8
            largo = 5
            self.create_matrix([1,1,0,0,0], ancho, largo)
        if(difficulty == 'h'):
            ancho = 8
            largo = 8
            self.create_matrix([1,1,1,0,0,0], ancho, largo)

        self.btn=  [[0 for x in xrange(ancho)] for y in xrange(largo)]
        for x in range(0, largo):
            for y in range(0, ancho):
                self.btn[x][y] = Button(self ,command= lambda x=x, y=y: self.buttonPush(x, y), text="*")
                self.btn[x][y].grid(column=x, row=y)

    def clear_canvas(self):
        for child in Frame.winfo_children(self):
            child.destroy()

    def create_matrix(self, perc, x, y):
        for d in range(0, x):
            for f in range(0, y):
                self.Matriz[d][f] = random.sample(perc, 1)[0]
        print(len(self.Matriz),len(self.Matriz[0]))
        for d in range(0, x):
            for f in range(0, y):
                print(d,f)
                if self.Matriz[d][f] == 0:
                    if d == 0:
                        if f == 0:
                            self.Matriz_prima[d][f] = self.Matriz[d+1][f+1] + self.Matriz[d+1][f] + self.Matriz[d][f+1]
                        elif f == y:
                            self.Matriz_prima[d][f] = self.Matriz[d+1][f-1] + self.Matriz[d+1][f] + self.Matriz[d][f-1]
                        else:
                            self.Matriz_prima[d][f] = self.Matriz[d+1][f+1] + self.Matriz[d+1][f] + self.Matriz[d][f+1] + self.Matriz[d+1][f-1] + self.Matriz[d][f-1]
                    elif d == x:
                        if f == 0:
                            self.Matriz_prima[d][f] = self.Matriz[d-1][f] + self.Matriz[d-1][f+1] + self.Matriz[d][f+1]
                        elif f == y:
                            self.Matriz_prima[d][f] = self.Matriz[d-1][f] + self.Matriz[d-1][f-1] + self.Matriz[d][f-1]
                        else:
                            self.Matriz_prima[d][f] = self.Matriz[d-1][f] + self.Matriz[d-1][f+1] + self.Matriz[d][f+1] + self.Matriz[d-1][f-1] + self.Matriz[d][f-1]
                    else:
                        if f == 0:
                            self.Matriz_prima[d][f] = self.Matriz[d-1][f] + self.Matriz[d-1][f+1] + self.Matriz[d][f+1] + self.Matriz[d+1][f+1] + self.Matriz[d+1][f]
                        elif f == y:
                            self.Matriz_prima[d][f] = self.Matriz[d-1][f] + self.Matriz[d-1][f-1] + self.Matriz[d][f-1] + self.Matriz[d+1][f-1] + self.Matriz[d+1][f]
                        else:
                            self.Matriz_prima[d][f] = self.Matriz[d-1][f] + self.Matriz[d-1][f-1] + self.Matriz[d][f-1] + self.Matriz[d+1][f-1] + self.Matriz[d+1][f] + self.Matriz[d-1][f+1] + self.Matriz[d][f+1] + self.Matriz[d+1][f+1]
                        
        print(self.Matriz)

    def buttonPush(self, x, y):
        if self.Matriz[x][y] == 'mina':
            self.btn[x][y].configure(background='red', text='x')
            print("Boom perdiste")
            self.menu()
        else:
            self.btn[x][y].configure(background='green', text=self.Matriz[x][y])

def main():

    root = Tk()
    root.geometry("300x300+800+300") # x_size, y_size, x_position, y_position
    app = Buscaminas(root)
    root.mainloop()  

if __name__ == '__main__':
    main()
