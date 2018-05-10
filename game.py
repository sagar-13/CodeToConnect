import pyglet
import os, platform

#Import globals
import settings

#Import other objects too 
import player, finish, block

#Size of the window screen
window = pyglet.window.Window(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)

#Collection of sprites to be populated and drawn later
main_batch = pyglet.graphics.Batch()

key = pyglet.window.key

#Initializing the event stack size
event_stack_size = 0


def init():
    '''
        Initializes global variables.
    '''
    # Global variables, make sure all objects are global
    # pl, fin, blo are the player, finishing point and blocks
    # More about the properties of each object can be found in respective .py files
    global p1, fin, blo, game_objects, event_stack_size
    
    # Iterates through the stack size and makes sure there aren't any handlers leftover
    while event_stack_size > 0:
        game_window.pop_handlers()
        event_stack_size -= 1

    # Where objects get initiated
    p1 = player.Player(x=400, y=300, batch=main_batch)
    # fin = finish.Finish(x=50, y=500, batch=main_batch)
    # blo = block.Block(x=500, y=200, batch=main_batch)

    def squaremaker(x,y,game_objects):

        for i in range(x,x+150,50):
            game_objects.append(block.Block(x=i, y=y, batch=main_batch))
            game_objects.append(finish.Finish(x=x+50, y=y+50, batch=main_batch))
            

        for i in range (y,y+150,50):
            game_objects.append(block.Block(x=x, y=i, batch=main_batch))

        for i in range(x,x+150,50):
            game_objects.append(block.Block(x=i, y=y+100, batch=main_batch))
        
        for i in range (y,y+150,50):
            game_objects.append(block.Block(x=x+100, y=i, batch=main_batch))


    # Add other objects here to
    game_objects = [p1]

    squaremaker(50,50, game_objects)
    squaremaker(200,200, game_objects)
    squaremaker(350,350, game_objects)
    squaremaker(500,200, game_objects)
    squaremaker(650,50, game_objects)

    

    # squaremaker(500,500, game_objects)


    

  

        



    for obj in game_objects:
        for handler in obj.event_handlers:
            window.push_handlers(handler)
            event_stack_size += 1


# You shouldn't really need to change this
@window.event
def on_draw():
    '''
        Clears the window of previous drawn sprites and then redraws them depending on the update.
    '''
    window.clear()  
    main_batch.draw()

def update(dt):
    '''
        Checks if it collides, with the object and then further calls each objects own updates.
        
        Special object called finish.Finish that upon being collided with would execute a command
        that would close the current level and go to the next level.
        
        game_objects - a list of all the objects
        dt - delay time in seconds
        player.Player, finsih.Finish - The object type that was imported
    '''
    for i in range(len(game_objects)):
        for j in range(i + 1, len(game_objects)):

            obj_1 = game_objects[i]
            obj_2 = game_objects[j]

            if obj_1.collision(obj_2):
                if((type(obj_1) == finish.Finish or type(obj_1) == player.Player) and
                   (type(obj_2) == finish.Finish or type(obj_2) == player.Player)):
                    
                    # This goes to the next level/game it closes the current window and opens
                    # the file of the next person/groups game.
                    window.close()
                    if platform.system() == "Windows":
                        os.system("py ../" + NEXT_GROUP + "/game.py")
                    else:
                        os.system("python ../" + NEXT_GROUP + "/game.py")
                obj_1.handle_collision(obj_2)
    
    #Updates every object from the initialized list
    for obj in game_objects:
        obj.update(dt)
  
if __name__ == "__main__":
    # Initializing Player and other objects
    init()
    # Update the game 120 times per second (fps)
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    # Tell pyglet to do its thing
    pyglet.app.run()




