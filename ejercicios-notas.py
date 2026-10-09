nota = float(input("Ingrese la nota: "))

if nota < 0 or nota > 10:
    print("incorrecto")
elif nota < 5:
        print("Insuficiente")
elif nota < 6:
        print("Suficiente")
elif nota < 7:
        print("Bien")
elif nota < 9:
        print("Notable")
else:
        print("Sobresaliente")


box = ["hola","20","casa","true","David"]
print(box[0])
print(box[1])
print(box[2])
print(box[3])
print(box[4])