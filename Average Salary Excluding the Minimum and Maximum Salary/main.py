salary = [1000,2000,3000]

def calc(salary):
    salary.remove(min(salary))
    salary.remove(max(salary))

    return sum(salary)/len(salary)


print(calc(salary))