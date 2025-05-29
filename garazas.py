import pickle
from models.elektromobilis import Automobilis, Elektromobilis

class Garazas:
    def __init__(self):
        self.automobiliai = self.gauti_garaza()

    def gauti_garaza(self):
        try:
            with open("garazas.pkl", 'rb') as file:
                automobiliai = pickle.load(file)
        except:
            automobiliai = []
        return automobiliai

    def irasyti_garaza(self):
        with open("garazas.pkl", 'wb') as file:
            pickle.dump(self.automobiliai, file)

    def prideti_auto(self):
        marke = input("Markė: ")
        modelis = input("Modelis: ")
        metai = int(input("Metai: "))
        automobilis = Automobilis(marke, modelis, metai)
        self.automobiliai.append(automobilis)
        self.irasyti_garaza()

    def prideti_elektroauto(self):
        marke = input("Markė: ")
        modelis = input("Modelis: ")
        metai = int(input("Metai: "))
        talpa = int(input("Talpa: "))
        elektroautomobilis = Elektromobilis(marke, modelis, metai)
        self.automobiliai.append(elektroautomobilis)
        self.irasyti_garaza()

    def atvaizduoti_auto(self):
        # print(self.automobiliai)
        for auto in self.automobiliai:
            print(auto)