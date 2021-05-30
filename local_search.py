import numpy as np
from itertools import combinations


def initial_solution(n):
    return np.random.permutation(np.arange(n))


class QAPdata:
    def __init__(self, n, distances, flows):
        self.n = n
        self.flows = flows
        self.distances = distances

    def cost_calculator(self, solution):
        cost = 0
        for i in range(self.n):
            for j in range(self.n):
                dist = self.distances[solution[i]][solution[j]]
                flow = self.flows[i][j]
                cost += flow * dist
        return cost


def QAPreader(path):
    with open(path, "r") as f:
        n = int(f.readline().strip())
        flows, distances = np.empty((n, n)), np.empty((n, n))

        for i in range(n):
            flows[i] = (list(map(int, f.readline().split())))
        _ = f.readline()
        for j in range(n):
            distances[j] = (list(map(int, f.readline().split())))
    return QAPdata(n, distances, flows)


class LocalSearch:
    def __init__(self, data, iters):
        self.data = data
        self.solution = initial_solution(self.data.n)
        self.iter_num = iters
        self.cost = self.data.cost_calculator(self.solution)

    def first_improvement(self):
        dont_look_bits = np.zeros(self.data.n)

        for _ in range(self.iter_num):
            if np.all(dont_look_bits):
                break
            combs = combinations(np.arange(self.data.n), 2)
            city = 0
            cnt = 0
            for item in combs:
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

                if cost < self.cost:
                    self.cost = cost
                    self.solution = cur_solution
                    break
                elif city == item[0]:
                    cnt += 1

        sol = self.solution
        cost = self.data.cost_calculator(self.solution)
        return sol, cost


def solver(data):
    ls = LocalSearch(data, 100)
    sol, cost = ls.first_improvement()
    return sol, cost


