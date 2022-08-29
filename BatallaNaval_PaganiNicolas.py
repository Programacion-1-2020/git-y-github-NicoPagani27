# Estados_Del_Barco:
# 0 = Vacio
# 1 = Barco
# 2 = Tirado
# 3 = Barco Hundido

# Diagrama_Estado
# 0 --> si pone tiro pasa a 2
# 0 --> si pone barco pasa a 1
# 1 --> si pone tiro(2) pasa a 3

from random import randint
from funciones import *

print('╔═══════════════════════════════╗')
print('║ BIENVENIDO A LA BATALLA NAVAL ║')
print('╚═══════════════════════════════╝')

tipeo_incorrecto_dimension_tablero = True
while tipeo_incorrecto_dimension_tablero:
    dimension_tablero = input('𝐈𝐧𝐠𝐫𝐞𝐬𝐞 𝐝𝐢𝐦𝐞𝐧𝐬𝐢𝐨𝐧 𝐝𝐞𝐥 𝐭𝐚𝐛𝐥𝐞𝐫𝐨 (𝐞𝐧𝐭𝐫𝐞 𝟓 𝐲 𝟓𝟎): ━▶ ')
    es_letra_tablero = True
    try:
        dimension_tablero = int(dimension_tablero)
        es_letra_tablero = False
    except ValueError:
        es_letra_tablero = True

    if es_letra_tablero:
        print("𝐈𝐧𝐠𝐫𝐞𝐬𝐚𝐫 𝐍𝐮𝐦𝐞𝐫𝐨")
        tipeo_incorrecto_dimension_tablero = True
    elif 5 <= dimension_tablero <= 50:
        tipeo_incorrecto_dimension_tablero = False

tablero_j1 = [[0]*dimension_tablero for i in range(dimension_tablero)]

imprimir_tablero("━▶ 𝐄𝐬𝐭𝐞 𝐞𝐬 𝐞𝐥 𝐓𝐚𝐛𝐥𝐞𝐫𝐨 𝐞𝐧 𝐁𝐥𝐚𝐧𝐜𝐨 ◀━", tablero_j1)
while True:
    cant_barcos = int(input('𝐂𝐨𝐧 𝐜𝐮𝐚𝐧𝐭𝐨𝐬 𝐛𝐚𝐫𝐜𝐨𝐬 𝐝𝐞𝐬𝐞𝐚 𝐣𝐮𝐠𝐚𝐫? ━▶ '))
    if cant_barcos > (dimension_tablero * dimension_tablero):
        print(f'𝐒𝐞 𝐩𝐮𝐞𝐝𝐞𝐧 𝐜𝐨𝐥𝐨𝐜𝐚𝐫 𝐡𝐚𝐬𝐭𝐚 {dimension_tablero * dimension_tablero} 𝐛𝐚𝐫𝐜𝐨𝐬')
    else:
        break

print(f"𝐓𝐢𝐞𝐧𝐞𝐬 𝐪𝐮𝐞 𝐜𝐨𝐥𝐨𝐜𝐚𝐫 {cant_barcos} 𝐛𝐚𝐫𝐜𝐨𝐬")
for i in range(cant_barcos):
    print("")
    pudo_colocar_barco = False
    while not pudo_colocar_barco:
        print(f'━▶ 𝐈𝐧𝐠𝐫𝐞𝐬𝐞 𝐥𝐚 𝐮𝐛𝐢𝐜𝐚𝐜𝐢𝐨𝐧 𝐝𝐞𝐥 𝐛𝐚𝐫𝐜𝐨 {i + 1} ◀━')

        tipeo_incorrecto_columna = True
        while tipeo_incorrecto_columna:
            columna = input('\n𝐂𝐎𝐋𝐔𝐌𝐍𝐀 ━▶ ')
            es_letra = True
            try:
                columna = int(columna)
                es_letra = False
            except ValueError:
                es_letra = True

            if es_letra:
                print("𝐈𝐧𝐠𝐫𝐞𝐬𝐚𝐫 𝐍𝐮𝐦𝐞𝐫𝐨")
                tipeo_incorrecto_columna = True
            elif columna < 0 or columna > (dimension_tablero - 1):
                print("𝐈𝐧𝐠𝐫𝐞𝐬𝐚𝐬𝐭𝐞 𝐮𝐧 𝐍𝐮𝐦𝐞𝐫𝐨 𝐟𝐮𝐞𝐫𝐚 𝐝𝐞 𝐥𝐨𝐬 𝐩𝐚𝐫𝐚𝐦𝐞𝐭𝐫𝐨𝐬")
                tipeo_incorrecto_columna = True
            else:
                tipeo_incorrecto_columna = False

        tipeo_incorrecto_fila = True
        while tipeo_incorrecto_fila:
            fila = input('\n𝐅𝐈𝐋𝐀 ━▶ ')
            letra_fila = True
            try:
                fila = int(fila)
                letra_fila = False
            except ValueError:
                letra_fila = True

            if letra_fila:
                print("𝐈𝐧𝐠𝐫𝐞𝐬𝐚𝐫 𝐍𝐮𝐦𝐞𝐫𝐨")
                tipeo_incorrecto_fila = True
            elif fila < 0 or fila > (dimension_tablero - 1):
                print("𝐈𝐧𝐠𝐫𝐞𝐬𝐚𝐬𝐭𝐞 𝐮𝐧 𝐍𝐮𝐦𝐞𝐫𝐨 𝐟𝐮𝐞𝐫𝐚 𝐝𝐞 𝐥𝐨𝐬 𝐩𝐚𝐫𝐚𝐦𝐞𝐭𝐫𝐨𝐬")
                tipeo_incorrecto_fila = True
            else:
                tipeo_incorrecto_fila = False

        pudo_colocar_barco = colocar_barco(tablero_j1, columna, fila)
    imprimir_tablero(f"𝐓𝐚𝐛𝐥𝐞𝐫𝐨 𝐥𝐮𝐞𝐠𝐨 𝐝𝐞 𝐢𝐧𝐠𝐫𝐞𝐬𝐚𝐫 𝐞𝐥 𝐛𝐚𝐫𝐜𝐨 {i + 1}", tablero_j1)

