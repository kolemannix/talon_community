import time

from talon.voice import Key, Context, Str, press
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
from talon import ctrl, ui

from ..utils import parse_words, text, is_in_bundles, insert, load_config_json
from ..misc.switcher import switch_app
from ..bundle_groups import TERMINAL_BUNDLES

# TODO: move application specific commands into their own files: apt-get, etc

ctx = Context("terminal", func=is_in_bundles(TERMINAL_BUNDLES))

mapping = {"semicolon": ";", r"new-line": "\n", r"new-paragraph": "\n\n"}


def parse_word(word):
    word = word.lstrip("\\").split("\\", 1)[0]
    word = mapping.get(word, word)
    return word


def dash(m):
    words = parse_words(m)
    press(" ")
    if len(words) == 1 and len(words[0]) == 1:
        press("-")
        Str(words[0])(None)
    else:
        if words == ["michelle"]:
            words = ["shell"]
        press("-")
        press("-")
        Str("-".join(words))(None)


KUBERNETES_PREFIX = "(cube | cube control)"

directory_shortcuts = {
    "up": "..",
    "up up": "../..",
    "up up up": "../../..",
    "up up up up": "../../../..",
    "up up up up up": "../../../../..",
    "home": "~",
    "talon home": TALON_HOME,
    "talon user": TALON_USER,
    "talon plug-ins": TALON_PLUGINS,
    "talon community": "~/.talon/user/talon_community",
}

def cd_directory_shortcut(m):
    directory = directory_shortcuts[m[1]]
    insert(f"cd {directory}; ls")
    for _ in range(4):
        press("left")


def name_directory_shortcuts(m):
    insert(directory_shortcuts[" ".join(m["terminal.directory_shortcuts"])])


servers = load_config_json("servers.json")


def get_server(m):
    return servers[" ".join(m["global_terminal.servers"])]


def mosh_servers(m):
    insert(f"mosh {get_server(m)}")


def ssh_servers(m):
    insert(f"ssh {get_server(m)}")


def name_servers(m):
    insert(get_server(m))


def ssh_copy_id_servers(m):
    insert(f"ssh-copy-id {get_server(m)}")


def new_server(m):
    press("cmd-d")
    insert(f"ssh {get_server(m)}")
    press("enter")


