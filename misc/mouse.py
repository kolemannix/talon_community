# from https://github.com/talonvoice/examples
# jsc added shift-click, command-click, and voice code compatibility

# import eye
import time
from talon import ctrl, tap, ui
from talon.voice import Context

ctx = Context("mouse")

x, y = ctrl.mouse_pos()
mouse_history = [(x, y, time.time())]
force_move = None


def on_move(typ, e):
    mouse_history.append((e.x, e.y, time.time()))
    if force_move:
        e.x, e.y = force_move
        return True


tap.register(tap.MMOVE, on_move)


def click_pos(m):
    word = m._words[0]
    start = (word.start + min((word.end - word.start) / 2, 0.100)) / 1000.0
    diff, pos = min([(abs(start - pos[2]), pos) for pos in mouse_history])
    return pos[:2]


def delayed_click(m, button=0, times=1):
    # old = eye.config.control_mouse
    # eye.config.control_mouse = False
    # x, y = click_pos(m)
    # ctrl.mouse(x, y)
    ctrl.mouse_click(x, y, button=button, times=times, wait=16000)
    # time.sleep(0.032)
    # eye.config.control_mouse = old


# jsc added
def press_key_and_click(m, key, button=0, times=1):
    ctrl.key_press(key, down=True)
    ctrl.mouse_click(x, y, button=button, times=times, wait=16000)
    ctrl.key_press(key, up=True)


# jsc added
def shift_click(m, button=0, times=1):
    press_key_and_click(m, "shift", button, times)


def command_click(m, button=0, times=1):
    press_key_and_click(m, "cmd", button, times)


def delayed_right_click(m):
    delayed_click(m, button=1)


def delayed_dubclick(m):
    delayed_click(m, button=0, times=2)


def delayed_tripclick(m):
    delayed_click(m, button=0, times=3)


def mouse_scroll(amount):
    def scroll(m):
        delta = 1 if amount > 0 else -1
        for i in range(0, abs(amount)):
            ctrl.mouse_scroll(y=delta)
    return scroll

def mouse_drag(m):
    x, y = click_pos(m)
    ctrl.mouse_click(x, y, down=True)


def mouse_release(m):
    x, y = click_pos(m)
    ctrl.mouse_click(x, y, up=True)


def mouse_center(m):
    win = ui.active_window()
    rect = win.rect
    center = (rect.x + rect.width / 2, rect.y + rect.height / 2)
    print(rect, center)
    ctrl.mouse_move(*center)


keymap = {
    # jsc modified with some voice-code compatibility
    "click right": delayed_right_click,
    "click [left]": delayed_click,
    "click double": delayed_dubclick,
    "click triple": delayed_tripclick,
    "click drag": mouse_drag,
    "click release": mouse_release,
    "click shift": shift_click,
    "click command": command_click,
    "scroll down": mouse_scroll(300),
    "scroll up": mouse_scroll(-300),
    "scroll down big": mouse_scroll(600),
    "scroll up big": mouse_scroll(-600),
    "mouse center": mouse_center,
}

ctx.keymap(keymap)
