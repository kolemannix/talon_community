from talon import app, webview, ui
from talon.engine import engine
from talon_init import TALON_HOME

hist_len = 6

template = '''
<style type="text/css">
body {
    width: 400px;
    padding: 0;
    margin: 0;
}
.contents, table, h3 {
    width: 100%;
}
table {
    table-layout: fixed;
}
td {
    overflow-wrap: normal;
    word-wrap: normal;
    text-align: left;
    margin: 0;
    padding: 0;
    padding-left: 5px;
    padding-right: 5px;
}
.text {
    font-weight: normal;
    font-style: italic;
}
#title {
    padding-right: 5px; /* this is broken */
    min-width: 100px;
}
</style>

<h3 id="title">History</h3>
<table>
{% for phrase in phrases %}
<tr><td class="phrase">{{ phrase }}</td></tr>
{% endfor %}
<tr><td><i>{{ hypothesis }}</i></td></tr>
</ul>
'''

webview = webview.Webview()
webview.render(template, phrases=['command'])
webview.show()
webview.move(1, ui.main_screen().height)

class History:
    def __init__(self):
        self.history = []
        engine.register('post:phrase', self.on_phrase_post)

    def parse_phrase(self, phrase):
        return ' '.join(word.split('\\')[0] for word in phrase)

    def on_phrase_post(self, j):
        phrase = self.parse_phrase(j.get('phrase', []))
        cmd = j['cmd']
        if cmd == 'p.end' and phrase:
            self.history.append(phrase)
            self.history = self.history[-hist_len:]
            webview.render(template, phrases=self.history)

history = History()
