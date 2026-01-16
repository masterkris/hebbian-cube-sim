class RubiksCube:
    def __init__(self):
        # simulating T-perm algorithm for 2-look PLL 
        # mapping is as follows:
        # R = 0, U = 1, Ri = 2, Ui = 3, F = 4, Fi = 5, R2 = 6
        # (R U Ri Ui) Ri F R2 Ui Ri Ui R U Ri Fi --> algo
        # [0, 1, 2, 3, 2, 4, 6, 3, 2, 3, 0, 1, 2, 5]
        self.t_perm_sequence = [0, 1, 2, 3, 2, 4, 6, 3, 2, 3, 0, 1, 2, 5]
        self.move_lookup = {
            0: "R", 1: "U", 2: "R'", 3: "U'", 
            4: "F", 5: "F'", 6: "R2"} # possible moves for T-perm
        
    def get_sequence(self):
        return self.t_perm_sequence
    
    def get_move_name(self, index):
        return self.move_lookup.get(index, "Unknown")