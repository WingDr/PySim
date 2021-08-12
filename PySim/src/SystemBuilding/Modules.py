import numpy as np
from src.Solving.Solver import Solver

'''
Basic class of all modal in system
'''
class Modal:
    def __init__(self, 
            name: str = "default modal",
            input_port: int = 1, 
            output_port: int = 1, 
            
            ) -> None:
        
        self.name = name
        self.input_port = input_port
        self.output_port = output_port

    def describe(self):
        print("name: ", self.name)
        print("input port number: ", self.input_port)
        print("output port number: ", self.output_port)
    
    def solve(self):
        print("{} modal has no solve function!".format(self.name))
        return np.zeros(self.output_port, 1)

class StateFunc(Modal):
    def __init__(self, 
            A: np.ndarray = None, 
            B: np.ndarray = None, 
            C: np.ndarray = None, 
            D: np.ndarray = None, 
            initial_state: np.ndarray = None
            ) -> None:
        super().__init__(name="state function", input_port=B.shape[1], output_port=C.shape[0])
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        if initial_state is not None:
            self.state = initial_state
        else:
            self.state = np.zeros(A.shape[0], 1)

        self.A.dtype = 'float64'
        self.B.dtype = 'float64'
        self.C.dtype = 'float64'
        self.D.dtype = 'float64'
        self.state.dtype = 'float64'

        self.state_his = []
    
    def solve(self):
        solver = Solver()
        solver.solve()
