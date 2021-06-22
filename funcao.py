valor = float(input("Qual valor a ser retirado?"))
cedulas = 0
valorcedatual = 200
valorsaiu = valor
moeda = "cedula(s)"

while True:
    if valorcedatual <= valorsaiu:
        cedulas += 1
        valorsaiu -= valorcedatual
    else:
        if cedulas > 0:
            print("%d de %s é de R$ %5.2f" % (cedulas,moeda,valorcedatual)),
        if valorsaiu == 0:
            break
        if valorcedatual == 200:
            valorcedatual = 100
        elif valorcedatual == 100:
            valorcedatual = 50
        elif valorcedatual == 50:
            valorcedatual = 20
        elif valorcedatual == 20:
            valorcedatual = 10
        elif valorcedatual == 10:
            valorcedatual = 5
        elif valorcedatual == 5:
            valorcedatual = 2
        elif valorcedatual == 2:
            valorcedatual = 1
            moeda = "moeda (s)"
        elif valorcedatual == 1:
            valorcedatual = 0.50
            moeda = "moeda (s)"
        elif valorcedatual == 0.50:
            valorcedatual = 0.25
            moeda = "moeda (s)"
        elif valorcedatual == 0.25:
            valorcedatual = 0.10
            moeda = "moeda (s)"
        elif valorcedatual == 0.10:
            valorcedatual = 0.05
            moeda = "moeda (s)"
        elif valorcedatual == 0.05:
            valorcedatual = 0.01
            moeda = "moeda (s)"
        elif valorcedatual == 0.01:
            valorcedatual = 0.01
            moeda = "moeda (s)"


        cedulas = 0
