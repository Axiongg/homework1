# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 08:22:36 2024

@author: student
"""



def solve_quadratic(a, b, c):
    # 計算判別式
    discriminant = (b**2) - (4*a*c)
    
    # 判斷判別式的值決定方程式有幾個解
    if discriminant > 0:
        # 有兩個實根
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # 有一個重根
        root = -b / (2*a)
        return root,
    else:
        # 有兩個虛根
        real_part = -b / (2*a)
        imaginary_part = cmath.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# 輸入a, b, c的值
a = float(input("請輸入a的值: "))
b = float(input("請輸入b的值: "))
c = float(input("請輸入c的值: "))

# 解方程式
roots = solve_quadratic(a, b, c)

# 顯示結果
if len(roots) == 2:
    print("方程式有兩個實根:")
    print("x1 =", roots[0])
    print("x2 =", roots[1])
elif len(roots) == 1:
    print("方程式有一個實根:")
    print("x =", roots[0])
else:
    print("方程式有兩個虛根:")
    print("x1 =", roots[0])
    print("x2 =", roots[1])
