for i in range(1, 101):
    fizz = i % 3 == 0
    buzz = i % 5 == 0
    
    if fizz and buzz:
        print("fizzbuzz")
    elif buzz:
        print("buzz")
    elif fizz:
        print("fizz")
    else:
        print(i)
        