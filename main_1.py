import random

contraseña = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
usuario = input("ingrese su nombre de usuario:")
largo = int(input("ingrese la longitud de la contraseña:"))
contra = ""
for i in range(largo):
    contra += random.choice(contraseña)
print("Hola", usuario, "tu contraseña es:", contra)