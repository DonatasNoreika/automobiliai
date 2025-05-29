from dataclasses import dataclass
from models.automobilis import Automobilis

@dataclass
class Elektromobilis(Automobilis):
    marke: str
    modelis: str
    metai: int
    talpa: int
