from flask import Flask, redirect
import empoind

if __name__ == "__main__":
  print()

print("Bienvenido a tu cine Favorito")

menu = """
  1. Cartelera
  2. Iniciar Sesion
  3. Crear Usuario
  4. Comprar Boletos

Elige una opción: """


opcion = input(menu)
if opcion == "1":
  print("empoind")
  print("segundo acto")
elif opcion == "2":
  print("argentinos", 65)
elif opcion == "3":
  print("mexicanos", 24)
else:
  print("Ingresa un opcion correta por favor")
