class Element:
    def __init__(self, 
        atomic_number: int,
        name: str,
        symbol: str,
        atomic_mass: float,
        num_electrons: int
    ) -> None:
        self.atomic_number = atomic_number
        self.name = name
        self.symbol = symbol
        self.atomic_mass = atomic_mass
        self.num_electrons = num_electrons
    
    def __str__(self) -> str:
        return f"{self.atomic_number} {self.name} ({self.symbol}) neutrons: {self.neutrons()}"
    
    def charge(self) -> int:
        return self.atomic_number - self.num_electrons
    
    def neutrons(self) -> int:
        return int(self.atomic_mass) - self.atomic_number