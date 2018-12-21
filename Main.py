import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.SKY_BLUE)

    def setup(self):
        # Set up your game here
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        #---------------------------------------------------------------------------------------------------------------
        # Your drawing code goes here
        #---------------------------------------------------------------------------------------------------------------
        arcade.finish_render()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass



def Main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "New World")
    game.setup()
    arcade.run()


Main()
