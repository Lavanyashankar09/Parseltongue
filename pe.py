import parseltongue as pt
from dragonfly import *

grammarContext = AppContext(executable="pe")
grammar = Grammar("parseltongueGrammar", context=grammarContext)

grammar = Grammar("Parseltongue")
grammar.add_rule(pt.ContinuousRules())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None