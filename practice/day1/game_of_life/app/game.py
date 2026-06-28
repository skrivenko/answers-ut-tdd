class Game:
    def __init__(self, cells):
        self.alive_cells = cells

    def next_generation(self) -> None:
        survived_cells = []
        for cell in self.alive_cells:
            if cell.count_neighbors(self.alive_cells) == 2:
               survived_cells.append(cell)
        self.alive_cells = survived_cells
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Game):
            return False
        return self.alive_cells == other.alive_cells

