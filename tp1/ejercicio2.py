import sys
import getopt
import os

(opt, arg) = getopt.getopt(sys.argv[1:], 'i:o:')

print("opciones:", opt)

for (op, ar) in opt:
    if op in '-i':
        texto1 = ar
    elif op == '-o':
        texto2 = ar
    else:
        print("Opcion invalida")

if os.path.isfile(texto1):
    print("El archivo existe")
    file = open(texto1, 'r')
    contenido = file.read()
    file.close()
    file_2 = open(texto2, 'a+')
    file_2.write(contenido)
    print("Se copio el contenido")
    file_2.close()
else:
    print("No existe el archivo")
    