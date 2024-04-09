num = int(input("Ingrese el numero de la ACL? "))
if num >= 1 and num <= 99:
    print("Corresponde a una ACL IPv4 estándar.")
elif num >=100 and num <= 199:
    print("Corresponde a una ACL IPv4 extendida")
else:
    print("El numero ingresado no es valido .")
