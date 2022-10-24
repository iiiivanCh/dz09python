from telegram import Update
from telegram.ext import CallbackContext
import random

from spy_log import *


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text('Игра человек против человека: КРЕСТИКИ - НОЛИКИ\n'
                              '/go - начало игры\n'
                              '/st - следующий ход. '
                              'Необходимо вызвать команду /st и через пробел - номер поля (например: /st 5) '
                              'куда игрок желает сделать ход')


boards = [1, 2, 3, 4, 5, 6, 7, 8, 9]
flag = True


victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


def get_print_boards(update: Update):
    update.message.reply_text(f"{boards[0]} {boards[1]} {boards[2]}\n"
                              f"{boards[3]} {boards[4]} {boards[5]}\n"
                              f"{boards[6]} {boards[7]} {boards[8]}")


def get_result():
    p = ''
    for i in victories:
        if boards[i[0]] == 'X' and boards[i[1]] == 'X' and boards[i[2]] == 'X':
            p = 'X'
        if boards[i[0]] == 'O' and boards[i[1]] == 'O' and boards[i[2]] == 'O':
            p = 'O'
    return p


def st_command(update: Update, context: CallbackContext):
    log(update, context)
    global boards
    global flag
    if flag == True:
        sign = 'X'
        go = update.message.text
        step = int(go[4])
    else:
        sign = 'O'
        go = update.message.text
        step = int(go[4])
    i = boards.index(step)
    boards[i] = sign
    v = get_result()
    if v == '':
        flag = not (flag)
        get_print_boards(update)
        return
    if v == 'X':
        update.message.reply_text('Победил игрок 1')
        get_print_boards(update)
        boards = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    else:
        update.message.reply_text('Победил игрок 2')
        get_print_boards(update)
        boards = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def go_command(update: Update, context: CallbackContext):
    log(update, context)
    global flag
    game_over = False
    first_second = random.randint(1, 100)
    if first_second % 2 == 0:
        update.message.reply_text('Игру начинает игрок 1')
        flag = True
        get_print_boards(update)
    else:
        update.message.reply_text('Игру начинает игрок 2')
        flag = False
        get_print_boards(update)
