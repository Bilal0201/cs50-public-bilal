def ener(m):
    energy = mass * 300000000**2
    return energy

mass = int(input("m: "))
print(f"E: {ener(mass)}")

