telfonos_dict={ "Alicia": 1111111 , "Patricia": 2222222, "Martha": 3333333, "Andrés": 4444444, "Juan": 5555555}

print(len(telfonos_dict))
llave :str = "Andrés"
print(f"El teléfono de {llave} es: {telfonos_dict[llave]}")

llave :str = "Amanda"

telfonos_dict[llave] = 6666666
print(len(telfonos_dict))
print(f"El teléfono de {llave} es: {telfonos_dict[llave]}")