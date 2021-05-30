import random
import copy
from local_search import *

random.seed(42)


class IteratedLocalSearch:
    def __init__(self, data, iters):
        self.data = data
        self.solution = initial_solution(self.data.n)
        self.iter_num = iters
        self.cost = self.data.cost_calculator(self.solution)

        self.best_solution = copy.deepcopy(self.solution)
        self.best_cost = copy.deepcopy(self.cost)

    def perturbation(self):
        self.solution = list(self.solution)
        s1, s2 = random.sample(self.solution, 2)

        if s1 > s2:
            temp = s1
            s1 = s2
            s2 = temp

        self.solution = np.array(self.solution[:s1] + list(reversed(self.solution[s1:s2])) + self.solution[s2::])

    def first_improvement(self):
        dont_look_bits = np.zeros(self.data.n)

        for _ in range(self.iter_num):

            self.perturbation()

            if np.all(dont_look_bits):
                break
            combs = list(combinations(np.arange(self.data.n), 2))
            city = 0
            cnt = 0

            combs_rand = random.sample(combs, 50)  # смотрим не все комбинации, а n случайных

            for item in combs_rand:
                if dont_look_bits[item[0]] or dont_look_bits[item[1]]:
                    continue

                item = list(item)
                cur_solution = self.solution.copy()
                cur_solution[item] = cur_solution[item][::-1]
                cost = self.data.cost_calculator(cur_solution)

                if cnt == self.data.n - city - 1 and city != item[0]:
                    dont_look_bits[city] = 1
                    cnt = 0
                    city += 1
                elif city != item[0]:
                    cnt = 0
                    city += 1

                if cost < self.best_cost:
                    self.best_cost = cost
                    self.best_solution = cur_solution
                    break
                elif city == item[0]:
                    cnt += 1

        sol = self.best_solution
        cost = self.data.cost_calculator(self.best_solution)
        return sol, cost


def solver2(data):
    ls = IteratedLocalSearch(data, 50)
    sol, cost = ls.first_improvement()
    return sol, cost