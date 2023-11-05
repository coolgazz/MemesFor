import telebot
from config import *
import random

TOKEN = '6654030191:AAEXpVIhrtWxtrgqZQAWPDQQvSwSblPn0bs'
bot = telebot.TeleBot(TOKEN)
WIDTH, HEIGHT = 10, 10
snake = [(1, 1)]
food = (random.randint(1, WIDTH), random.randint(1, HEIGHT))
direction = "RIGHT"

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global snake, food, direction

    user_input = message.text.lower()
    if user_input == "w":
        direction = "UP"
    elif user_input == "s":
        direction = "DOWN"
    elif user_input == "a":
        direction = "LEFT"
    elif user_input == "d":
        direction = "RIGHT"

    move_snake()

    if snake[0] == food:
        snake.append(snake[-1])
        food = (random.randint(1, WIDTH), random.randint(1, HEIGHT))

    if is_game_over():
        bot.send_message(message.chat.id, "Игра окончена. Начните заново.")
        snake.clear()
        snake.append((1, 1))
        food = (random.randint(1, WIDTH), random.randint(1, HEIGHT))
        direction = "RIGHT"

    display_game(message.chat.id)

def move_snake():
    head_x, head_y = snake[0]
    if direction == "UP":
        new_head = (head_x, head_y - 1)
    elif direction == "DOWN":
        new_head = (head_x, head_y + 1)
    elif direction == "LEFT":
        new_head = (head_x - 1, head_y)
    elif direction == "RIGHT":
        new_head = (head_x + 1, head_y)
    snake.insert(0, new_head)
    snake.pop()

def is_game_over():
    head_x, head_y = snake[0]
    return (
        head_x < 1
        or head_x > WIDTH
        or head_y < 1
        or head_y > HEIGHT
        or len(snake) != len(set(snake))
    )

def display_game(chat_id):
    gameboard = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for x, y in snake:
        game_board[y - 1][x - 1] = "O"
    x, y = food
    game_board[y - 1][x - 1] = "X"

    game_text = "\n".join([" ".join(row) for row in game_board])
    bot.send_message(chat_id, game_text)

if __name__ == '__main__':
    bot.polling(True)