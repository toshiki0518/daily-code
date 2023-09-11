import time
import datetime

class Order:
    def __init__(self, n):
        """_summary_

        Args:
            n (_typine_): _description_
        """
        self.time = n

    def single_loop(self):
        # O(N)
        count = 0
        for i in range(self.time):
            count += 1
        print(count)

    def double_loop(self):
        # O(N2)
        count = 0
        for i in range(self.time):
            for j in range(self.time):
                count += 1
        print(count)

    def measure_time(self):
        # print(self.time)
        start = time.perf_counter()
        self.single_loop()
        end = time.perf_counter()
        # print("single:")
        print(end - start)
        start = time.perf_counter()
        self.double_loop()
        end = time.perf_counter()
        # print("double:")
        print(end - start)

Order(10).measure_time()
Order(100).measure_time()
Order(1000).measure_time()
Order(10000).measure_time()
# Order(100000).measure_time()

