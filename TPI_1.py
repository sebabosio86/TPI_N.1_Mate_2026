# Simulador de evaporador de leche

# Declaración de funciones


# Función que pregunta al usuario si quiere ajustar valores y reinicar el ciclo o salir de la simulación.
def continuar_o_salir():

    while True:
        continuar  = input("\n¿Ajustar valores? s/n: ").strip().lower()

        if continuar == "s":
            break


        elif continuar == "n":
            print("\n === Fin de la simulación ===\n")
            break

        else:
            print("Ingreso incorrecto")

    return continuar


# Función para validar que el valor ingresado por el usuario sea 0 o 1
def validar_ingreso_binario(valor):

    while not valor.isdigit() or int(valor) < 0 or int(valor) > 1:

        valor = input(" ❌ Error, ingresar 0 o 1: ").strip()

    valor = int(valor)  # Si se cumple la validación, el valor se convierte a número entero

    return valor


# Función de selección silo origen materia prima
def silo_producto():

    while True:
        silo = input("\nIngrese silo de origen de materia prima:\n" \
        "Silo 1: Leche entera\n" \
        "Silo 2: Leche entera\n" \
        "Silo 3: Leche descremada\n" \
        "Silo 4: Leche descremada\n" \
        "Silo: ").strip()

        if not silo.isdigit():
            print("\nError. Ingreso inválido")
            continue

        silo = int(silo)  #Se convierte el valor ingresado a número entero

        if silo in [1,2]:
            silo = 0  # Al seleccionar silo 1 o 2 (Leche entera), la variable se convierte en 0 como valor de entrada al circuito.
            break
        elif silo in [3,4]:
            silo = 1  # Al seleccionar silo 3 o 4 (Leche descremada), la variable se convierte en 1 como valor de entrada al circuito.
            break
        else:
            print(" ❌ Error. Ingreso inválido")

    return silo


# Función para seleccionar receta de producción
def receta_producto():
    receta = input("\nSeleccione receta de producto:\n" \
    "0: Leche entera\n" \
    "1: Leche descremada\n" \
    "Receta: ").strip()

    receta = validar_ingreso_binario(receta)  # La función valida que el valor ingresado sea 0 o 1

    return receta


# Función para ingresar caudal en la salida del tanque balance de leche.
def caudal_evap():

    while True:
        # Se ingresa el valor de caudal en el equipo.
        caudal = input("\nCaudal actual en salida de tanque balance (óptimo 19 - 21 m³/h): ").strip()

        # Valida que se ingrese un número
        if not caudal.isdigit():
            print(" ❌ Error. Ingreso inválido")
            continue

        caudal = int(caudal)  # Convierte el valor a número entero

        # Si los valores están fuera de rango el valor de entrada al ciucuito será 0.
        if caudal < 19:
            caudal = 0
            mensaje = "\n ⚠️ Caudal bajo: Riesgo de ensuciamiento del equipo."
            break

        elif caudal > 21:
            caudal = 0
            mensaje = "\n ⚠️ Caudal alto: Riesgo de inundación del equipo y baja concentración de leche en la salida."
            break

        # Si el caudal es el adecuado, el valor de la variable será 1 para entrar al circuito.
        else:
            caudal = 1
            mensaje = ""
            break

    return caudal, mensaje


# Ingreso temperatura de pasteurización
def temp_past():

    while True:
        # Se ingresa el valor de temperatura actual
        temp= input("\nTemperatura de pasteurización actual(óptimo 72 - 95°C) ").strip()

        # Valida que se ingrese un número
        if not temp.isdigit():
            print(" ❌ Error. Ingreso inválido")
            continue

        temp = int(temp)

        # Si los valores están fuera de rango el valor de entrada al ciucuito será 0.
        if temp < 72:
            temp = 0
            mensaje = "\n ⚠️ Baja temperatura de pasteurización: riesgo de proliferación de microorganismos patógenos."
            break

        elif temp > 95:
            temp = 0
            mensaje = "\n ⚠️ Alta temperatura de pasteurización: riesgo de degradación de proteínas."
            break

        # Si la temperatura es la adecuada, el valor de la variable será 1 para entrar al circuito.
        else:
            temp = 1
            mensaje = ""
            break

    return temp, mensaje


# Función para indicar si hay falla en algón motor
def falla_motores():

    falla = input("\n¿Hay alarma de falla de motores?\n" \
    "0: No\n" \
    "1: Si\n" \
    "Opción: ").strip()

    falla = validar_ingreso_binario(falla)  # valida que la entrada sea 0 o 1

    return falla


# Función para ingresar detección de nivel en el sensor principal del tanque balance
def sensor_nivel_1():

    sensor1 = input("\nSensor principal de nivel en tanque balance.\n" \
    "0: Sin detección de nivel\n" \
    "1: Detectando nivel\n" \
    "Opción: ").strip()

    sensor1 = validar_ingreso_binario(sensor1)  # valida que la entrada sea 0 o 1

    return sensor1

