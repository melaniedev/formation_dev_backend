salle = []
width = 8
height = 9

def init_salle(salle):
    for i in range(width):
        rangee = []
        for j in range(height):
            rangee.append("_")
        salle.append(rangee)
    return salle

def print_salle(salle):
    for i in range(width):
        print(str(i) + " ", end='')
        for j in range(height):
            print("[", salle[i][j], "]", end='')
        print()

    for k in range(0,height):
        print("    " + str(k), end='')
    print()


salle = init_salle(salle)
print_salle(salle)
success = True
while(success):
    print("Combien de places voulez vous acheter?")
    nb_places = int(input())
    print("A quelle rangée voulez vous aller?")
    rangee_id = int(input())

    print("-------------------------------------")

    i = 0
    if salle[rangee_id].count("_") >= nb_places:
        while salle[rangee_id][i] != "_":
            i += 1
        while nb_places != 0:
            salle[rangee_id][i] = "X"
            nb_places -= 1
            i += 1

        print_salle(salle)
    else:
        print("There is no enough places")
        success = False
