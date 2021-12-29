# intento de temporizador
import time
import pygame

# bienvenida al programa np?
print("\nTEMPORIZADOR")
rta = "S"

# sonido
pygame.mixer.init()
pygame.mixer.music.load("C:/Users/pc/Documents/Proyectos/Proyectos en Python/timer/alarma.wav")

while rta == "S" or rta == "s":
    # pregunta la cantidad de minutos
    t = int(input("Cuantos minutos?  "))
    techo = "============================="
    print(techo)
    seg = t*60
    piso = "="
    while (seg >= 0):
        # calculos
        min, seg_t = divmod(seg, 60)
        tempo = "{:02d}:{:02d}".format(min, seg_t)

        # el tempo (rizador)
        print("[|||||||\>=", tempo, "=</|||||||]", end="\r")
        # print("\n")

        # restar segundos
        time.sleep(1)
        seg = seg - 1
        if seg == 0:
            print("[|||||||\>= 00:00 =</|||||||]", end="\r")
            print("\n=============================")
            break
    
    print("\nya termino \n")
    pygame.mixer.music.play()
    rta = input("queres seguir? [S/N]  ")

print("\n==============================")
print("\chau\n")


# barra de carga (en progreso) (medio imposible)
        # print(piso, end="\r")
        # igual = "="
        # piso = piso + igual
        # if piso.count("=") > techo.count("="):
        # piso = "                              "
        # print(piso, end="\r")
        # piso = "="
