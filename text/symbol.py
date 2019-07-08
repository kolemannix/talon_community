from talon.voice import Context, Key

ctx = Context("symbol")

keymap = {
    # capital letters
    "goose": "G",
    "Frank": "F",
    # simple
    "(question [mark] | questo)": "?",
    "plus": "+",
    "tilde": "~",
    "(bang | exclamation point | clamor)": "!",
    "(dollar [sign] | dolly)": "$",
    "(downscore | crunder | down score)": "_",
    "colon": ":",
    "(hug | left hug | open hug)": "(",
    "(close hug | right hug | R hug)": ")",
    "(brace | left brace | open brace)": "{",
    "(shut brace | right brace | close brace)": "}",
    "(angle | left angle | less than)": "<",
    "(rangle | close angle | right angle | greater than)": ">",
    "(star | asterisk)": "*",
    "(pound | hash [sign] | octo | number sign)": "#",
    "(percent | mod)": "%",
    "caret": "^",
    "at sign": "@",
    "(and sign | ampersand | amper)": "&",
    "(pipe | spike)": "|",
    "(dubquote | double quote | quote)": '"',
    # compound
    "triple quote": "'''",
    "triple tick": "```",
    "[forward] dubslash": "//",
    "coal twice": "::",
    "(ellipsis | dot dot dot | dotdotdot)": "...",
    # unnecessary: use repetition commands?
}

ctx.keymap(keymap)
