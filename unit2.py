########################## Gauss-Jacobi Method ###########################
    
def gauss_jacobi_method():  

    def f(y, z):
        return (1/5) * (20 + y + z)  # write x =
    def g(x, z):
        return (1/5) * (2 + x + z)  # write y =
    def h(x, y):
        return (1/5) * (8 + x + y)  # write z =
    
    x = float(input('put value of x_0 given in question if not take x_0 = 0, x_0 = '))    
    y = float(input('put value of y_0 given in question if not take y_0 = 0, y_0 = '))    
    z = float(input('put value of z_0 given in question: if not take z_0 = 0, z_0 = '))  
    r = int(input("How many place want to round up: "))
    
    n = 0 
    while True:
        print('n = ', n)
        print('x_n =' , f'%.{r}f' % x)
        print('y_n =' , f'%.{r}f' % y)
        print('z_n =' , f'%.{r}f' % z)
    
        a = f(y, z)
        b = g(x, z)
        c = h(x, y)
    
        if abs(x - a) < 0.00001 and abs(y - b) < 0.00001 and abs(z - c) < 0.00001:
            break
    
        x = a
        y = b
        z = c
        
        n += 1
    
        print()
    
#################### gauss seidel iteration method ##########################
def gauss_seidel_iteration_method():  

    def f(y, z):
        return (1/20) * (17 - y + 2*z)   # write x = 
    def g(x, z):
        return (1/20) * (-18 - 3*x + z)   # write y =
    def h(x, y):
        return (1/20) * (25 + 3*y - 2*x)  # write z =
    
    x = float(input('put value of x_0 given in question if not take x_0 = 0, x_0 = '))    
    y = float(input('put value of y_0 given in question if not take y_0 = 0, y_0 = '))    
    z = float(input('put value of z_0 given in question: if not take z_0 = 0, z_0 = '))  
    r = int(input("How many place want to round up: "))
    
    n = 0 
    while True:
        print('n = ', n)
        print('x_n =' , f'%.{r}f' % x)
        print('y_n =' , f'%.{r}f' % y)
        print('z_n =' , f'%.{r}f' % z)
    
        a = f(y, z)
        if abs(x-a) < 0.000001:
            break
        x = a
        b = g(x, z)
        y = b
        c = h(x, y)
        z = c

        n += 1
    
        print() 

########################## Newton-Raphson method ######################

def newton_raphson_method():

    import math

    a = float(input('put L_0 = 0, 1, 2, 3, or 4: L_0 = '))
    r = int(input("How many place want to round up: "))
    print()

    def f(x):
        return -x**3 +3*x**2 + 6*x - 16
        ######################################## write p3(lembda) or p4(lembda)
        # x**5 - 5*x**4 + 11*x**3 - 26*x**2 + 52*x - 40
        # x**3 - 5*x - 1
        # math.cos(x) - x*math.exp(x)

    def df(x):
        return -3*x**2 + 6*x + 6
        ######################################## write d' of p3(lembda) or p4(lembda)
        # 5*x**4 - 20*x**3 + 33*x**2 - 52*x + 52
        # 3*x**2 - 5
        # -math.sin(x) - (x + 1)*math.exp(x)

    if df(a) != 0:
        n = 0
        while True:
            print("n = ", n)

            print("x_n = ", f'%.{r}f' % a)

            b = a - (f(a)/df(a))

            print("x_n+1 = ", f'%.{r}f' % b)

            print("|x_n - x_n+1| = ", f'%.{r}f' % abs(a - b))

            if abs(a - b) < 0.000001:
                break
            a = b
            n += 1

            print()

        print()
        print("Hence, the approximate root of the equation is x = ",
              f'%.{r}f' % b)

    else:
        print("Put the value of a such that: f'(a) is not equal to 0") 

##################################################
def eigen_values_for_symmetric_matrices():
    import math
    def p0(x):
        return 1
    def p1(x, a1):
        return a1 - x 
    def p2(x, a2, b2):
        return (a2 - x)*p1(x, a1) - b2**2 * p0(x)   

    def p3(x, a3, b3, p1):
        return (a3 - x)*p2(x, a2, b2) - b3**2 * p1(x, a1)    
    
    a1 = 1
    a2 = -3/5
    a3 = 13/5
    b2 = -math.sqrt(5)
    b3 = -6/5
    r = int(input("How many place want to round up: "))
    x = int(input("lembda = "))
    
    while x < 8:
        print("lembda = ", x)
        print("p0 =", f'%.{r}f' % p0(x), "", "p1 =", f'%.{r}f' % p1(x, a1), "", "p2 =", f'%.{r}f' % p2(x, a2, b2), "", "p3 =", f'%.{r}f' % p3(x, a3, b3, p1))
        print()
        x += 1

#########################################################################
gauss_jacobi_method()



      