imprimir_tablero("𝐓𝐀𝐁𝐋𝐄𝐑𝐎 𝐈𝐍𝐈𝐂𝐈𝐀𝐋", tablero_j1)

tablero_computadora = [[0]*dimension_tablero for i in range(dimension_tablero)]
print('𝐂𝐎𝐌𝐏𝐔: 𝐄𝐬𝐭𝐨𝐲 𝐮𝐛𝐢𝐜𝐚𝐧𝐝𝐨 𝐦𝐢𝐬 𝐛𝐚𝐫𝐜𝐨𝐬...')
for i in range(cant_barcos):
    pudo_colocar_barco_compu = False
    while not pudo_colocar_barco_compu:
        columna = randint(0, (dimension_tablero - 1))
        fila = randint(0, (dimension_tablero - 1))
        pudo_colocar_barco_compu = colocar_barco(tablero_computadora, columna, fila)
print('𝐂𝐎𝐌𝐏𝐔: 𝐋𝐢𝐬𝐭𝐨!!!')

hay_ganador = False
while not hay_ganador:
    print('𝐈𝐧𝐠𝐫𝐞𝐬𝐞 𝐮𝐛𝐢𝐜𝐚𝐜𝐢𝐨𝐧 𝐝𝐞𝐥 𝐭𝐢𝐫𝐨')

    verificacion_columna = False
    while not verificacion_columna:
        columna = input('\n𝐂𝐎𝐋𝐔𝐌𝐍𝐀 ━▶ ')
        try:
            columna = int(columna)
            if columna < 0 or columna > dimension_tablero - 1:
                print('𝐈𝐧𝐠𝐫𝐞𝐬𝐚𝐫 𝐝𝐞 𝐍𝐮𝐞𝐯𝐨')
                verificacion_columna = False
            else:
                verificacion_columna = True
        except ValueError:
            verificacion_columna = False
            print('𝐈𝐧𝐠𝐫𝐞𝐬𝐚𝐫 𝐝𝐞 𝐍𝐮𝐞𝐯𝐨')

    verificacion_fila = False
    while not verificacion_fila:
        fila = input('\n𝐅𝐈𝐋𝐀 ━▶ ')
        try:
            fila = int(fila)
            if fila < 0 or fila > dimension_tablero - 1:
                print('𝐈𝐧𝐠𝐫𝐞𝐬𝐚𝐫 𝐝𝐞 𝐍𝐮𝐞𝐯𝐨')
                verificacion_fila = False
            else:
                verificacion_fila = True
        except ValueError:
            verificacion_fila = False
            print('𝐈𝐧𝐠𝐫𝐞𝐬𝐚𝐫 𝐝𝐞 𝐍𝐮𝐞𝐯𝐨')
    resultado_tiro = tiro(tablero_computadora, columna, fila)
    print(resultado_tiro)
    imprimir_tablero('𝐀𝐬𝐢 𝐡𝐚 𝐪𝐮𝐞𝐝𝐚𝐝𝐨 𝐞𝐥 𝐭𝐚𝐛𝐥𝐞𝐫𝐨 𝐝𝐞 𝐥𝐚 𝐜𝐨𝐦𝐩𝐮𝐭𝐚𝐝𝐨𝐫𝐚:', tablero_computadora, ocultar_barcos=True)

    if verificar_ganador(tablero_computadora):
        print("GANASTE!!!🎉🎉🎉")
        imprimir_tablero('𝐓𝐚𝐛𝐥𝐞𝐫𝐨 𝐝𝐞 𝐥𝐚 𝐜𝐨𝐦𝐩𝐮𝐭𝐚𝐝𝐨𝐫𝐚', tablero_computadora)
        hay_ganador = True
        break

    print('𝐂𝐎𝐌𝐏𝐔: 𝗔𝗵𝗼𝗿𝗮 𝗲𝘀 𝗺𝗶 𝘁𝘂𝗿𝗻𝗼...')

    columna = randint(0, (dimension_tablero - 1))
    fila = randint(0, (dimension_tablero - 1))
    print(f'𝐂𝐎𝐌𝐏𝐔: 𝐓𝐞 𝐭𝐢𝐫𝐨 𝐚𝐥 {columna}, {fila}')
    resultado_tiro = tiro(tablero_j1, columna, fila)
    print(resultado_tiro)
    imprimir_tablero("𝐓𝐮 𝐭𝐚𝐛𝐥𝐞𝐫𝐨 𝐡𝐚 𝐪𝐮𝐞𝐝𝐚𝐝𝐨 𝐚𝐬𝐢", tablero_j1)
    if verificar_ganador(tablero_j1):
        print("𝐓𝐞 𝐠𝐚𝐧𝐨 𝐮𝐧𝐚 𝐦𝐚𝐪𝐮𝐢𝐧𝐚 JAJA🌚🌚")
        hay_ganador = True
        break
