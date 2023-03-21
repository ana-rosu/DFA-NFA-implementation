def check(file, word):
    with open(file) as automata:
        nrStates = int(automata.readline())
        alphabet = automata.readline().split()
        initialState = int(automata.readline())
        finalStates = [int(x) for x in automata.readline().split()]
        # input validation
        for letter in word:
            if letter not in alphabet:
                print("The word can only contain ", end="")
                print(*alphabet)
                return
        # lambda word
        if word == "":
            if initialState in finalStates:
                print("The word λ is accepted!")
                return
            else:
                print("The word λ is rejected!")
                return
        # delta function
        delta = {}
        line = automata.readline()
        while line:
            aux = line.split()
            state1 = int(aux[0])
            transition = aux[1]
            state2 = int(aux[2])
            if state1 not in delta:
                delta[state1] = {transition:state2}
            else:
                delta[state1][transition] = state2
            line = automata.readline()

        # processing the word
        state = initialState
        road = [initialState]
        for letter in word:
            state = delta[state][letter]
            road.append(state)

        # check if the word is accepted
        if  road[len(road)-1] in finalStates:
            print(f'The word {word} is accepted!')
            print('The road is: ')
            formatRoad = ""
            for state in road:
                formatRoad += str(state) + "->"
            print(formatRoad[:-2])
        else:
            print("Rejected!")



word = input("Word = ")
# word = ""

check("dfa1.txt", word)