# https://github.com/JonathanNickerson/talon_voice_user_scripts

import time

import talon.clip as clip
from talon.voice import Key, press, Str, Context
from ..utils import (
    parse_words,
    join_words,
    is_not_vim,
    numeral_list,
    extract_num_from_m,
)

ctx = Context("generic_editor", func=is_not_vim)
ctx.set_list("n", numeral_list)


def find_next(m):
    press("cmd-f")
    Str(str(m.dgndictation[0]._words[0]))(None)
    press("escape")


def find_previous(m):
    press("left")
    press("cmd-f")
    Str(str(m.dgndictation[0]._words[0]))(None)
    press("cmd-shift-g")
    press("escape")


# jcooper-korg from talon slack
def select_text_to_left_of_cursor(m):
    words = parse_words(m)
    if not words:
        return
    old = clip.get()
    key = join_words(words).lower()
    press("shift-home", wait=2000)
    press("cmd-c", wait=2000)
    press("right", wait=2000)
    text_left = clip.get()
    clip.set(old)
    result = text_left.find(key)
    if result == -1:
        return
    # cursor over to the found key text
    for i in range(0, len(text_left) - result):
        press("left", wait=0)
    # now select the matching key text
    for i in range(0, len(key)):
        press("shift-right")


# jcooper-korg from talon slack
def select_text_to_right_of_cursor(m):
    words = parse_words(m)
    if not words:
        return
    key = join_words(words).lower()
    old = clip.get()
    press("shift-end", wait=2000)
    press("cmd-c", wait=2000)
    press("left", wait=2000)
    text_right = clip.get()
    clip.set(old)
    result = text_right.find(key)
    if result == -1:
        return
    # cursor over to the found key text
    for i in range(0, result):
        press("right", wait=0)
    # now select the matching key text
    for i in range(0, len(key)):
        press("shift-right")


alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789_"


def big_word_neck(m):
    return word_neck(m, valid_characters=set(alphanumeric) | set("/\\-_.>=<"))


def word_neck(m, valid_characters=alphanumeric):
    word_index = extract_num_from_m(m, 1)

    old = clip.get()
    press("shift-right", wait=2000)
    press("cmd-c", wait=2000)
    press("shift-left", wait=2000)
    current_highlight = clip.get()
    if len(current_highlight) > 1:
        press("right", wait=2000)
    press("shift-end", wait=2000)
    time.sleep(0.25)
    press("cmd-c", wait=2000)
    press("left", wait=2000)
    time.sleep(0.25)
    text_right = clip.get().lower()
    clip.set(old)

    is_word = [character in valid_characters for character in text_right]
    word_count = 1
    i = 0
    while i < (len(is_word) - 1) and not is_word[i]:
        i += 1

    # print("a start", i)

    while i < (len(is_word) - 1) and word_count < word_index:
        # print(i, is_word[i], word_count, word_index)
        if not is_word[i] and is_word[i + 1]:
            word_count += 1
        i += 1
    # warning: this is a hack, sorry
    # print("i", i)
    if i == 1 and is_word[0]:
        i = 0
    start_position = i
    # print(text_right[start_position:])
    while i < len(is_word) and is_word[i]:
        i += 1
    end_position = i

    # print(start_position, end_position)
    # cursor over to the found word
    for i in range(0, start_position):
        press("right", wait=0)
    # now select the word
    for i in range(0, end_position - start_position):
        press("shift-right")


def big_word_prev(m):
    return word_prev(m, valid_characters=set(alphanumeric) | set("/\\-_.>=<"))


