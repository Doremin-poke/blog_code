class Pokemon:
    def __init__(self, name, types, H, A, B, C, D, S, move1, move2, move3, move4, terastal):
        self.name = name
        self.types = types  # リスト定義する
        self.H = H
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.S = S
        self.moves = [move1, move2, move3, move4]  # 技をリストで保持する
        self.terastal = terastal

Landorus = Pokemon("Landorus", ["Fly", "Ground"], 165, 197, 110, 112, 100, 157, Earthquake, U_Turn, Rock_Slide, Protect, "Fly")
