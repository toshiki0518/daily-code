from frog import Frog
from knapsack import Knapsack
def frog():
    # frog = Frog(True)
    # frog.get_total_min_jump_cost_hard_code()
    frog = Frog(True)
    frog.check()

def knapsack():
    knapsack = Knapsack()
    knapsack.check()

def main():
    # frog()
    knapsack()

if __name__ == "__main__":
    main()