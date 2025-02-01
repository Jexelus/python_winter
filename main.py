import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100) 

    sh, sw = stdscr.getmaxyx()

    snowflakes = []

    snow_heights = [sh - 2] * sw 

    snake_length = 10 
    snake_body = [] 
    snake_x = sw // 2  
    snake_y = snow_heights[snake_x] - 1  
    snake_direction = 1  

    for i in range(snake_length):
        snake_body.append([snake_y, snake_x - i])

    while True:
        stdscr.clear()

        if random.random() < 0.25: 
            snowflakes.append([0, random.randint(1, sw - 2)])

        new_snowflakes = []
        for flake in snowflakes:
            flake[0] += 1  
            if flake[0] < snow_heights[flake[1]]: 
                new_snowflakes.append(flake)
            else:
                if snow_heights[flake[1]] > 1: 
                    snow_heights[flake[1]] -= 1

        for flake in new_snowflakes:
            stdscr.addch(flake[0], flake[1], '*')

        for col in range(sw):
            for row in range(snow_heights[col], sh - 1):
                stdscr.addch(row, col, '#') 

        snowflakes = new_snowflakes

        snake_x += snake_direction

        if snake_x >= sw - 1 or snake_x <= 0:
            snake_direction *= -1  

        snake_y = snow_heights[snake_x] - 1

        snake_body.insert(0, [snake_y, snake_x])

        if len(snake_body) > snake_length:
            snake_body.pop()

        for i, segment in enumerate(snake_body):
            if i == 0: 
                head_symbol = '>' if snake_direction == 1 else '<'
                stdscr.addch(segment[0], segment[1], head_symbol)
            else: 
                stdscr.addch(segment[0], segment[1], '=')

        stdscr.refresh()

        time.sleep(0.08)

if __name__ == "__main__":
    curses.wrapper(main)