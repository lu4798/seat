df = [
    [41,2,0,"AZL",5,0],
    [47,3,4,"VR",10,1],
    [60,5,1,"AZL",20,1],
    [76,7,0,"VR",15,0],
    [77,8.17,0,"AZL",20,0],
    [78,7.17,1,"VR",16,1],
    [20,2,0,"VR",15,0],
    [22,1,2,"AZL",3,1],

    [23,2,0,"AZL",5,0],
    [30,3,4,"VR",10,1],
    [62,5,1,"AZL",20,1],
    [34,7,0,"VR",15,0],
    [31,8.17,0,"AZL",20,0],
    [78,7.17,1,"VR",16,1],
    [19,2,0,"VR",6,0],
    [22,1,2,"AZL",3,1]
]

if __name__== '__main__':

    latitud = float (input("Introduce la latitud"))
    longitud = float (input("Introduce la longitud"))
    maxDistancia = float(input("Introduce la distancia máxima en m: "))
    zona= []
    final = []
    gratis = []
    facil = []
    cercanos = []
    top = []
    gratisFacil = []
    gratisCercanos = []
    facilCercanos = []

    for id in (df):
        destino = (latitud,longitud)
        actual = (id[0], id[1])
        margen = maxDistancia/1000
        if(latitud + margen > id[0] and latitud - margen < id[0]
                and longitud + margen > id[1] and longitud - margen < id[1]):
            zona.append(id)

    for plaza in zona:
        if plaza[5] == 0:
            gratis.append(plaza)
        if plaza[4] > 10:
            facil.append(plaza)
        if (latitud - plaza[0]).__abs__() < margen/2 and (longitud-plaza[1]).__abs__() < margen/2:
            cercanos.append(plaza)

    print(cercanos)
    # Enseñamos los que aparezcan en varias categorias
    for plaza in zona:
        if plaza in gratis and plaza in facil:
            gratisFacil.append(plaza)
        if plaza in gratis and plaza in cercanos:
            gratisCercanos.append(plaza)
        if plaza in facil and plaza in cercanos:
            facilCercanos.append(plaza)
        if plaza in facil and plaza in cercanos and plaza in gratis:
            top.append(plaza)

    if zona.__len__() > 0:
        print("Resultados")
        print(zona)

    if top.__len__() > 0:
        print("Top")
        print(top)

    if gratisFacil.__len__() > 0:
        print("Gratis y  con muchas plazas")
        print(gratisFacil)

    if gratisCercanos.__len__() > 0:
        print("Gratis y muy cercanos")
        print(gratisCercanos)

    if facilCercanos.__len__() > 0:
        print("Con muchas plazas y muy cercanos")
        print(facilCercanos)






