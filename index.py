import model.gramatica as gramatica

grammar = {
    "1": "S -> A B",
    "2": "A -> A a | @",
    "3": "B -> b C d",
    "4": "C -> c |  @"
}

gr = gramatica.Gramatica(grammar)

print(gr.getProducciones())