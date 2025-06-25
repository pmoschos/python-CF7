# import my_calculations
from my_calculations import my_add_function as my_add, num1

num2 = 10

# res = my_calculations.my_add_function(num2, my_calculations.num1)
# res = my_add_function(num1, num2)
res = my_add(num1, num2)
print(res) # 110
print(__name__)