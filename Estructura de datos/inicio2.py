temperatura = list()
for n in range (0,5): 
    t=int(input("registre temperatura "))
    temperatura.append(t)
promedio = sum (temperatura)/len (temperatura)    
print ("resgistra la temperatura", temperatura)
print ("promedio de temperatura", promedio)
if promedio <=20 :
    print ("la temperatura es baja ") 
if promedio >=37:
    print ("la temperatura es muy alta revise la ventilacion")
else: 
 print ("todo esta bien")
