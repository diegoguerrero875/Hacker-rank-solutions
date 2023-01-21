#from hakcer rank migratory birds problem
def migratoryBirds(arr):
    cont = {}
    for i in  arr:
        if i not in cont:
            cont[i] = 1
        else:
            cont[i] += 1

    max_sighting = max(cont, key=cont.get)

    most_common_max_sighting = [k for k, v in cont.items() if v ==         cont[max_sighting]]
    most_common_max_sighting.sort()
    return most_common_max_sighting[0]
