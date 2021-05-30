# Лабораторная работа №3: Генетические алгоритмы
### 18ПМИ Богородицкая Екатерина, Сазанов Дмитрий, Селивановская Дарья


```python
from iterated_local_search import *
import glob
from pathlib import Path
```


```python
benchmarks = glob.glob('data/*')


best_solutions = { 
    'tai100a': 21052466,
    'tai20a': 703482,
    'tai40a': 3139370,
    'tai60a': 7205962,
    'tai80a': 13499184
}

data = list() #все данные
for file in benchmarks:
    data.append(QAPreader(file))
```


```python
benchmarks
```




    ['data\\tai100a',
     'data\\tai20a',
     'data\\tai40a',
     'data\\tai60a',
     'data\\tai80a']



## Локальный поиск


```python
Path("local_solution").mkdir(parents=True, exist_ok=True)
for i in range(len(benchmarks)):
    filename = benchmarks[i][5:]+'_solution'
    print(f"Working on file {filename}")
    solution, cost = solver(data[i])
    print(f"Best solution for it: {best_solutions[benchmarks[i][5:]]}")
    print(f"Our solution for it: {cost}")
    np.savetxt('local_solution/'+ filename, solution, fmt='%d', newline=' ')
    print("---------------------------")
```

    Working on file tai100a_solution
    Best solution for it: 21052466
    Our solution for it: 22885716.0
    ---------------------------
    Working on file tai20a_solution
    Best solution for it: 703482
    Our solution for it: 750010.0
    ---------------------------
    Working on file tai40a_solution
    Best solution for it: 3139370
    Our solution for it: 3348194.0
    ---------------------------
    Working on file tai60a_solution
    Best solution for it: 7205962
    Our solution for it: 7637358.0
    ---------------------------
    Working on file tai80a_solution
    Best solution for it: 13499184
    Our solution for it: 14531526.0
    ---------------------------
    

## Итеративный локальный поиск


```python
Path("iterated_local_solution").mkdir(parents=True, exist_ok=True)
for i in range(len(benchmarks)):
    filename = benchmarks[i][5:]+'_solution'
    print(f"Working on file {filename}")
    solution, cost = solver2(data[i])
    print(f"Best solution for it: {best_solutions[benchmarks[i][5:]]}")
    print(f"Our solution for it: {cost}")
    np.savetxt('iterated_local_solution/'+ filename, solution, fmt='%d', newline=' ')
    print("---------------------------")
```

    Working on file tai100a_solution
    Best solution for it: 21052466
    Our solution for it: 23906214.0
    ---------------------------
    Working on file tai20a_solution
    Best solution for it: 703482
    Our solution for it: 814792.0
    ---------------------------
    Working on file tai40a_solution
    Best solution for it: 3139370
    Our solution for it: 3665794.0
    ---------------------------
    Working on file tai60a_solution
    Best solution for it: 7205962
    Our solution for it: 8385192.0
    ---------------------------
    Working on file tai80a_solution
    Best solution for it: 13499184
    Our solution for it: 15334994.0
    ---------------------------
    
