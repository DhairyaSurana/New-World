import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.player_list = None
        self.wall_list = None

        self.player_sprite = None
        self.wall_sprite = None

        self.physics_engine = None
        self.background = None

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("test_sprite_up.png", 0.2)
        self.wall_sprite = arcade.Sprite("wooden_wall.jpg", 0.2)

        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2

        self.player_list.append(self.player_sprite)

        # -- Set up the walls
        # Create a row of boxes
        for x in range(173, 650, 64):
            wall = arcade.Sprite("wooden_wall.jpg", 0.3)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)

        # Create a column of boxes
        for y in range(273, 500, 64):
            wall = arcade.Sprite("wooden_wall.jpg", 0.3)
            wall.center_x = 465
            wall.center_y = y
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list)

        self.background = arcade.load_texture("grass.png")

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED

        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED

        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED

        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.wall_list.draw()
        self.player_list.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "New World")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

