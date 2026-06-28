class Cell:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Cell) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
    
    def has_neighbor(self, other):
        return abs(other.x - self.x) <= 1 and abs(other.y - self.y) <= 1
    
    def count_neighbors(self, alive_cells):
        count = 0
        for cell in alive_cells:
            if cell != self and self.has_neighbor(cell):
                count += 1
        return count