
from models.elektromobilis import Automobilis, Elektromobilis

class Garazas:
    def __init__(self):
        self.automobiliai = []

    def prideti_auto(self):
        marke = input("Markė: ")
        modelis = input("Modelis: ")
        metai = int(input("Metai: "))
        automobilis = Automobilis(marke, modelis, metai)
        self.automobiliai.append(automobilis)

    def prideti_elektroauto(self):
        marke = input("Markė: ")
        modelis = input("Modelis: ")
        metai = int(input("Metai: "))
        talpa = int(input("Talpa: "))
        elektroautomobilis = Elektromobilis(marke, modelis, metai)
        self.automobiliai.append(elektroautomobilis)

    def atvaizduoti_auto(self):
        # print(self.automobiliai)
        for auto in self.automobiliai:
            print(auto)