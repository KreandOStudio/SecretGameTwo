#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

secret = randint(1, 20)
seguimos = True

def comparamos_numeros (numero, secreto):
    mayor = None
    if numero > secreto:
        mayor = "mayor"
    elif numero < secreto:
        mayor = "menor"
    else:
        mayor = "iguales!"
    return mayor

print "Bienvenidos a Secret Game!"

while seguimos:
    no_es_correcto = True
    while no_es_correcto:
        try:
            guess = int(raw_input("Introduzca el número a adivinar, ¿lo adivinarás? Tiene que ser del 1 al 20. ¡ADELANTE!: "))
            no_es_correcto = False
        except ValueError:
            print "MAL CHAVAL/CHAVALA!! Debe ser un numero (del 1 al 20)!"

    if guess >= 0:
        if guess <= 20:
            if guess == secret:
                print "¡ACERTASTE! INCREIBLE!!"
                seguimos = False
            else:
                print "OOOOHHHH! Po va ser que no... FALLASTE!! Tu numero es {}".format(comparamos_numeros(guess, secret))
        else:
            print "¿Crees que son pocos numeros? No te preocupes, trabajaremos para poner mas, de momento es hasta 20. Lo siento."
    else:
        print "NO estan permitidos los numeros negativos! PERDISTE!!"

