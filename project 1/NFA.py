class NFA:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.start_state = set()
        self.final_state = set()
        self.transitions = {}

    def add_transition(self, from_state, input_char, to_state):
        if from_state not in self.transitions:
            self.transitions[from_state] = {}

        if input_char not in self.transitions[from_state]:
            self.transitions[from_state][input_char] = set()  # مقداردهی به یک مجموعه

        self.transitions[from_state][input_char].add(to_state)


def grammar_to_nfa(grammar) -> NFA:
    nfa = NFA()

    for rule in grammar:
        left, right = rule.split('->')
        nfa.states.add(left)
        for symbol in right:
            if symbol.islower():
                nfa.alphabet.add(symbol)
            elif symbol.isupper():
                nfa.states.add(symbol)
                nfa.add_transition(left, symbol, symbol)
            elif symbol == "λ":
                nfa.add_transition(left, "", right)
    return nfa

grammar = [
    "S->aA",
    "A->bB",
    "B->λ"
]

nfa = grammar_to_nfa(grammar)

print(nfa.states)
print(nfa.alphabet)
print(nfa.start_state)
print(nfa.final_state)
print(nfa.transitions)