import arcade
import os
import tank

def vie():
    hpbleu,hprouge=100
    if hpbleu==0:
        arcade.draw_text("Tank Bleu est mort ! Victoire du Tank Rouge !")
    if hprouge==0:
        arcade.draw_text("Tank Rouge est mort ! Victoire du Tank Bleu !")

def barre():
    arcade.draw_rectangle_outline(width=100,height=10,arcade.color.WHITE,border_width=2)
    if hp==100:



