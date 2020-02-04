#http://arcade.academy/examples/drawing_primitives.html
import arcade
import os

hpbleu,hprouge=(100,100)

def tank_bleu():
    arcade.draw_rectangle_filled(600, 300, 100, 150,arcade.color.BLUE) #rectangle du tank bleu
    arcade.draw_rectangle_filled(600,370,30,150,arcade.color.BLUE) #rectangle du canon du tank bleu
    arcade.draw_rectangle_outline(600,300,100,150,arcade.color.WHITE,border_width=2) #contour du tank bleu en blanc
    arcade.draw_rectangle_outline(600,370,30,150,arcade.color.WHITE)#contour du canon du tank bleu
    arcade.draw_circle_filled(600,300,20,arcade.color.DARK_BLUE) #pivot du canon

def tank_rouge():
    arcade.draw_rectangle_filled(300, 300, 100, 150,arcade.color.RED) #rectangle du tank rouge
    arcade.draw_rectangle_filled(300,370,30,150,arcade.color.RED) #rectangle du canon du tank bleu
    arcade.draw_rectangle_outline(300,300,100,150,arcade.color.WHITE,border_width=2) #contour du tank rouge en blanc
    arcade.draw_rectangle_outline(300,370,30,150,arcade.color.WHITE)#contour du canon du tank rouge
    arcade.draw_circle_filled(300,300,20,arcade.color.DARK_BLUE) #pivot du canon

def vie(hpbleu,hprouge):
    if hpbleu==0:
        arcade.draw_text("Tank Bleu est mort ! Victoire du Tank Rouge !")
    if hprouge==0:
        arcade.draw_text("Tank Rouge est mort ! Victoire du Tank Bleu !")

def barrebleu(x,y):
    arcade.draw_rectangle_outline(arcade.color.WHITE, width=100,height=10,border_width=2)
    if hpbleu==100:
        arcade.draw_rectangle_filled(arcade.color.LIGHT_BLUE, width=100,height=10)
    elif hpbleu==80:
        arcade.draw_rectangle_filled(arcade.color.LIGHT_BLUE,width=80,height=10,)
    elif hpbleu==60:
        arcade.draw_rectangle_filled(arcade.color.LIGHT_BLUE,width=60,height=10,)
    elif hpbleu==40:
        arcade.draw_rectangle_filled(arcade.color.LIGHT_BLUE,width=40,height=10,)
    elif hpbleu==20:
        arcade.draw_rectangle_filled(arcade.color.LIGHT_BLUE,width=20,height=10,)
    elif hpbleu==0:
        vie(hpbleu)

def barrerouge(x,y):
    arcade.draw_rectangle_outline(x,y-20,arcade.color.WHITE,width=100,height=10,border_width=2)
    if hprouge==100:
        arcade.draw_rectangle_filled(x,arcade.color.LIGHT_BLUE,width=100,height=10)
    elif hprouge==80:
        arcade.draw_rectangle_filled(arcade.color.LIGHT_BLUE,width=80,height=10)
    elif hprouge==60:
        arcade.draw_rectangle_filled(arcade.color.LIGHT_BLUE,width=60,height=10,)
    elif hprouge==40:
        arcade.draw_rectangle_filled(arcade.color.LIGHT_BLUE,width=40,height=10,)
    elif hprouge==20:
        arcade.draw_rectangle_filled(arcade.color.LIGHT_BLUE,width=20,height=10,)
    elif hprouge==0:
        vie(hprouge)



def main():
    arcade.open_window(1200, 600, "Tanks",antialiasing=True, resizable=True)
    arcade.start_render() #doit être fait avant chaque commande de dessin

    tank_bleu()
    tank_rouge()

    
    arcade.finish_render() #doit être fait à la fin du dessin
    arcade.run() #garde la fenêtre ouverte jusqu'à ce que quelqu'un la ferme

main()