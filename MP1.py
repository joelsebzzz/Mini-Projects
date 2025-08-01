def unit_converter():
    while True:
        print("""
Welcome to Unit Converter
1. Length Converter
2. Weight Converter
3. Temperature Converter
4. Exit""")
        ch = int(input("Enter Your Choice from 1-4: "))

        if ch == 1:
            while True:
                print("""
1. cm to m  
2. m to cm  
3. inch to cm  
4. cm to inch
5. Previous Menu""")
                lench = int(input("Enter your Choice from 1-5: "))
                if lench == 1:
                    v = float(input("Enter the value in cm: "))
                    ans = lambda x: x / 100
                    print(ans(v), "m")
                elif lench == 2:
                    v = float(input("Enter the value in m: "))
                    ans = lambda x: x * 100
                    print(ans(v), "cm")
                elif lench == 3:
                    v = float(input("Enter the value in inch: "))
                    ans = lambda x: x * 2.54
                    print(ans(v), "cm")
                elif lench == 4:
                    v = float(input("Enter the value in cm: "))
                    ans = lambda x: x / 2.54
                    print(ans(v), "inch")
                elif lench == 5:
                    break
                else:
                    print("Invalid Choice!")

        elif ch == 2:
            while True:
                print("""
1. kg to lb  
2. lb to kg
3. Previous Menu""")
                weich = int(input("Enter your Choice from 1-3: "))
                if weich == 1:
                    v = float(input("Enter the value in kg: "))
                    ans = lambda x: x * 2.205
                    print(ans(v), "lb")
                elif weich == 2:
                    v = float(input("Enter the value in lb: "))
                    ans = lambda x: x / 2.205
                    print(ans(v), "kg")
                elif weich == 3:
                    break
                else:
                    print("Invalid Choice!")

        elif ch == 3:
            while True:
                print("""
1. Celsius to Fahrenheit  
2. Fahrenheit to Celsius
3. Previous Menu""")
                temch = int(input("Enter your Choice from 1-3: "))
                if temch == 1:
                    v = float(input("Enter the value in Celsius: "))
                    ans = lambda x: (x * 9/5) + 32
                    print(ans(v), "F")
                elif temch == 2:
                    v = float(input("Enter the value in Fahrenheit: "))
                    ans = lambda x: (x - 32) * 5/9
                    print(ans(v), "C")
                elif temch == 3:
                    break
                else:
                    print("Invalid Choice!")

        elif ch == 4:
            print("Exiting...")
            break
        else:
            print("Invalid main choice!")

unit_converter()
