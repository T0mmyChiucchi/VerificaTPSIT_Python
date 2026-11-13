from pannello import PannelloFotovoltaico

class ImpiantoSolare:
    def __init__(self, codice: str, modello: str, localita: str, potenza_massima_kw: float, stato: str) -> None:
        self.codice = codice
        self.mdoello = modello
        self.localita = localita
        self.potenza_massima_kw = potenza_massima_kw
        self.stato = stato
        self.pannelli: list[PannelloFotovoltaico] = []
    
    def aggiungi_pannello(self, pannello: PannelloFotovoltaico) -> None:
        if pannello.codice in pannelli:
            raise ValueError("Il pannello è già presente")
        if pannello.potenza_kw > self.potenza_massima_kw:
            raise ValueError("La potenza super quella massima")
        self.pannelli.append(pannello)
        
    def potenza_pannelli(self) -> float:
        sum(pannello.potenza_kw for pannello in self.pannelli)
        
    def cerca_pannello(self, codice: str) -> PannelloFotovoltaico:
        for pannello in self.pannelli:
            if pannello.codice.lower() == codice.lower():
                return pannello
        return None
    
    def rimuovi_pannello(self, codice: str) -> PannelloFotovoltaico:
        for pannello in self.pannelli:
            if pannello.codice.lower() == codice.lower():
                self.pannelli.remove(pannello)
                return pannello
        return None
    
    def pannelli_sotto_potenza(self, potenza_massima: float) -> list[PannelloFotovoltaico]:
        return [pannello for pannello in self.pannelli if pannello.potenza_wq <= potenza_massima]