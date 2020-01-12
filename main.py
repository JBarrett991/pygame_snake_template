import pygame
import sys

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800


class Game:

    def __init__(self):
        # load and initialize all pygame modules
        pygame.init()

        # create the window
        self.win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # set max frame rate
        self.max_fps = 20
        # create clock that will track the frame rate
        self.clock = pygame.time.Clock()

        # begin main game loop
        self.main()

    def main(self):
        while True:
            for event in pygame.event.get():
                # pygame.QUIT is the x in the corner of the window that allows you to close the window
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_UP:
                        print("you pressed the up arrow key")
                        # the up arrow key was pressed
                        pass

            # position of the rectangle when drawn
            x = 40
            y = 100

            # size of the rectangle when drawn
            width = 20
            height = 80

            # draw calls
            # fill the window with black
            self.win.fill((0, 0, 0))

            # draw rectangle
            pygame.draw.rect(self.win,  # tell which window to draw in
                             (255, 0, 0),  # color, RGB
                             (x,  # x coordinate
                              y,  # y coordinate
                              width,  # dimensions of the rectangle
                              height))

            # show what has been drawn in the window
            pygame.display.update()

            # tick, to tell the clock that one frame is complete
            self.clock.tick(self.max_fps)


if __name__ == "__main__":
    Game()
