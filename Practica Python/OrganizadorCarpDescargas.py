import os
import shutil as sh

ruta_descarga = "C:\\Users\\Bedoy\\Downloads\\"

ruta = os.listdir(ruta_descarga)


ext_excel = ['.xlsx', '.csv', '.xls']
ext_stl = ['.stl', '.lys', 'ctb']
ext_imagenes = ['.png', '.jpg', '.jpeg', '.gif']
ext_zip = ['.zip', '.rar']
ext_exe = ['.exe']
ext_pdf = ['.pdf']


def ordenar():
    for i in ruta:
        for a in ext_excel:
            if i.endswith(a):
                sh.move(ruta_descarga + i, ruta_descarga + 'Archivos Excel')

    for i in ruta:
        for a in ext_stl:
            if i.endswith(a):
                sh.move(ruta_descarga + i, ruta_descarga + 'STL´s')

    for i in ruta:
        for a in ext_imagenes:
            if i.endswith(a):
                sh.move(ruta_descarga + i, ruta_descarga + 'Imagenes')

    for i in ruta:
        for a in ext_zip:
            if i.endswith(a):
                sh.move(ruta_descarga + i, ruta_descarga + 'ZIP`s')

    for i in ruta:
        for a in ext_exe:
            if i.endswith(a):
                sh.move(ruta_descarga + i, ruta_descarga + 'Instaladores')

    for i in ruta:
        for a in ext_pdf:
            if i.endswith(a):
                sh.move(ruta_descarga + i, ruta_descarga + 'pdf')

    """ for i in ruta:
        for a in ext_pdf:
            if i.endswith(''):
                sh.move(ruta_descarga + i , ruta_descarga + 'Otros') """


ordenar()


# def ordenar(archivo, ext):
#     for i in ext_excel:
#         if ext == i:
#             sh.move(ruta_descarga + archivo + ext,
#                     ruta_descarga + 'Archivos Excel')

#     for i in ext_stl:
#         if ext == i:
#             sh.move(ruta_descarga + archivo + ext, ruta_descarga + 'STL´s')

#     for i in ext_imagenes:
#         if ext == i:
#             sh.move(ruta_descarga + archivo + ext, ruta_descarga + 'Imagenes')

#     for i in ext_zip:
#         if ext == i:
#             sh.move(ruta_descarga + archivo + ext, ruta_descarga + 'ZIP´s')

#     for i in ext_exe:
#         if ext == i:
#             sh.move(ruta_descarga + archivo + ext,
#                     ruta_descarga + 'Instaladores')

#     for i in ext_pdf:
#         if ext == i:
#             sh.move(ruta_descarga + archivo + ext, ruta_descarga + 'pdf')

#     if ext != '':
#         sh.move(ruta_descarga + archivo + ext, ruta_descarga + 'Otros')


# def main():
#     for archivo in os.listdir(ruta_descarga):
#         nombre_archivo, ext = os.path.splitext(archivo)
#         ordenar(nombre_archivo, ext)


# main()
