tabuada=int(input("Tabuada do número:"))

for count in range(10):
    print("%d x %d= %d" % (tabuada, count+1, tabuada*(count+1)))