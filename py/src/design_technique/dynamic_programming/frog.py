import random

class Frog:
    def __init__(self, is_sample = False) -> None:
        self.scaffolds = self._create_scaffolds(is_sample)
        self.jump_cost_list = []

    def _create_scaffolds(self, is_sample = False):

        if is_sample is True:
            sample_scaffolds = [2, 9, 4, 5, 1, 6, 10]
            return sample_scaffolds
        else:
            length_input = input("Enter the quantity: ")
            length = int(length_input) if length_input else 10
            return [random.randint(0, 10) for _ in range(length)]
            # for _ in range(length):
            #     height = random.randint(0, 10)
            #     scaffolds.append(height)
            # return scaffolds
    
    def _calc_jump_cost(self, point1: int, point2: int ) -> int:
        height1 = self.scaffolds[point1]
        height2 = self.scaffolds[point2]
        return abs(height1 - height2)

    def get_total_min_jump_cost_hard_code(self):
        INF = 100
        self.jump_cost_list = []
        next = 0
        self.jump_cost_list.append(0)

        # scaffolds 1
        next += 1
        self.jump_cost_list.append(self._calc_jump_cost(next - 1, next))

        # scaffolds 2
        next += 1
        cost1 = self.jump_cost_list[next - 1] + self._calc_jump_cost(next - 1, next)
        cost2 = self._calc_jump_cost(next - 2, next)
        self.jump_cost_list.append(cost1 if cost1 < cost2 else cost2)

        # scaffolds 3
        next += 1
        cost1 = self.jump_cost_list[next - 1] + self._calc_jump_cost(next - 1, next)
        cost2 = self.jump_cost_list[next - 2] + self._calc_jump_cost(next - 2, next)
        self.jump_cost_list.append(cost1 if cost1 < cost2 else cost2)

        # scaffolds 4
        next += 1
        cost1 = self.jump_cost_list[next - 1] + self._calc_jump_cost(next - 1, next)
        cost2 = self.jump_cost_list[next - 2] + self._calc_jump_cost(next - 2, next)
        self.jump_cost_list.append(cost1 if cost1 < cost2 else cost2)

        # scaffolds 5
        next += 1
        cost1 = self.jump_cost_list[next - 1] + self._calc_jump_cost(next - 1, next)
        cost2 = self.jump_cost_list[next - 2] + self._calc_jump_cost(next - 2, next)
        self.jump_cost_list.append(cost1 if cost1 < cost2 else cost2)

        # scaffolds 6
        next += 1
        cost1 = self.jump_cost_list[next - 1] + self._calc_jump_cost(next - 1, next)
        cost2 = self.jump_cost_list[next - 2] + self._calc_jump_cost(next - 2, next)
        self.jump_cost_list.append(cost1 if cost1 < cost2 else cost2)

        print("height:{}:".format(self.scaffolds))
        print("cost_list:{}".format(self.jump_cost_list))
        print("cost:{}".format(self.jump_cost_list[-1:]))
        return self.jump_cost_list

    def get_total_min_jump_cost(self):
        self.jump_cost_list = []
        self.jump_cost_list.append(0)
        self.jump_cost_list.append(self._calc_jump_cost(0, 1))

        for i in range(2, len(self.scaffolds)):
            # 
            self.jump_cost_list.append(
                min(
                    self.jump_cost_list[i - 1] + self._calc_jump_cost(i - 1, i)
                    ,self.jump_cost_list[i - 2] + self._calc_jump_cost(i - 2, i)
                )
            )
        print("height:{}:".format(self.scaffolds))
        print("cost_list:{}".format(self.jump_cost_list))
        print("cost:{}".format(self.jump_cost_list[-1:]))
        return self.jump_cost_list

def main():
    frog = Frog(True)
    frog.get_total_min_jump_cost()

if __name__ == "__main__":
    main()