class Knapsack():
    def __init__(self) -> None:
        self.max_weight = 0
        self.weight_value_list = self._create_weight_value_list()
        self._total_weight()

    def _create_weight_value_list(self):
        weight_value_list = []
        # sample1
        # weight_value_list.append((2, 3))
        # weight_value_list.append((1, 2))
        # weight_value_list.append((3, 6))
        # weight_value_list.append((2, 1))
        # weight_value_list.append((1, 3))
        # weight_value_list.append((5, 85))

        # sample2
        weight_value_list.append((4, 3))
        weight_value_list.append((6, 2))
        weight_value_list.append((2, 6))
        weight_value_list.append((3, 1))
        weight_value_list.append((2, 3))
        # weight_value_list.append((9, 85))

        print(len(weight_value_list))
        print(weight_value_list)
        return weight_value_list

    def _total_weight(self):
        # weight_value_listのすべての要素の重さの合計を算出
        total_weight = sum(weight for weight, _ in self.weight_value_list)
        print("total_weight:{}".format(total_weight))
        total_value = sum(value for _, value in self.weight_value_list)
        print("total_value:{}".format(total_value))
        return total_weight

    def calc(self):
        n = len(self.weight_value_list)
        dp = [[0] * (self.max_weight + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(self.max_weight + 1):
                weight_i, value_i = self.weight_value_list[i - 1]
                if w >= weight_i:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight_i] + value_i)
                else:
                    dp[i][w] = dp[i - 1][w]

        # 最適な結果を出力
        result = dp[n][self.max_weight]
        print("dp:", dp)
        print("n:", n)
        print("dp[n]:", dp[n])
        print("Optimal Value:", result)


    def check(self):
        pass

def main():
    print("knapsack")
    knapsack = Knapsack()
    knapsack.max_weight = 11 # ナップサックの容量を設定
    knapsack.calc()

if __name__ == "__main__":
    main()
