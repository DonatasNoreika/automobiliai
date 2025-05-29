from garazas import Garazas

garazas = Garazas()

if __name__ == "__main__":
    while True:
        veiksmas = int(input("1 - peržiūrėti, 2 - pridėti automobilį, 3 - pridėti elektromobilį, 0 - išeiti: "))
        match veiksmas:
            case 1: garazas.atvaizduoti_auto()
            case 2: garazas.prideti_auto()
            case 3: garazas.prideti_elektroauto()
            case 0: break
            case _: print("Neteisingas pasirinkimas")