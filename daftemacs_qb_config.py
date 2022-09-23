# daftemacs-qb - Emacs binding configuration for qutebrowser
#
# This configuration is based on qutemacs
# (https://gitlab.com/jgkamat/qutemacs/-/blob/master/qutemacs.py).
#
# Installation:
#
# 1. Copy this file or add this repo as a submodule to your dotfiles.
# 2. Add this line to your config.py, and point the path to this file:
# config.load_autoconfig()
# config.source('daftemacs-qb/daftemacs_qb_config.py')

""" Replace 'KeySequence.parse' with 'parse_daftemacs_qb' """

from PyQt5.QtGui import QKeySequence
from qutebrowser.utils import utils
from qutebrowser.keyinput.keyutils import _parse_keystring, KeySequence

@classmethod
def parse_daftemacs_qb(cls, keystr: str) -> 'KeySequence':
    """Parse a keystring like <Ctrl-x> or xyz and return a KeySequence."""
    new = cls()
    if keystr == '<Alt+Shift+>>':
        strings = ['alt+shift+>']
    elif keystr == '<Alt+Shift+<>':
        strings = ['alt+shift+<']
    else:
        strings = list(_parse_keystring(keystr))
    for sub in utils.chunk(strings, cls._MAX_LEN):
        sequence = QKeySequence(', '.join(sub))
        new._sequences.append(sequence)

    if keystr:
        assert new, keystr

    new._validate(keystr)
    return new

KeySequence.parse = parse_daftemacs_qb


#config = config  # type: ConfigAPI # noqa: F821 pylint: disable=E0602,C0103
#c = c  # type: ConfigContainer # noqa: F821 pylint: disable=E0602,C0103

""" Base """

c.confirm_quit = ['multiple-tabs', 'downloads']

""" tabs """

c.tabs.background = True
c.tabs.show = 'multiple'  # always, never, multiple, switching

""" completion """

c.completion.shrink = True

""" url """

c.url.start_pages = "https://www.google.com"
c.url.searchengines["DEFAULT"] = "https://www.google.com/search?q={}"
c.url.searchengines["Google"] = "https://www.google.com/search?q={}"
c.url.searchengines["DuckDuckGo"] = "https://duckduckgo.com/?q={}"

""" colors """

c.colors.tabs.bar.bg = '#282a36'
c.colors.tabs.indicator.error = '#ff5555'
c.colors.tabs.indicator.start = '#50fa7b'
c.colors.tabs.indicator.stop = '#282a36'
c.colors.tabs.even.bg = '#282a36'
c.colors.tabs.odd.bg = '#282a36'
c.colors.tabs.even.fg = '#888888'
c.colors.tabs.odd.fg = '#888888'
c.colors.tabs.selected.even.bg = '#bd93f9'
c.colors.tabs.selected.odd.bg = '#bd93f9'
c.colors.tabs.selected.even.fg = '#000000'
c.colors.tabs.selected.odd.fg = '#000000'
c.colors.tabs.pinned.even.bg = '#28803e'
c.colors.tabs.pinned.odd.bg = '#28803e'
c.colors.tabs.pinned.even.fg = '#000000'
c.colors.tabs.pinned.odd.fg = '#000000'
c.colors.tabs.pinned.selected.even.bg = '#50fa7b'
c.colors.tabs.pinned.selected.odd.bg = '#50fa7b'
c.colors.tabs.pinned.selected.even.fg = '#000000'
c.colors.tabs.pinned.selected.odd.fg = '#000000'

""" input """

# disable insert mode completely
c.input.insert_mode.auto_enter = False
c.input.insert_mode.auto_leave = False
c.input.insert_mode.plugins = False
# Forward unbound keys
c.input.forward_unbound_keys = "all"

""" bindings """

import string

c.bindings.default['normal'] = {}
c.bindings.default['insert'] = {}

c.bindings.commands['insert'] = {
    '<ctrl-space>': 'mode-leave',
#    '<ctrl-g>': 'mode-leave;;fake-key <Left>;;fake-key <Right>',
    '<ctrl-f>': 'fake-key <Shift-Right>',
    '<ctrl-b>': 'fake-key <Shift-Left>',
    '<ctrl-e>': 'fake-key <Shift-End>',
    '<ctrl-a>': 'fake-key <Shift-Home>',
    '<ctrl-p>': 'fake-key <Shift-Up>',
    '<ctrl-n>': 'fake-key <Shift-Down>',
    '<Return>': 'mode-leave',
    '<ctrl-w>': 'fake-key <Ctrl-x>;;message-info "cut to clipboard";;mode-leave',
    '<alt-w>': 'fake-key <Ctrl-c>;;message-info "copy to clipboard";;mode-leave',
    '<backspace>': 'fake-key <backspace>;;mode-leave',
    '<alt-x>': 'mode-leave;;set-cmd-text :',
    '<alt-o>': 'mode-leave;;tab-focus last',
    '<Tab>': 'fake-key <f1>'
}

for char in list(string.ascii_lowercase):
    c.bindings.commands['insert'].update({char: 'fake-key ' + char + ';;mode-leave'})

for CHAR in list(string.ascii_uppercase):
    c.bindings.commands['insert'].update({CHAR: 'fake-key ' + char + ';;mode-leave'})

for num in list(map(lambda x : str(x), range(0, 10))):
    c.bindings.commands['insert'].update({num: 'fake-key ' + num + ';;mode-leave'})