# Función para ingresar detección de nivel en el sensor de respaldo del tanque balance
def sensor_nivel_2():
    sensor2 = input("\nSensor de respaldo nivel en tanque balance.\n" \
    "0: Sin detección de nivel\n" \
    "1: Detectando nivel\n" \
    "Opción: ").strip()

    sensor2 = validar_ingreso_binario(sensor2)  # valida que la entrada sea 0 o 1

    return sensor2

# Función para activar bomba dosificadora de soda cáustica.
def dosif_soda():

    soda = input("\nActivar dosificación de soda cáustica.\n" \
    "0: No\n" \
    "1: Si\n" \
    "Opción: ").strip()

    soda = validar_ingreso_binario(soda)  # valida que la entrada sea 0 o 1

    return soda

# Función para activar bomba dosificadora de ácido nítrico.
def dosif_acido():
    acido = input("\nActivar dosificación de ácido nítrico.\n" \
    "0: No\n" \
    "1: Si\n" \
    "Opción: ").strip()

    acido = validar_ingreso_binario(acido)  # valida que la entrada sea 0 o 1

    return acido


####################################################################################################################################
# Definición de funciones de las compuertas lógicas
# El nombre de cada función nos dice a que compuerta pertenece

def compuerta_not(a):
    return not a

def compuerta_xor(a, b):
    return a ^ b

def compuerta_and(a, b):
    return a and b

def compuerta_or(a, b):
    return a or b

def compuerta_nor(a, b, c):
    return not(a or b or c)

def compuerta_nand(a, b):
    return not(a and b)


####################################################################################################################################
# Programa principal

print("\n===== SIMULADOR DE EVAPORADOR DE LECHE =====\n")

# Se definen algunas variables que se usarán en el programa
paso = 1
opcion = 0

# Se ejecuta el paso de configuración de parámetros antes de comenzar la producción
while paso == 1:
    print("=" * 60)
    print("PASO 1: Configuración previa al arranque")
    print("Selección de receta y ajuste de parámetros")
    print("=" * 60)

    # Ingreso de receta de producto llamando a la función correspondiente
    receta = receta_producto()

    # Selección de silo de origen de materia prima invocando a la función correspondiente.
    silo = silo_producto()

    # La compuerta XOR se utiliza para detectar inconsistencias entre la receta seleccionada y la materia prima.
    # Si coinciden arroja 0, significa que no hay error y se puede continuar.
    prod_y_receta_ok = compuerta_xor(receta, silo)

    # El valor de salida de la compuerta XOR pasa por unacompuerta NOT para invertir su valor.
    # Un 1 en la salida significa que la receta y el producto coinciden. Es una condición necesaria para iniciar la producción.
    prod_y_receta_ok = compuerta_not(prod_y_receta_ok)

    # Si la receta y el silo coinciden se procede al siguiente paso.
    if prod_y_receta_ok:
        print("\n ✅ Silo de origen y receta seleccionados correctamente.")

    # Si no hubo coincidencia entre la materia prima y la receta se muetsra un error.
    else:
        print("\n❌ Error: receta y materia prima no coinciden.")

        # Se pregunta al usuario si se ajustan valores o se finaliza la simulación.
        opcion = continuar_o_salir()
        if opcion == "s":
            continue
        else:
            break

    input("\nPresione ENTER para continuar...")

    # Se ingresa el caudal del equipo llamando a la función corespondiente.
    caudal_ok, mensaje_error_caudal = caudal_evap()

    # Se ingresa la temperatura de pasteurización.
    temp_ok, mensaje_error_temp = temp_past()

    # La compuerta AND se utiliza para validar que tanto el caudal de salida de producto como la temperatura de pasteurización sean óptimos.
    evap_ok = compuerta_and(caudal_ok, temp_ok)

    # Si ambos valores son correctos se valida la condición para comenzar la producción.
    if evap_ok:
        print("\n ✅ Caudal y temperatura OK")

    # Si al menos una de las entradas es 0 se mostrará el error en cuestón
    else:
        if not caudal_ok:
            print(mensaje_error_caudal)

        if not temp_ok:
            print(mensaje_error_temp)

        # Se pregunta al usuario si se ajustan valores o se finaliza la simulación.
        opcion = continuar_o_salir()
        if opcion == "s":
            continue
        else:
            break

    input("\nPresione ENTER para continuar...")

    # Se verifica si hay falla en algún motor de impulsión.
    falla = falla_motores()

    # Si hay falla en motores (1) al pasar por la compuerta NOT esta se convierte en 0 y no cumple con la condición para iniciar producción.
    # Se compuerta NOT saldrá con 1 en caso que no haya alarma, de ésta manera se cumple una de las condiciones para inicar producción
    sin_alarmas = compuerta_not(falla)

    # Si se cumple la condición que no hay alarma se puede iniciar la producción
    if sin_alarmas:
        print("\n ✅ Motores en condiciones.")

    # En caso de existir alarma se muestra un error.
    else:
        print("\n❌ Hay falla de motores. Avisar a personal de mantenimiento")
        opcion = continuar_o_salir()

        # Se pregunta al usuario si se ajustan valores o se finaliza la simulación.
        if opcion == "s":
            continue
        else:
            break

    # La última compuerta AND comprueba que se hayan cumplido las condiciones anteriores para poder iniciar la producción.
    if prod_y_receta_ok and evap_ok and sin_alarmas:

        print("\nParámetros en condiciones\n \
        \nInicio de producción")

    input("\nPresione ENTER para continuar...")
    paso = 2

