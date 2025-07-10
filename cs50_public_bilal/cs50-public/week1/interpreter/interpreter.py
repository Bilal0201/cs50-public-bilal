exp = input("Expressions: ")
x, y, z = exp.split(" ")
x = float(x)
z = float(z)

match y:
    case "+":
        print(round(x+z, 1))
    case "-":
        print(round(x-z, 1))
    case "*":
        print(round(x*z, 1))
    case "/":
        print(round(x/z, 1))
