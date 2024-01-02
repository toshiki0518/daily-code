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
        total_jump_cost = 0
        current = 0
        goal = len(self.scaffolds) - 1
        while True:
            current_height = self.scaffolds[current]
            next_jump = random.randint(1, 2)
            next_position = min(current + next_jump, goal)  # 次のジャンプ後の位置
            next_height = self.scaffolds[next_position]
            jump_cost = abs(current_height - next_height)
            total_jump_cost += jump_cost
            print("total:{},current:{} - {}".format(total_jump_cost, current_height, next_height))
            current = next_position
            if current >= goal:
                break
        return total_jump_cost

    pass



def main():
    frog = Frog()
    print(frog.get_jump_cost())

if __name__ == "__main__":
    main()