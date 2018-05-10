Overview:

This is a very simple pyglet game with a character that moves around trying to get to the finishing point.

See pyglet documentation here: https://bitbucket.org/pyglet/pyglet/wiki/Home

This "game" only has movement, rectangle collision, and a way to get from level to level.
You can modify your copy of the files to create your own level.
Currently, if you reach the finish, the game will exit.

Each person has a copy of the files. Each group should upload their complete set into a different folder on the shared Google drive.

HOW TO CHANGE LEVEL TO NEXT GROUPS GAME:

1) Look your respective game.py under the update(dt) function
2) Look within the double for loop and inside the if statement and look for something like:
			os.system("py game.py")
3) Change the string (In this case game.py) to the next groups game.py file path

There are 6 python files:

game.py
physicalobject.py
player.py
finish.py
block.py
settings.py

The rest are images. 

The pyglet folder contains the pyglet library and will be used to import from.
Please look at the pyglet documentation for more information on implementing.

To start the game, double click on game.py. There, you will see 3 different colored squares
The green square is the player, the red is the finish line, and the yellow square is an example wall.

Each square has a corresponding file to it. Green corresponds to player.py, red corresponds to finish.py,
and yellow corresponds to block.py.
All three inherit from the file called physicalobject.py.

============GAME.PY============

game.py is the main file where all other objects get initialized, updated, and displayed on the screen.
game.py uses different classes such as the aforementioned player, finish and blocks, which are all physicalobjects.

init()

	This is where everything is initialized. 
	
on_draw()
	
	This is used to clear the window and draw the sprites. To modify it, look at the pyglet documentation 
	to see what cool things you can do with it
	
update(dt)
	
	This basically checks for collision. Some optimization to avoid double checking collisions twice.
	Checks if the finish line is reached. Also moves the objects.

============PHYSICALOBJECT.PY============

physicalobject.py is where you get all the functions.

update(self,dt)

	This is the general version of the update which is used by game.py's update.
	This just checks if an object is in bounds and moves the object using its velocity.
	
check_bounds(self)
	
	Keeps the object in the screen so it doesn't run away.
	
collision(self, other)

	Returns if there is a collision or not.
	
handle_collision(self,other)

	This returns what the objects will do if a collision is encountered.
	In general, I put it that it would not overlap with other.
	

============PLAYER.PY============

update(self, dt):
	
	In this update, this is where the movement and the event handling of 
	key presses happen. This is where the velocity is set as well. 
	That's why you can see the square moving around "smoothly."
	
Similarly to player.py, finish.py and block.py inherit from physicalobject.py and 
has the update and collision properties.

Modify, delete, add anything you want as long as you can go from one level to the next.
The rest is up to you.


============SETTINGS.PY============

All the global variables are stored here

Good Luck :-)


