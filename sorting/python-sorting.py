# li = [9,1,8,2,7,3,6,4,5]

# s_li = sorted(li)
# s_li = sorted(li, reverse=True)

# print('Sorted Variable:\t', s_li)

# li.sort()

# print('Original Variable:\t', li )

# tup = (9,1,8,2,7,3,6,4,5)
# s_tup = sorted(tup)

# print('OG Tuple:\t',  tup)
# print('Sorted Variable:\t', s_tup)

# di = {'name': 'Alex', 'job': 'Dev', 'age': None, 'os': 'Mac'}
# s_di = sorted(di)

# print('OG Di:\t', di)
# print('Sorted Di:\t', s_di)

# li = [-6,3,-4,1,-5,2]
# s_li = sorted(li, key=abs)

# print('OG li:\t', li)
# print('Sorted li:\t', s_li)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)
    
from operator import attrgetter    

e1 = Employee('Carl', 27, 65000)
e2 = Employee('Sarah', 25, 45000)
e3 = Employee('Jordan', 30, 70000)

employees = [e1,e2,e3]

# def e_sort(emp):
#     return emp.salary

s_employees = sorted(employees, key=attrgetter('salary'))

print('OG employees:\t', employees)
print('Sorted employees:\t', s_employees)