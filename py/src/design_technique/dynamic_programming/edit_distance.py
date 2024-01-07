class EditDistance():
    def __init__(self) -> None:
        self.str_S = ""
        self.str_T = ""
        self.number_of_operations = 0

    def _check_equal(self):
        print("s:{},t:{}".format(self.str_S,self.str_T))
        if self.str_S == self.str_T:
            print("equal")
        else:
            print("not equal")

    def _count_edit_distance(self):
        self.number_of_operations += 1
        print(self.number_of_operations)
        self._check_equal()

    def _change(self, target_str, position, change_str):
        after_str =""
        if 0 <= position < len(target_str):
            after_str = target_str[:position] + change_str + target_str[position + 1:]
        else:
            after_str = target_str
        return after_str     

    def _delete(self, target_str, position):
        modified_str = target_str[:position] + target_str[position + 1:]
        return modified_str

    def _insert(self, target_str: str, position: int, insert_value: str):
        inserted_str = target_str[:position] + insert_value + target_str[position:]
        return inserted_str

    def _sample1(self):
        self.number_of_operations = 0
        self.str_S = "bag"
        self.str_T = "big"

    def _sample2(self):
        self.number_of_operations = 0
        self.str_S = "kodansha"
        self.str_T = "danshari"

    def _sample3(self):
        self.number_of_operations = 0
        self.str_S = "logistic"
        self.str_T = "algorithm"
        self.str_S = self._insert(self.str_S, 0, "a")
        self._count_edit_distance()
        self.str_S = self._insert(self.str_S, 2, "g")
        self._count_edit_distance()
        self.str_S = self._change(self.str_S, 4, "r")
        self._count_edit_distance()
        self.str_S = self._delete(self.str_S, 6)
        self._count_edit_distance()
        self.str_S = self._change(self.str_S, 7, "h")
        self._count_edit_distance()
        self.str_S = self._change(self.str_S, 8, "m")
        self._count_edit_distance()

    def measure_similarity(self):
        self._sample3()

    def edit_distance(self):
        # wip
        pass

    def check(self):
        self.measure_similarity()
        pass

def main():
    print("knapsack")
    edit_distance = EditDistance()
    edit_distance.measure_similarity()

if __name__ == "__main__":
    main()
