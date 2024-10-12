import turtle
import random
import time
from itertools import repeat
from tkinter import messagebox, mainloop

pencere= turtle.Screen()
messagebox.showinfo("Kaplumbağayı Yakala","Oyun Başlıyoor")
pencere.bgcolor("light blue")
pencere.title("Turtle Ödevi")
pencere.setup(700,700)

kalem=turtle.Turtle()
kalem.shape("turtle")
kalem.shapesize(2,2,2)
kalem.color("green","pink")
kalem.penup()
kalem.speed(10)


style= ("Arial",20,"bold")
turtle.hideturtle()
turtle.penup()
turtle.goto(-110,300)
turtle.write("Süre:",font=style)

style= ("Arial",20,"bold")
turtle.hideturtle()
turtle.penup()
turtle.goto(-110,250)
turtle.write("Skor:",font=style)





koordinat_x= [-50,-100,-150,-200,-250,-300,50,100,150,200,250,300]
koordinat_y= [-50,-100,-150,-200,-250,-300,50,100,150,200,]

sure=5
skor= 0

while sure >0:
    kalem.goto(random.choice(koordinat_x),random.choice(koordinat_y))
    time.sleep(1)
    sure=sure-1
    repeat

if skor <3:
    messagebox.showinfo("Oyun Sonu","Kaybettiniz. Çıkmak için Q'ya basınız.")
else:
    messagebox.showinfo("Oyun Sonu","Tebrikler!! Kazandınız! Çıkmak için Q'ya basınız.")

pencere.listen()
pencere.onkey(fun=exit,key= "q")
#while sure > 0:




### GOTO FONKSİYONU KULLANABİLİRSİN, TURTLEIN POZİSYONU  KOORDİNATLA BELİTLENİYOR
#turtle.onclick(fonksiyon) tıklayınca bir artan fonksiyon yaz

mainloop()