import rk45

class Solver:
    def __init__(self) -> None:
        self.rk45 = rk45.rk45()
    
    def solve(self):
        return None