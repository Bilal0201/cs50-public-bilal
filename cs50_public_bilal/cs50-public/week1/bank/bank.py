greeting = input("Greeting: " )

greeting = greeting.split()[0]
greeting = greeting.strip(",").strip().lower()

if greeting == "hello":
    output = "$0"
elif greeting[:1] == "h":
    output = "$20"
else: output = "$100"

print(output)
