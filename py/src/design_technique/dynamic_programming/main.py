from frog import Frog
from knapsack import Knapsack
from edit_distance import EditDistance

def frog():
    # frog = Frog(True)
    # frog.get_total_min_jump_cost_hard_code()
    frog = Frog(True)
    frog.check()

def knapsack():
    knapsack = Knapsack()
    knapsack.check()

def edit_distance():
    edit_distance = EditDistance()
    edit_distance.check()

def main():
    # frog()
    # knapsack()
    edit_distance()

if __name__ == "__main__":
    main()