import random

def roll_dice():
    return random.randint(1, 6)

def main():
    dice1 = 0
    dice2 = 0
    count = 0
    
    while dice1 != 6 or dice2 != 6:
        dice1 = roll_dice()
        dice2 = roll_dice()
        count += 1
        print(f"Dice 1: {dice1}, Dice 2: {dice2}, Rolls: {count}")
        
    print(f"Both dice rolled 6! It took {count} rolls.")
    
if __name__ == "__main__":
    main()