keymap = {
    "shell Whereami": "pwd ",
    "shell home": "~/",
    "lefty": Key("home"),
    "ricky": Key("end"),
    "clear back": Key("ctrl-u"),
    "clear line": [Key("ctrl-e"), Key("ctrl-u")],
    "(pain new | split vertical)": Key("cmd-d"),
    "new {global_terminal.servers}": new_server,
    # talon
    "tail talon": "tail -f ~/.talon/talon.log",
    "talon reple": "~/.talon/bin/repl",
    # some habits die hard
    "troll char": Key("ctrl-c"),
    "cd": ["cd ; ls", Key("left"), Key("left"), Key("left"), Key("left")],
    "cd wild": [
        "cd **; ls",
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
    ],
    "cd wild [<dgndictation>]": [
        "cd **; ls",
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
        text,
    ],
    "cd {terminal.directory_shortcuts}": cd_directory_shortcut,
    "directory {terminal.directory_shortcuts}": name_directory_shortcuts,
    "(LS | run ellis | run alice)": "ls\n",
    "(la | run la)": "ls -la\n",
    # "durrup": "cd ..; ls\n",
    "pseudo": "sudo ",
    "(redo pseudo | pseudo [make me a] sandwich)": [
        Key("up"),
        Key("ctrl-a"),
        "sudo ",
        Key("enter"),
    ],
    "shell C H mod": "chmod ",
    "shell clear": Key("ctrl-l"),
    "shell copy [<dgndictation>]": ["cp ", text],
    "shell copy (recursive | curse) [<dgndictation>]": ["cp -r", text],
    "shell kill": Key("ctrl-c"),
    "shell list [<dgndictation>]": ["ls ", text],
    "shell list all [<dgndictation>]": ["ls -la ", text],
    "shell make (durr | dear | directory) [<dgndictation>]": ["mkdir ", text],
    "shell move [<dgndictation>]": ["mv ", text],
    "shell cat [<dgndictation>]": ["cat ", text],
    "shell X args [<dgndictation>]": ["xargs ", text],
    "shell mosh": "mosh ",
    "[shell] mosh {global_terminal.servers}": mosh_servers,
    "[shell] S S H {global_terminal.servers}": ssh_servers,
    # "shell server {terminal.servers}": name_servers,
    "[shell] S S H copy I D {global_terminal.servers}": ssh_copy_id_servers,
    "shell M player": "mplayer ",
    "shell nvidia S M I": "nvidia-smi ",
    "shell R sync": "./src/dotfiles/sync_rsync ",
    "shell tail": "tail ",
    "shell tail follow": "tail -f ",
    "shall count lines": "wc -l ",
    "shell L S U S B": "lsusb",
    # python
    "create virtual environment": ["virtualenv -p python3 venv", Key("enter")],
    "activate virtual environment": [
        "source `find . | grep bin/activate$`",
        Key("enter"),
    ],
    # Tools
    # "(grep | grip)": ["grep  .", Key("left left")],
    "(grep | grip)": "grep ",
    # "gripper": ["grep -r  .", Key("left left")],
    "pee socks": "ps aux ",
    "vi": "vi ",
    # kubectl
    KUBERNETES_PREFIX + "control": "kubectl ",
    KUBERNETES_PREFIX + "create": "kubectl create ",
    KUBERNETES_PREFIX + "expose": "kubectl expose ",
    KUBERNETES_PREFIX + "run": "kubectl run ",
    KUBERNETES_PREFIX + "set": "kubectl set ",
    KUBERNETES_PREFIX + "run-container": "kubectl run-container ",
    KUBERNETES_PREFIX + "get": "kubectl get ",
    KUBERNETES_PREFIX + "explain": "kubectl explain ",
    KUBERNETES_PREFIX + "edit": "kubectl edit ",
    KUBERNETES_PREFIX + "delete": "kubectl delete ",
    KUBERNETES_PREFIX + "rollout": "kubectl rollout ",
    KUBERNETES_PREFIX + "rolling-update": "kubectl rolling-update ",
    KUBERNETES_PREFIX + "scale": "kubectl scale ",
    KUBERNETES_PREFIX + "autoscale": "kubectl autoscale ",
    KUBERNETES_PREFIX + "certificate": "kubectl certificate ",
    KUBERNETES_PREFIX + "cluster-info": "kubectl cluster-info ",
    KUBERNETES_PREFIX + "top": "kubectl top ",
    KUBERNETES_PREFIX + "cordon": "kubectl cordon ",
    KUBERNETES_PREFIX + "uncordon": "kubectl uncordon ",
    KUBERNETES_PREFIX + "drain": "kubectl drain ",
    KUBERNETES_PREFIX + "taint": "kubectl taint ",
    KUBERNETES_PREFIX + "describe": "kubectl describe ",
    KUBERNETES_PREFIX + "logs": "kubectl logs ",
    KUBERNETES_PREFIX + "attach": "kubectl attach ",
    KUBERNETES_PREFIX + "exec": "kubectl exec ",
    KUBERNETES_PREFIX + "port-forward": "kubectl port-forward ",
    KUBERNETES_PREFIX + "proxy": "kubectl proxy ",
    KUBERNETES_PREFIX + "cp": "kubectl cp ",
    KUBERNETES_PREFIX + "auth": "kubectl auth ",
    KUBERNETES_PREFIX + "apply": "kubectl apply ",
    KUBERNETES_PREFIX + "patch": "kubectl patch ",
    KUBERNETES_PREFIX + "replace": "kubectl replace ",
    KUBERNETES_PREFIX + "convert": "kubectl convert ",
    KUBERNETES_PREFIX + "label": "kubectl label ",
    KUBERNETES_PREFIX + "annotate": "kubectl annotate ",
    KUBERNETES_PREFIX + "completion": "kubectl completion ",
    KUBERNETES_PREFIX + "api": "kubectl api ",
    KUBERNETES_PREFIX + "config": "kubectl config ",
    KUBERNETES_PREFIX + "help": "kubectl help ",
    KUBERNETES_PREFIX + "plugin": "kubectl plugin ",
    KUBERNETES_PREFIX + "version": "kubectl version ",
    KUBERNETES_PREFIX
    + "shell": ["kubectl exec -it  -- /bin/bash"]
    + [Key("left")] * 13,
    # tmux
    "mux attach [<dgndictation>]": ["tmuxre ", text],
    "mux": Key("ctrl-a"),
    "mux vertical": [Key("ctrl-a"), "|"],
    "mux horizontal": [Key("ctrl-a"), "-"],
    "mux up": [Key("ctrl-a"), "k"],
    "mux down": [Key("ctrl-a"), "j"],
    "mux left": [Key("ctrl-a"), "h"],
    "mux right": [Key("ctrl-a"), "l"],
    "mux next": [Key("ctrl-a"), "n"],
    "mux max": [Key("ctrl-a"), "z"],
    "mux new": [Key("ctrl-a"), "c"],
    "mux scroll": [Key("ctrl-a"), "a"],
    "SBT [<dgndictation>]": ["sbt ", text],
    # "tee mucks": "tmux ",
    # "T hello": "tmux ",
    # "T mux list": "tmux ls",
    # "T mux attach [<dgndictation>]": ["tmux a -t ", text],
    # "T mux scroll": [Key("ctrl-b"), Key("[")],
    # other
    "shell make": "make\n",
    "shell jobs": "jobs\n",
}

for action in ("get", "delete", "describe"):
    for object in (
        "nodes",
        "jobs",
        "pods",
        "namespaces",
        "services",
        "events",
        "deployments",
        "replicasets",
        "",
    ):
        if object:
            object = object + " "
        command = f"{KUBERNETES_PREFIX} {action} {object}"
        typed = f"kubectl {action} {object}"
        keymap.update({command: typed})

keymap.update({"(pain | bang) " + str(i): Key("alt-" + str(i)) for i in range(10)})

ctx.keymap(keymap)
ctx.set_list("directory_shortcuts", directory_shortcuts.keys())
# ctx.set_list("servers", servers.keys())


def shell_rerun(m):
    # switch_app(name='iTerm2')
    app = ui.apps(bundle="io.alacritty")[0]
    ctrl.key_press("c", ctrl=True, app=app)
    time.sleep(0.05)
    ctrl.key_press("up", app=app)
    ctrl.key_press("enter", app=app)

global_ctx = Context("global_terminal")
global_ctx.keymap(
    {
        "shell rerun": shell_rerun,
    }
)
