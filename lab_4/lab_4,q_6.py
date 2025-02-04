def printer():
    for i in range(1,13):
        if i == 12:
            print(i,"noon")
            break
        print(i,"AM")
    for i in range(1,13):
        if i == 12:
            print(i,"midnight")
            break
        print(i,"PM")
printer()
