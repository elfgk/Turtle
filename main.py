import turtle
import random
import time
from tkinter import messagebox, mainloop

pencere= turtle.Screen()
messagebox.showinfo("Kaplumbağayı Yakala","Oyun Başlıyor")
pencere.bgcolor("light blue")
pencere.title("Turtle")
pencere.setup(700,700)

hedef = turtle.Turtle()
hedef.shape("turtle")
hedef.shapesize(2,2,2)
hedef.color("black","pink")
hedef.penup()
hedef.speed(10)
sure=20
skor= 0

def tiklama(x,y):
    global skor
    skor = skor+1
    skorum.clear()
    style = ("Arial", 20, "bold")
    skorum.write(skor,font=style)

def kalan_zaman():
    global sure
    time.sleep(1)
    sure=sure-1
    kalan_sure.clear()
    style = ("Arial", 20, "bold")
    kalan_sure.write(sure,font=style)


koordinat_x= [-50,-100,-150,-200,-250,-300,50,100,150,200,250,300]
koordinat_y= [-50,-100,-150,-200,-250,-300,50,100,150,200,]



sure_yazisi=turtle.Turtle()
style= ("Arial",20,"bold")
sure_yazisi.hideturtle()
sure_yazisi.penup()
sure_yazisi.speed(10)
sure_yazisi.goto(-110,300)
sure_yazisi.write("Süre:",font=style)

style= ("Arial",20,"bold")
kalan_sure= turtle.Turtle()
kalan_sure.hideturtle()
kalan_sure.penup()
kalan_sure.speed(10)
kalan_sure.goto(100,300)
kalan_sure.write(sure,font=style)




skor_yazisi=turtle.Turtle()
style= ("Arial",20,"bold")
skor_yazisi.hideturtle()
skor_yazisi.penup()
skor_yazisi.speed(10)
skor_yazisi.goto(-110,250)
skor_yazisi.write("Skor:",font=style)

style= ("Arial",20,"bold")
skorum = turtle.Turtle()
skorum.hideturtle()
skorum.penup()
skorum.speed(10)
skorum.goto(100,250)
skorum.write(skor,font=style)

while sure >0:
    hedef.goto(random.choice(koordinat_x),random.choice(koordinat_y))
    hedef.onclick(tiklama)
    kalan_zaman()
    hedef.home()

if skor <3:
    messagebox.showinfo("Oyun Sonu","Kaybettiniz. Çıkmak için Q'ya basınız.")
else:
    messagebox.showinfo("Oyun Sonu","Tebrikler!! Kazandınız!! Çıkmak için Q'ya basınız.")

pencere.listen()
pencere.onkey(fun=exit,key= "q")

mainloop()