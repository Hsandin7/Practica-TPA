from tkinter import *

window = Tk()


canvas = Canvas(window, height=1100, width=110*8.15, background="black")
canvas.pack()

imagen = PhotoImage(file='Graficos/Menu_Inicio.png')

la_imagen = canvas.create_image(0, 0, image=imagen, anchor="nw")

window.mainloop()


# canvas.create_image(posx, posy, )


# Igual es util para botones:
    # label = Label(window, image=imagen)
    # label.pack()





