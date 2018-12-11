#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

secret = random.randint(1, 20)

print "Bienvenidos a Secret Game!"

try:
    guess = int(raw_input("Introduzca el número a adivinar, ¿lo adivinarás? Tiene que ser del 1 al 20. ¡ADELANTE!: "))
    if guess >= 0:
        if guess <= 20:
            if guess == secret:
                print "¡ACERTASTE! INCREIBLE!!"
            else:
                print "OOOOHHHH! Po va ser que no... FALLASTE!! Era", secret
        else:
            print "¿Crees que son pocos numeros? No te preocupes, trabajaremos para poner mas, de momento es hasta 20. Lo siento."
    else:
        print "NO estan permitidos los numeros negativos! PERDISTE!!"
except ValueError:
    print "MAL CHAVAL/CHAVALA!! Debe ser un numero (del 1 al 20)!"
