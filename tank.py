#http://arcade.academy/examples/drawing_primitives.html
import arcade
import os

arcade.open_window(1200, 600, "Tanks",antialiasing=True, resizable=True)

arcade.start_render() #doit être fait avant chaque commande de dessin

arcade.draw_rectangle_filled(600, 300, 100, 150,arcade.color.BLUE) #rectangle du tank bleu
arcade.draw_rectangle_filled(600,370,30,150,arcade.color.BLUE) #rectangle du canon du tank bleu
arcade.draw_rectangle_outline(600,300,100,150,arcade.color.WHITE,border_width=2) #contour du tank bleu en blanc
arcade.draw_rectangle_outline(600,370,30,150,arcade.color.WHITE)
arcade.draw_circle_filled(600,300,20,arcade.color.DARK_BLUE)




arcade.finish_render() #doit être fait à la fin du dessin
arcade.run() #garde la fenêtre ouverte jusqu'à ce que quelqu'un la ferme