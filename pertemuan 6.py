import os
import math

def Rectangle():
    print("reactangle")
    print("______________________")
    print("|                     |")
    print("|                     | Y")
    print("|                     |")
    print("______________________")
    print("           X          ")
    
    x = int(input("x : "))
    y = int(input("y : "))
    print()
    print(f'area =  {x} x {y}')
    print("area =",x*y )
    print()
    print(f'Circumference = 2 x ( {x} + {y} )')
    print('Circumference =', 2*(x+y) )
    input("press enter...")
    
def Triangle():
    print(' |\\')
    print(' | \\')
    print(' |  \\')
    print(' |   \\')
    print('y|    \\z')
    print(' |     \\')
    print(' |      \\')
    print(' |       \\')
    print('  ---------')
    
    x = int(input("x : "))
    y = int(input("y : "))
    print()
    print(f'area =  {x} x {y}')
    print("area =",x*y )
    print()
    print('z = ✓(x² + y²)')
    print(f'z = ✓({x}² + {y}²)')
    print('z= ', math.sqrt(x**2 + y**2) )
    input("press enter to continue...")
    
def Circle():
    pass


while True:
    os.system('cls')
    print("1.Rectangle")
    print("2.Triangle")
    print("3.Circle")
    print("4.Quit")
    print()
    choice = input("please choose: ")
    if choice == '1':
        Rectangle()
        
    elif choice == '2':
        Triangle()
        
    elif choice == '3':
        Circle()