def word_prev(m, valid_characters=alphanumeric):
    word_index = extract_num_from_m(m, 1)

    old = clip.get()
    press("shift-right", wait=2000)
    press("cmd-c", wait=2000)
    press("shift-left", wait=2000)
    current_highlight = clip.get()
    if len(current_highlight) > 1:
        press("left", wait=2000)
    press("shift-home", wait=2000)
    time.sleep(0.25)
    press("cmd-c", wait=2000)
    press("right", wait=2000)
    time.sleep(0.25)
    text_right = clip.get().lower()
    clip.set(old)

    text_right = list(reversed(text_right))

    is_word = [character in valid_characters for character in text_right]
    word_count = 1
    i = 0
    while i < (len(is_word) - 1) and not is_word[i]:
        i += 1

    while i < (len(is_word) - 1) and word_count < word_index:
        # print(i, is_word[i], word_count, word_index)
        if not is_word[i] and is_word[i + 1]:
            word_count += 1
        i += 1
    start_position = i
    # print(text_right[start_position:])
    while i < len(is_word) and is_word[i]:
        i += 1
    end_position = i

    # print(start_position, end_position, text_right[start_position:end_position])
    # cursor over to the found word
    for i in range(0, start_position):
        press("left", wait=0)
    # now select the word
    for i in range(0, end_position - start_position):
        press("shift-left")


def left_go(m):
    # Defaults to 1
    n = extract_num_from_m(m, 1)
    press_n("alt-left", n)

def right_go(m):
    # Defaults to 1
    n = extract_num_from_m(m, 1)
    press_n("alt-right", n)

def press_n(key, n):
    for i in range(0, n):
        press(key)

def delete_word_left(m):
    n = extract_num_from_m(m, 1)
    press_n("alt-backspace", n)
    

def delete_word_right(m):
    n = extract_num_from_m(m, 1)
    press_n("alt-delete", n)
def select_word_right(m):
    n = extract_num_from_m(m, 1)
    press_n("alt-shift-right", n)

def select_word_left(m):
    n = extract_num_from_m(m, 1)
    press_n("alt-shift-left", n)

ctx.keymap(
    {
        # meta
        "save it": Key("cmd-s"),
        "undo it": Key("cmd-z"),
        "redo it": Key("cmd-shift-z"),
        # clipboard
        "clip cut": Key("cmd-x"),
        "clip copy": Key("cmd-c"),
        "clip paste": Key("cmd-v"),
        # motions
        "go word left [{generic_editor.n}]": left_go,
        "go word right [{generic_editor.n}]": right_go,
        "go line after end": Key("cmd-right space"),
        "go line start": Key("cmd-left"),
        "go line end": Key("cmd-right"),
        "go line before end": Key("cmd-right left"),
        # insertions
        "([insert] line break | sky turn)": Key("shift-enter"),
        # "([insert] new line below | slap)": Key("cmd-right enter"),
        "([insert] new line above | shocker)": Key("ctrl-a cmd-left enter up"),
        "([insert] duplicate line | jolt)": Key(
            "ctrl-a cmd-left shift-down cmd-c down cmd-v"
        ),
        # deleting
        "delete around this": Key("backspace delete"),
        "(delete line left | snip left)": Key("shift-cmd-left delete"),
        "(delete line right | snip right)": Key("shift-cmd-right delete"),
        "(delete [this] line)": Key("shift-cmd-right delete delete ctrl-a cmd-left"),
        "delete word left [{generic_editor.n}]": delete_word_left,
        "delete word right [{generic_editor.n}]": delete_word_right,
        "delete [this] word": Key("alt-backspace alt-delete"),
        # selecting
        "(select find right | crew) <dgndictation>": select_text_to_right_of_cursor,
        "(select find left | trail) <dgndictation>": select_text_to_left_of_cursor,
        "(select this word | word this)": Key("alt-right shift-alt-left"),
        "(select this line | shackle)": Key("cmd-right shift-cmd-left"),
        "(select above | shift home)": Key("shift-home"),
        "select up": Key("shift-up"),
        "select down": Key("shift-down"),
        "select all": Key("cmd-a"),
        "select left": Key("shift-left"),
        "select right": Key("shift-right"),
        "(select word number {generic_editor.n}* above | wordpreev {generic_editor.n}*)": word_prev,
        "big word preev {generic_editor.n}*": big_word_prev,
        "big word neck {generic_editor.n}*": big_word_neck,
        "(select word number {generic_editor.n}* below | wordneck {generic_editor.n}*)": word_neck,
        "select word left [{generic_editor.n}]": select_word_left, # Key("alt-shift-left"),
        "select word right [{generic_editor.n}]": select_word_right, # Key("alt-shift-right"),
        "select line left": Key("cmd-shift-left"),
        "select line right": Key("cmd-shift-right"),
    }
)
