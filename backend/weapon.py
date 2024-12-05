class Weapon:
    def __init__(self, to_hit, dice_size, dice_number):
        self.to_hit = to_hit
        self.dice_size = dice_size
        self.dice_number = dice_number

# Base stats
## dice_size: 3
## dice_number: d6 [d4, d6, d8, d10, d12]

# Runes
## potency: 1
## striking: 1 [0, 1, 2]
## elemental: {fire: 1, lightning: 0, cold: 2}
