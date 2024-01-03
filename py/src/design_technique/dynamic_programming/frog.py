import random

class Frog:
    def __init__(self, is_sample = False) -> None:
        self.scaffolds = self._create_scaffolds(is_sample)
        self.jump_cost_list = []
        self.INF = 10000
    def _create_scaffolds(self, is_sample = False):

        if is_sample:
            sample_scaffolds = [2, 9, 4, 5, 1, 6, 10]
            return sample_scaffolds
        else:
            length_input = input("Enter the quantity of scaffolds: ")
            length = int(length_input) if length_input else 10
            return [random.randint(0, 10) for _ in range(length)]
            # for _ in range(length):
            #     height = random.randint(0, 10)
            #     scaffolds.append(height)
            # return scaffolds
    
    def _calc_jump_cost(self, point1: int, point2: int ) -> int:
        """Calculate the jump cost between two points."""
        height1 = self.scaffolds[point1]
        height2 = self.scaffolds[point2]
        return abs(height1 - height2)

    def get_total_min_jump_cost_hard_code(self):
        """動的計画法の解説用コード"""
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

        self.show_result()
        return self.jump_cost_list

    def get_total_min_jump_cost_p1(self) -> int:
        """
        calc total minumun jump cost patter1
        Returns:
            int: calculation result
        """
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
        self.show_result()
        return self.jump_cost_list

    def _update_min_pulled_base(self, jump_cost_list, position, jump_distance):
        current_value = jump_cost_list[position]
        compare_value = jump_cost_list[position - jump_distance] + self._calc_jump_cost(position - jump_distance, position)
        if(current_value > compare_value):
            # update minumum value
            jump_cost_list[position] = compare_value

    def _update_min_pushed_base(self, jump_cost_list, position, jump_distance):
        current_value = jump_cost_list[position + jump_distance]
        compare_value = jump_cost_list[position] + self._calc_jump_cost(position + jump_distance, position)
        if(current_value > compare_value):
            # update minumum value
            jump_cost_list[position + jump_distance] = compare_value

    def get_total_min_jump_cost_with_relaxation(self, is_pulled_base = True) -> int:
        """
        dynamic programming
        calc total minumun jump cost pattern2
        with relaxation
        Returns:
            int: calculation result
        """
        list_length = len(self.scaffolds)
        jump_cost_list = [self.INF] * list_length
        jump_cost_list[0] = 0
        # jump_cost_list.append(self._calc_jump_cost(0, 1))

        if is_pulled_base:
            print("pulled_base")
            for i in range(1, len(self.scaffolds)):
                self._update_min_pulled_base(jump_cost_list, i, 1)
                if i > 1:
                    self._update_min_pulled_base(jump_cost_list, i, 2)
        else:
            print("pushed_base")
            for i in range(len(self.scaffolds)):
                if i + 1 < list_length:
                    self._update_min_pushed_base(jump_cost_list, i, 1)
                if i + 2 < list_length:
                    self._update_min_pushed_base(jump_cost_list, i, 2)
        self.jump_cost_list = jump_cost_list
        self.show_result()
        return self.jump_cost_list

    def show_result(self):
        print("height:{}:".format(self.scaffolds))
        print("cost_list:{}".format(self.jump_cost_list))
        print("cost:{}".format(self.jump_cost_list[-1:]))

    def get_total_min_jump_cost_with_recursion(self):
        self.jump_cost_list = [self.INF] * len(self.scaffolds)
        jump_cost = self._calc_with_recursion()
        print("cost:{}".format(jump_cost))


    def _calc_with_recursion(self,position: int) -> int:
        if self.jump_cost_list[position] < self.INF:
            return self.jump_cost_list[position]
        if position == 0:
            return 0
        result = self.INF
        result = min(result, self._calc_with_recursion(position - 1) + abs(self.scaffolds[position] - self.scaffolds[position -1]))
        if position > 1:
            result = min(result, self._calc_with_recursion(position - 1) + abs(self.scaffolds[position] - self.scaffolds[position -1]))
        self.jump_cost_list[position] = result
        
    def check(self):
        self.get_total_min_jump_cost_p1()
        self.get_total_min_jump_cost_with_relaxation(True)
        self.get_total_min_jump_cost_with_relaxation(False)

def main():
    frog = Frog(True)
    frog.get_total_min_jump_cost_p1()
    frog = Frog(True)
    frog.get_total_min_jump_cost_with_relaxation(True)
    frog.get_total_min_jump_cost_with_relaxation(False)
    frog = Frog(True)
    frog.get_total_min_jump_cost_with_relaxation()

if __name__ == "__main__":
    main()