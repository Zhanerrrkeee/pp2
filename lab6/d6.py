for i in range(65,91): 
    with open(chr(i)+'.txt', 'x') as f: 
        f.write("Hello world")
