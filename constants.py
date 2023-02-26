from dataclasses import dataclass


@dataclass(frozen=True)
class APP:
    VERSION: str = "ALPHA 1.0"
    NAME: str = "BarPek Directory Sorter"
    

@dataclass(frozen=True)
class WINDOW:
    SIZE: str = "750x750"
    BACKGROUND: str = "#404040"