for symb in [',', '.', '/', '\'', ';', '[', ']', '\\',
             '!', '@','#','$','%','^','&','*','(',')','-','_', '=', '+', '`', '~',
             ':', '\"', '<', '>', '?','{', '}', '|']:
    c.bindings.commands['insert'].update({symb: 'insert-text ' + symb + ' ;;mode-leave'})

c.bindings.commands['normal'] = {
    # Navigation
    '<ctrl-space>': 'mode-enter insert',
    '<ctrl-]>': 'fake-key <Ctrl-Shift-Right>',
    '<ctrl-[>': 'fake-key <Ctrl-Shift-Left>',
    '<ctrl-v>': 'scroll-page 0 0.5',
    '<alt-v>': 'scroll-page 0 -0.5',
    '<ctrl-shift-v>': 'scroll-page 0 1.0',
    '<alt-shift-v>': 'scroll-page 0 -1.0',
    '<alt-shift-greater>': 'scroll-to-perc 100',
    '<alt-shift-less>': 'scroll-to-perc 0',

    '<alt-x>': 'set-cmd-text :',
    '<ctrl-x><ctrl-b>': 'bookmark-list -t',
    '<ctrl-x>k<return>': 'tab-close',
    #'<ctrl-x>r': 'config-cycle statusbar.hide',
    #'<ctrl-x>1': 'tab-only;;message-info "cleared all other tabs"',
    '<ctrl-x><ctrl-c>': 'wqa',

    # zoom in/out
    '<ctrl-x><ctrl-=>': 'zoom-in',
    '<ctrl-x><ctrl-->': 'zoom-out',

    # searching
    '<ctrl-s>': 'set-cmd-text /',
    '<ctrl-r>': 'set-cmd-text ?',

    # hinting
    '<alt-g><alt-g>': 'hint all',

    # tabs
    '<alt-[>': 'tab-prev',
    '<alt-]>': 'tab-next',
    '<alt-ctrl-shift-{>': 'tab-move -',
    '<alt-ctrl-shift-}>': 'tab-move +',
    '<alt-1>': 'tab-select 1',
    '<alt-2>': 'tab-select 2',
    '<alt-3>': 'tab-select 3',
    '<alt-4>': 'tab-select 4',
    '<alt-5>': 'tab-select 5',
    '<alt-6>': 'tab-select 6',
    '<alt-7>': 'tab-select 7',
    '<alt-8>': 'tab-select 8',
    '<alt-9>': 'tab-select 9',
    '<alt-0>': 'tab-select 10',

    # open links
    '<ctrl-l>': 'set-cmd-text -s :open',
    '<alt-l>': 'set-cmd-text -s :open -t',

    # reload
    '<ctrl-x><ctrl-v><return>': 'reload',

    # editing
    '<ctrl-shift-{>': 'back',
    '<ctrl-shift-}>': 'forward',
    '<ctrl-/>': 'fake-key <Ctrl-z>',
    '<ctrl-shift-?>': 'fake-key <Ctrl-Shift-z>',
    '<ctrl-k>': 'fake-key <Shift-End>;;fake-key <Backspace>',
    '<ctrl-f>': 'fake-key <Right>',
    '<ctrl-b>': 'fake-key <Left>',
    '<alt-o>': 'tab-focus last',
    '<ctrl-a>': 'fake-key <Home>',
    '<ctrl-x>h': 'fake-key <Ctrl-a>',
    '<ctrl-e>': 'fake-key <End>',
    '<ctrl-n>': 'fake-key <Down>',
    '<ctrl-p>': 'fake-key <Up>',
    '<alt-f>': 'fake-key <Ctrl-Right>',
    '<alt-b>': 'fake-key <Ctrl-Left>',
    '<ctrl-d>': 'fake-key <Delete>',
    '<alt-d>': 'fake-key <Ctrl-Delete>',
    '<alt-backspace>': 'fake-key <Ctrl-Backspace>',
    '<ctrl-w>': 'fake-key <Ctrl-x>;;message-info "cut to clipboard"',
    '<alt-w>': 'fake-key <Ctrl-c>;;message-info "copy to clipboard"',
    '<ctrl-y>': 'insert-text {primary}',
    '1': 'fake-key 1',
    '2': 'fake-key 2',
    '3': 'fake-key 3',
    '4': 'fake-key 4',
    '5': 'fake-key 5',
    '6': 'fake-key 6',
    '7': 'fake-key 7',
    '8': 'fake-key 8',
    '9': 'fake-key 9',
    '0': 'fake-key 0',

    # escape hatch
    '<ctrl-h>': 'set-cmd-text -s :help',
    #'<ctrl-g>': ESC_BIND,
}

c.bindings.commands['command'] = {
    '<ctrl-s>': 'search-next',
    '<ctrl-r>': 'search-prev',

    '<ctrl-p>': 'completion-item-focus prev',
    '<ctrl-n>': 'completion-item-focus next',

    '<alt-p>': 'command-history-prev',
    '<alt-n>': 'command-history-next',

    # escape hatch
    #'<ctrl-g>': 'mode-leave',
}

c.bindings.commands['hint'] = {
    # escape hatch
    #'<ctrl-g>': 'mode-leave',
}

c.bindings.commands['caret'] = {
    # escape hatch
    #'<ctrl-g>': 'mode-leave',
    '<ctrl-space>': 'toggle-selection'
}

c.bindings.key_mappings = {"<Ctrl-G>": "<Escape>"}
