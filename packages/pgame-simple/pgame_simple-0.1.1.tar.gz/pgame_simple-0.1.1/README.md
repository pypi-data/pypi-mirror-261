pgame_simple is a simple lib based on pygame
by MRanos


simple example:

from pgame_simple import pgame_simple
game = pgame_simple.screen(400,400)
player = game.image("player.png")
player_x,player_y=50,50
def update():
   global player_x , player_y
   game.bg((255,255,255))
   game.draw(player,player_x,player_y)
   player_x = game.movex(player_x,1)
   player_y = game.movey(player_y,1)
   
game.start(update)
