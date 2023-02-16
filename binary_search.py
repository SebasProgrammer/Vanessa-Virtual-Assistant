letters = { 'a': 1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,
            'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'ñ':15, 'o':16,
            'p':17, 'q':18, 'r':19, 's':20, 't':21, 'u':22, 'v':23, 'w':24,
            'x':25, 'y':26, 'z':27}

sortWords= [['abajo', 'adiós vanessa', 'arriba'],
            ['baja', 'bajo', 'barra de busqueda', 'borra', 'borrar', 'buscar'],
            ['cambia aplicación', 'cambia app', 'cambia ventana', 'cambiar aplicación', 'cambiar app', 'cambiar ventana', 'cambio aplicación', 'cambio app', 'cambio ventana', 'cerrar aplicación', 'cerrar app', 'cerrar pestaña', 'cerrar ventana', 'cierra aplicación', 'cierra app', 'cierra pestaña', 'cierra ventana', 'cierro pestañá', 'clic', 'corre', 'center'],
            [],
            ['enter', 'escribe', 'escribir'],
            [],
            ['google'],
            [],
            [],
            [],
            [],
            ['letra'],
            ['minimiza ventana', 'minimizar ventana'],
            ['nueva pestaña', 'nombre', 'nombres'],
            [],
            ['otra vez'],
            ['pantalla completa', 'pausa', 'pestaña'],
            ['qué hora es'],
            [],
            ['silencio', 'silencio vanessa', 'spotify', 'sube'],
            ['tab', 'tecla'],
            [],
            [],
            ['whatsapp', 'whatsapp web'],
            [],
            ['youtube'],
            []
        ]

def findAction(n):
    if type(n) == str and len(n)>0 and n!= ' ':
        number = letters.get(n[0])-1
        ret = sortWords[number]
        for _ , v in enumerate(ret):
            if n in v:
                return True
    return False
