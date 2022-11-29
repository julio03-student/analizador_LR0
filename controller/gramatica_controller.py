class Gramatica_Controller:

    def __init__(self):
        pass

    def organizarGramatica(self, grammar):
        orderGramatica = []
        for value in grammar.values():
            orderGramatica.append(value.split('->'))
        return orderGramatica

    def noTerminalesM(self, producciones):
        noTerminales = []
        for k in producciones.keys():
            noTerminales.append(k)
        return noTerminales

    def aggProducciones(self, split):
        producciones = {}
        for k in split:
            producciones[k[0].strip()] = k[1].split('|')
        for i,j in producciones.items():
            min_producciones = []
            for k in j:
                min_producciones.append(k.strip().split(' '))
            producciones[i] = min_producciones
        return producciones

    def aggTerminales(self, producciones, noTerminales):
        terminales = []
        for produccion in producciones.values():
            for prod in produccion:
                for prod1 in prod:
                    if prod1 not in noTerminales and prod1 not in terminales:
                        terminales.append(prod1)
        return terminales