# Paso de producción en proceso.
while paso == 2:
    print("=" * 60)
    print("Paso 2 - Producción")
    print("=" * 60)

    print("\n-Nivel en tanque balance")

    # Se llama a la función para mostrar si el sensor principal detecta nivel de leche en tanque balance
    sensor_1 = sensor_nivel_1()

    # Se llama a la función para mostrar si el sensor de respaldo detecta nivel de leche en tanque balance
    sensor_2 = sensor_nivel_2()

    # Las entradas de los sensores de nivel entran a una compuerta OR.
    # Si al menos un sensor detecta nivel, la salida de la compuerta es 1 y la producción continua normalmente.
    nivel_ok = compuerta_or(sensor_1, sensor_2)

    # La salida de la compuerta OR pasa por una compuerta NOT para invertir su valor.
    # Si el tanque tiene nivel, entonces no hay alarma (valor 0)
    # Si se detecta que no hay nivel, el valor de alarma_nivel será 1
    alarma_nivel = compuerta_not(nivel_ok)

    # Se revisa caudal. Si está fuera de rango aparece una falla (valor 1)
    alarma_caudal, mensaje_error_caudal = caudal_evap()
    alarma_caudal = not alarma_caudal

    # Se revisa temperatura de pasteurización. Si está fuera de rango aparece una falla (valor 1).
    alarma_temp, mensaje_error_temp  = temp_past()
    alarma_temp = not alarma_temp

    # Todos los valores de alarma entran a una compuerta NOR.
    produccion_normal = compuerta_nor(alarma_nivel, alarma_caudal, alarma_temp)

    # Mientras no haya alarmas activas (valores en 0) la producción funciona normalmente.
    if produccion_normal:
        print("\nProducción en condiciones normales")

        # Mientras se está en proceso de producción se puede decidir continuar con la marcha o ir al paso de lavado químico.
        cambiar_paso = input("Seleccione una opción.\n" \
        "0: Continuar produción\n" \
        "1: Ir a limpieza química\n" \
        "Opción: ")

        cambiar_paso = validar_ingreso_binario(cambiar_paso)

        if cambiar_paso:
            paso = 3  # Se pasa al paso de lavado
        else:
            paso = 2  # Se contin;ua en el paso actual (producción)

    # En el caso de que se active al menos una alarma (valor 1) aparece el mensaje de advertencia correspondiente.
    # Se cambia al paso de lavado por seguridad.
    else:
        print("\n ❌ ¡ATENCIÓN! Hay alarmas activadas\n")

        if alarma_nivel:
            print("\n ⚠️ No se detecta producto en tanque balance.")  # Muestra mensaje de alarma

        if alarma_caudal:
            print(mensaje_error_caudal)  # Muestra mensaje de alarma

        if alarma_temp:
            print(mensaje_error_caudal)  # Muestra mensaje de alarma

        print("\nSe detiene la producción y se envía a paso de limpieza química")

        input("Presione ENTER para continuar...")

        # Cambio al paso 3 para la limpieza química
        paso = 3

# Paso de limpieza química
while paso == 3:
    print("=" * 60)
    print("PASO 3 - Limpieza química")
    print("=" * 60)

    # Se pregunta si activar bomba dosificadora de soda cáustica.
    soda = dosif_soda()

    # Se pregunta si activar bomba dosificadora de ácido nítrico.
    acido = dosif_acido()

    # Se entra a una compuerta NAND para verificar que haya solo una bomba dosificadora en funcionamiento a la vez, o ninguna.
    lavado_normal = compuerta_nand(soda, acido)

    if lavado_normal:

        # Si ninguna bomba está activa significa que se está enjuagando el equipo con agua.
        if not soda and not acido:
            print("\nPaso actual: enjuage")
            input("Presione ENTER para continuar...")

        # Si está encendida la bomba dosificadora de soda cáustica es porque se está realizando lavado alcalino.
        elif soda and not acido:
            print("Lavado alcalino en proceso")
            input("Presione ENTER para continuar...")

        # En este caso está encendida la bomba dosificadora de ácido nítrico, realizando limpieza ácida.
        else:
            print("Lavado ácido en proceso")
            input("Presione ENTER para continuar...")

    # Cuando ambas bombas dosificadoras se activan a la vez (salida NAND 0) se detiene el equipo por seguridad.
    else:
        print("\n¡PELIGRO! Dosificación de soda cáustica y ácido nítrico en simultáneo. Riesgo de daño estructural del equipo")
        print("\nParada de emergencia")
        print("\n === Fin de la simulación ===\n")
        break




