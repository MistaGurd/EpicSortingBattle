import random, tests


def BubbleSort(items): # Laver en funktion som får en liste af data fra items
    items = items.copy()  # Laver en kopi af listen så man ikke får justeret den originale.
    n = len(items)  # Her bliver længden af listen items gemt i variablen n. Dette bruges senere til at bestemme, hvor mange gange de indre og ydre loops skal køre.
    for x in range(n): # Begyndelse af ydre loop som kører n antal gange.
        for y in range(n - 1 - x): # Indre loop som går den usorteret del af listen igennem.
            if items[y] > items[y + 1]: # Dette tjekker, om det nuværende element (items[y]) er større end det næste element (items[y + 1]). Hvis dette er tilfældet, skal elementerne bytte plads for at sikre, at det største element "bobler" mod slutningen af listen.
                temp = items[y + 1] # Hvis items[y] er større end items[y + 1], gemmes items[y + 1] midlertidigt i variablen temp. Dette gøres for at holde styr på værdien, mens vi udfører swap (bytte).
                items[y + 1] = items[y] # Overskriver værdien i items[y + 1] med værdien af items[y]. Dette betyder, at det større element nu flyttes en position frem i listen, hvilket er nødvendigt for at "boble" det større element mod slutningen af listen
                items[y] = temp # ;Hænger sammen med den forrige linje; gemmer værdien midlertidigt så den ikke går tabt.
    return items # Når alt er sorteret bliver den nye sorteret liste gemt som items.


"""def TimSort(items):
    return sorted(items)"""

def SelectionSort(items):
    n = len(items)

    for x in range(n):
        index_of_min = x

        for y in range(x, n):
            if items[index_of_min] > items[y]:
                index_of_min = y

        # Swap the elements
        temp = items[x]
        items[x] = items[index_of_min]
        items[index_of_min] = temp
    return items



if __name__ == '__main__':
    ## Skriv navnet på den algoritme, der skal testes
    algorithm = SelectionSort

    passedTest = True
    for i in range(10):
        l = list(range(0, 10))
        lb = l.copy()
        random.shuffle(lb)
        ls = lb.copy()
        if not tests.sortsCorrectly(ls, algorithm):
            passedTest = False
            break

    if passedTest:
        print('Succes! Algoritmen sorterer korrekt.')
    else:
        print('Fejl! Algoritmen kan ikke sortere.')

    print('blandet: ', lb)
    print('sorteret:', algorithm(ls))
