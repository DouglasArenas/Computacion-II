import sys
import getopt
import subprocess as sp
import datetime as dt

(opt, arg) = getopt.getopt(sys.argv[1:], 'c:f:l:')

print("opciones:", opt)

for (op, ar) in opt:
    if op in '-c':
        comando = ar
    elif op == '-f':
        archivo_salida = open(ar, "a")
    elif op == '-l':
        archivo_modificado = ar
    else:
        print("Opcion invalida")

proceso = sp.Popen([comando], stdout=archivo_salida, stderr=sp.PIPE, shell=True, universal_newlines=True)
error = proceso.communicate()[1]

if not error:
    fecha = dt.datatime.now()
    escribir = fecha, ": El comando:", comando, "se ha ejecutado correctamente"
    archivo_escrito = open(archivo_modificado, "a")
    archivo_escrito.write(escribir)
    archivo_escrito.write("\n")
    archivo_escrito.close()
else:
    fecha = dt.datatime.now()
    escribir = fecha, ": >>", error
    archivo_escrito = open(archivo_modificado, "a")
    archivo_escrito.write(escribir)
    archivo_escrito.write("\n")
    archivo_escrito.close()


archivo_salida.writelines("\n")
archivo_salida.close()