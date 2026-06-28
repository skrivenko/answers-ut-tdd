class Game:
    def __init__(self, cells):
        self.alive_cells = cells

    def next_generation(self) -> None:
        self.alive_cells = []
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Game):
            return False
        return self.alive_cells == other.alive_cells

