import random, tests


"""def BubbleSort(items): # Laver en funktion som får en liste af data fra items
    items = items.copy()  # Laver en kopi af listen så man ikke får justeret den originale.
    n = len(items)  # Her bliver længden af listen items gemt i variablen n. Dette bruges senere til at bestemme, hvor mange gange de indre og ydre loops skal køre.
    for x in range(n): # Begyndelse af ydre loop som kører n antal gange.
        for y in range(n - 1 - x): # Indre loop som går den usorteret del af listen igennem.
            if items[y] > items[y + 1]: # Dette tjekker, om det nuværende element (items[y]) er større end det næste element (items[y + 1]). Hvis dette er tilfældet, skal elementerne bytte plads for at sikre, at det største element "bobler" mod slutningen af listen.
                temp = items[y + 1] # Hvis items[y] er større end items[y + 1], gemmes items[y + 1] midlertidigt i variablen temp. Dette gøres for at holde styr på værdien, mens vi udfører swap (bytte).
                items[y + 1] = items[y] # Overskriver værdien i items[y + 1] med værdien af items[y]. Dette betyder, at det større element nu flyttes en position frem i listen, hvilket er nødvendigt for at "boble" det større element mod slutningen af listen
                items[y] = temp # ;Hænger sammen med den forrige linje; gemmer værdien midlertidigt så den ikke går tabt.
    return items # Når alt er sorteret bliver den nye sorteret liste gemt som items."""


"""def TimSort(items):
    return sorted(items)"""

"""def SelectionSort(items): # Laver en funktion som får en liste af data fra items
    n = len(items) # Her bliver længden af listen items gemt i variablen n. Dette bruges senere til at bestemme, hvor mange gange de indre og ydre loops skal køre.

    for x in range(n): # En "for" løkke som iterere n antal gange. Variablen x repræsenterer det aktuelle indeks i iterationen.
        index_of_min = x # Gemmer variable x som mindste værdi. Dette er en kodisk antagelse.

        for y in range(x, n): # "For" løkke som itererer et interval mellem x og n, hvor y derefter tjekker om der er nogle værdier som kan byttes.
            if items[index_of_min] > items[y]: # Hvis index_of_min er større end y i items:
                index_of_min = y # Gem index_of_min som y i stedet for x.

        items[x],items[index_of_min] = items[index_of_min],items[x] # Python udfører swap
    return items # Retunere den sorterede liste."""

def MergeSort(items): #Laver hovedfunktion MergeSort som er en liste af items som inputs og returnere en sorterede listen
    """Sorts a list of items using the MergeSort algorithm.
    Args:
        items (list): The list of items to be sorted.
    Returns:
        list: The sorted list of items."""
    # Base case: If the list has 1 or 0 items, it's already sorted.
    if len(items) <= 1:# Dette er hoved rekursion som tjekker som input i listen er 1 eller 0, så er det allerede sorterede og returnere til den originale listen
        return items

    mid = len(items) // 2 #Her dividere listen i to halvdele ved brug af variable mid. Vi bruger integer division (//) for sikker sig at det en integer
    left_half = items[:mid]# Her laver vi to lister som venstre og højre som indholder første og anden halvdel af den originale liste
    right_half = items[mid:]

    # Recursively sort the two halves.
    left_half = MergeSort(left_half)# Vi gentagende kalder på MergeSort på begge venstre og højre halvdel
    right_half = MergeSort(right_half)# Dette vil sortere hver halvdel af listen selvstændigt

    # Merge the two sorted halves.
    return merge(left_half, right_half)# Når hver halvdel er sorterede kaldes funktion merge til putte den sammen som en samlet sorterede listen


def merge(left, right):# Funktion tager det to lister som venstre og højere som input og merge dem en sorterede liste
    """Merges two sorted lists into a single sorted list.
    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.
    Returns:
        list: The merged sorted list."""
    merged = []# Laver en tom liste som vil indhold merged resultater
    left_index = 0# Et index som venstre liste
    right_index = 0# Et indes som højere liste

    while left_index < len(left) and right_index < len(right):# Vi gentager gennem begge lister, hvor vi samlinger elementer med den nuværende indexer
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])#  Herefter sætter de mindre elementer til merge listen og increaser værdien til det passende index
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])#Hvis der tilbageværende elementer i enten liste, så sætter vil den bag på the sorterede liste
    merged.extend(right[right_index:])

    return merged# Returener den sorterede liste





if __name__ == '__main__':
    ## Skriv navnet på den algoritme, der skal testes
    algorithm = MergeSort

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
