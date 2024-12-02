import time
import os

game_map = [
    "......................................",
    ".                                    .",
    ".                                    .",
    ".                                    .",
    ".                                    .",
    ".                                    .",
    ".                                    .",
    "......................................"
]

player_pos = [1, 1]

figures = {
    (2, 5): {"char": "x", "text": "The horizon ends where it begins."},
    (4, 16): {"char": "y", "text": "What you seek is beyond form."},
    (6, 28): {"char": "z", "text": "Do you feel the void calling?"},
}

end_game_position = [7, 34]

talked_to_figures = set()
steps_after_third_figure = 0

color_reset = "\033[0m"
color_red = "\033[31m"
color_yellow = "\033[33m"
color_gray = "\033[90m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def render_map():
    clear_screen()
    for r, row in enumerate(game_map):
        row_str = list(row)
        if r == player_pos[0]:
            row_str[player_pos[1]] = f"{color_red}i{color_reset}"
        for pos, figure in figures.items():
            if r == pos[0] and pos != tuple(player_pos):
                row_str[pos[1]] = f"{color_yellow}{figure['char']}{color_reset}"
        print("".join(row_str))
    print("\nMove with W/A/S/D, or Q to quit.\n")

while True:
    render_map()
    move = input("Enter your move: ").lower()

    if move == 'q':
        print(f"{color_gray}You fade into nothingness. Goodbye.{color_reset}")
        break

    new_pos = player_pos[:]
    if move == 'w':
        new_pos[0] -= 1
    elif move == 's':
        new_pos[0] += 1
    elif move == 'a':
        new_pos[1] -= 1
    elif move == 'd':
        new_pos[1] += 1
    else:
        print("Invalid move. Try again.")
        time.sleep(1)
        continue

    if new_pos[0] < 0 or new_pos[0] >= len(game_map) or new_pos[1] < 0 or new_pos[1] >= len(game_map[0]):
        print(f"{color_gray}You can't move there!{color_reset}")
        time.sleep(1)
        continue

    if game_map[new_pos[0]][new_pos[1]] == '.':
        print(f"{color_gray}The void blocks your path.{color_reset}")
        time.sleep(1)
        continue

    player_pos = new_pos

    if tuple(player_pos) in figures and tuple(player_pos) not in talked_to_figures:
        figure = figures[tuple(player_pos)]
        talked_to_figures.add(tuple(player_pos))
        print(f"\n{color_yellow}{figure['char']} whispers: \"{figure['text']}\"{color_reset}")
        input("\n(Press Enter to continue)")

    if len(talked_to_figures) == 3:
        steps_after_third_figure += 1

    if steps_after_third_figure == 5:
        for _ in range(3):
            render_map()
            print(f"{color_gray}The void consumes you...{color_reset}")
            time.sleep(1)
        print("\nYou vanish into the void. The journey ends.")
        break
