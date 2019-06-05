from talon.voice import Context, Key

ctx = Context("symbol")

keymap = {
    # capital letters
    "goose": "G",
    # simple
    "(question [mark] | questo)": "?",
    "plus": "+",
    "tilde": "~",
    "(bang | exclamation point | clamor)": "!",
    "(dollar [sign] | dolly)": "$",
    "(downscore | crunder | down score)": "_",
    "colon": ":",
    "(paren | left paren | open paren )": "(",
    "(R paren | close paren | right paren)": ")",
    "(brace | left brace | open brace)": "{",
    "(closing brace | right brace | close brace)": "}",
    "(angle | left angle | less than)": "<",
    "(rangle | are angle | right angle | greater than)": ">",
    "(star | asterisk)": "*",
    "(pound | hash [sign] | octo | number sign)": "#",
    "(percent | mod)": "%",
    "caret": "^",
    "at sign": "@",
    "(and sign | ampersand | amper)": "&",
    "(pipe | spike)": "|",
    "(dubquote | double quote | quatches)": '"',
    # compound
    "mintwice": "--",
    "plustwice": "++",
    "minquall": "-=",
    "pluqual": "+=",
    "starqual": "*=",
    "triple quote": "'''",
    "triple tick": "```",
    "[forward] dubslash": "//",
    "coal twice": "::",
    "(dot dot | dotdot)": "..",
    "(ellipsis | dot dot dot | dotdotdot)": "...",
    # unnecessary: use repetition commands?
}

ctx.keymap(keymap)
