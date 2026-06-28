class Game:
    def __init__(self, cells):
        self.alive_cells = cells

    def next_generation(self) -> None:
        survived_cells = []
        for cell in self.alive_cells:
            neighbours_count = cell.count_neighbors(self.alive_cells)
            if neighbours_count == 2 or neighbours_count == 3:
               survived_cells.append(cell)
        self.alive_cells = survived_cells
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Game):
            return False
        return self.alive_cells == other.alive_cells

