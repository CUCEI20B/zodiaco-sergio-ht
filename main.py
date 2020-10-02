dia = int(input())
mes = input()


if(mes == "enero"):
    if(dia < 20):
        print("capricornio")
    else:
        print("acuario")
elif(mes == "febrero"):
    if(dia < 20):
        print("acuario")
    else:
        print("piscis")
elif(mes == "marzo"):
    if(dia < 21):
        print("piscis")
    else:
        print("aries")
elif(mes == "abril"):
    if(dia < 21):
        print("aries")
    else:
        print("tauro")
elif(mes == "mayo"):
    if(dia < 21):
        print("tauro")
    else:
        print("geminis")
elif(mes == "junio"):
    if(dia < 21):
        print("geminis")
    else:
        print("cancer")
elif(mes == "julio"):
    if(dia < 23):
        print("cancer")
    else:
        print("leo")
elif(mes == "agosto"):
    if(dia < 23):
        print("leo")
    else:
        print("virgo")
elif(mes == "septiembre"):
    if(dia < 23):
        print("virgo")
    else:
        print("libra")
elif(mes == "octubre"):
    if(dia < 23):
        print("libra")
    else:
        print("scorpio")
elif(mes == "noviembre"):
    if(dia < 23):
        print("scorpio")
    else:
        print("sagitario")
elif(mes == "diciembre"):
    if(dia < 22):
        print("sagitario")
    else:
        print("capricornio")
