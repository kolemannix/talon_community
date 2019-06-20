"""
"""

from talon.voice import Context, Key, press
from ..utils import text, numeral_list, extract_num_from_m
import time

ctx = Context("general_lang")
ctx.set_list("n", numeral_list)

def back_n(m):
    n = extract_num_from_m(m, 1)
    if n > 10:
        n = 10

    for i in range(0, n):
        press("backspace")
        time.sleep(0.025)

ctx.keymap(
    {
        # Vim-like Editor
        # "debug line": ["Idbg!(", Key("esc"), "$i)", Key("esc"), "0e"],
        "fix me [<dgndictation>]": ["// FIXME: ", text],
        "to do [<dgndictation>]": ["// TODO: ", text],
        "line down": "o",
        "line up": "O",
        "jump up": Key("ctrl-u"),
        "jump down": Key("ctrl-d"),
        "redo": Key("ctrl-r"),
        "bubble [{general_lang.n}]": back_n,
        "dupe": "yyp",
        "args": ["()", Key("left")],
        # combos
        "spamma": ", ",
        "sinker": [Key("cmd-right ;")],
        "coal space": ": ",
        # Operators
        "(op equals | assign)": " = ",
        "op (minus | subtract)": " - ",
        "op (plus | add)": " + ",
        "(op times | multiply)": " * ",
        "op divide": " / ",
        "op mod": " % ",
        "coleek": " := ",
        "op greater than": " > ",
        "op less than": " < ",
        "op equals": " == ",
        "op not equal": " != ",
        "((op | is) greater [than] or equal [to] | grayqual)": " >= ",
        "((op | is) less [than] or equal [to] | lessqual)": " <= ",
        "([(op | is)] not exactly (equal [to] | equals) | ranqual | nockle)": " !== ",
        "(op (power | exponent) | to the power [of])": " ** ",
        "op and": " && ",
        "op or": " || ",
        "[op] (logical | bitwise) and": " & ",
        "([op] (logical | bitwise) or | (op | D) pipe)": " | ",
        "(op | logical | bitwise) and equals": " &= ",
        "(op | logical | bitwise) or equals": " |= ",
        "(op | logical | bitwise) (ex | exclusive) or equals": " ^= ",
        "[(op | logical | bitwise)] (left shift | shift left) equals": " <<= ",
        "[(op | logical | bitwise)] (right shift | shift right) equals": " >>= ",
        "arrow": " -> ",
        "double arrow": " => ",
        # Completed matchables
        "empty (dict | object)": "{}",
        "(empty array | brackers)": "[]",
        # Blocks
        # "[brace] block": [" {}", Key("left enter enter up tab")],
        "(square | brax) block": ["[", Key("enter")],
        "(paren | prex) block": ["(", Key("enter")],
        # Combos
        "coalshock": [":", Key("enter")],
        "comshock": [",", Key("enter")],
        "[forward] slasher": "// ",
        # Statements
        "state (def | deaf | deft)": "def ",
        "state if": "if ",
        "state else if": [" else if ()", Key("left")],
        "state while": ["while ()", Key("left")],
        "state for": "for ",
        "state switch": ["switch ()", Key("left")],
        "state case": ["case \nbreak;", Key("up")],
        # Other Keywords
        "const": "const ",
        "static": "static ",
        "tip pent": "int ",
        "tip char": "char ",
        "tip byte": "byte ",
        "tip float": "float ",
        "tip double": "double ",
        # Comments
        "comment see": "// ",
        "comment py": "# ",
    }
)

