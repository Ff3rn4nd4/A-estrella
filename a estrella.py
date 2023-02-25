#es necesario importar la liberia time para que muestre el tiempo que tardo en la ejecucion
import time
start_time = 0

#A* 
mochila = []
beneficio = [33,24,36,37,12]
peso = [15,20,17,8,31]

def estrella(beneficio,peso):
    camino = [0]
    otherpath = []
    acumulado = 0
    if len(beneficio) != len(peso):
        return "No se puede"
    for j in range(len(beneficio)):
        nodo = 0
        costo = []
        for i in range(len(beneficio)):
            costo.append(beneficio[i]/peso[i])
        for i in range(len(costo)):
            if camino[j] < costo[i]+acumulado:
                nodo = i
                del camino[j]
                camino.insert(j,costo[i]+acumulado)
        camino.append(0)
        otherpath.append(beneficio[nodo])
        acumulado = beneficio[nodo] + acumulado
        del beneficio[nodo]
        del peso[nodo]
    return otherpath
print(estrella(beneficio,peso))
print("--------%s seconds -----"%(time.time() - start_time))
