n=int(input("introduce un numero"))

for i in range (1, 1+n ):
     print(" ".join(str(j) for j in range(1, i + 1)))