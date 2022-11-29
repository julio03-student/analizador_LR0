import controller.gramatica_controller as controller

class Gramatica:

    controller = controller.Gramatica_Controller()

    LAMBDA = '@'
    prod_inicial = ''
    producciones = {}
    min_producciones = []
    noTerminales = []
    terminales = []
    orderGramatica = []
    mapPrimeros = {}

    def __init__(self, grammar):
        self.orderGramatica = self.controller.organizarGramatica(grammar)
        self.producciones = self.controller.aggProducciones(self.orderGramatica)
        self.noTerminales = self.controller.noTerminalesM(self.producciones)
        self.prod_inicial = self.noTerminales[0]
        self.terminales = self.controller.aggTerminales(self.producciones, self.noTerminales)

    def getOrderGramatica(self):
        return self.orderGramatica

    def getProducciones(self):
        return self.producciones

    def getNoTerminales(self):
        return self.noTerminales
    
    def getProd_Inicial(self):
        return self.prod_inicial

    def getTerminales(self):
        return self.terminales
