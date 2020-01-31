import arcade
import os

arcade.open_window(1200, 600, "Tank Test")

arcade.start_render() #doit être fait avant chaque commande de dessin

arcade.draw_rectangle_outline(295, 100, 45, 65,arcade.color.BRITISH_RACING_GREEN)




arcade.finish_render() #doit être fait à la fin du dessin
arcade.run() #garde la fenêtre ouverte jusqu'à ce que quelqu'un la ferme