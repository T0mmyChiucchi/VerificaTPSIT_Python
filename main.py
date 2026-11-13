from pannello import PannelloFotovoltaico
from impianto import ImpiantoSolare

if __name__ == "__main__":
    impianti = list[ImpiantoSolare]
    i1 = ImpiantoSolare("ABC", "Aurora", "Cesena", 100, "in installazione")
    i2 = ImpiantoSolare("ABC", "Aurora", "Milano", 100, "in collaudo")
    i3 = ImpiantoSolare("ABC", "Aurora", "Roma", 100, "attivo")
    i4 = ImpiantoSolare("ABC", "Aurora", "Forli", 100, "in installazione")
    
    impianti.append(i1)
    impianti.append(i2)
    impianti.append(i3)
    impianti.append(i4)
    
    