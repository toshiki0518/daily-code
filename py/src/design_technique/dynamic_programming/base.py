import sys
import random

class Frog:
    def __init__(self) -> None:
        self.scaffolds = self._create_scaffolds()

    def _create_scaffolds(self):
        length_input = input("Enter the quantity: ")
        length = int(length_input) if length_input else 10
        scaffolds = []
        for _ in range(length):
            height = random.randint(0, 10)
            scaffolds.append(height)
        return scaffolds
    
    def get_jump_cost(self):
        jump_cost = 0
        current = 0
        goal = len(self.scaffolds)
        while current < goal:
            current_height = self.scaffolds[current]
            next_jump = random.randint(1, 2)
            next_position = min(current + next_jump, goal - 1)  # 次のジャンプ後の位置
            next_height = self.scaffolds[next_position]
            jump_cost += abs(current_height - next_height)
            current = next_position
        return jump_cost

    pass



def main():
    frog = Frog()
    print(frog.get_jump_cost())

if __name__ == "__main__":
    main()