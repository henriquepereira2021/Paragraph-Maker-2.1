 
running = True

while running is True:
 
    
    print("Modes: Standard (1) , One sentence per paragraph (2), Number of sentences per paragraph (3)")
    mode = int(input("Select your mode: "))

    # example of text to use: One. Two. Three. Four. Five. Six. Seven. Eight. Nine. Ten. Eleven. Twelve.


    # For the standard mode, of around 300 characters per paragraph.
    if mode == 1:
        body = input("Insert your text:  ")

        characters_list = []
        indices_adjusted = []

        for a in body:
            characters_list.append(str(a))

        body_len = len(body)
        q_pars = int((body_len / 300) + 1)
        breaker = q_pars
        pars_range = list(range(1, (q_pars + 1)))
        pars_ref = []
        for a in pars_range:
            b = 300 * a
            pars_ref.append(b)

        for a in pars_ref:
            if a > body_len:
                b = pars_ref.index(a)
                pars_ref.pop(b)

        pars = [0]

        indices = [i for i, x in enumerate(characters_list) if x == "."]

        for a in pars_ref:
            b = min(indices, key=lambda x: abs(x - a))
            pars.append(b)

        indices_2 = indices[(breaker - 1):]
        indices_3 = indices_2[::breaker]
        adjustment = [i for i, x in enumerate(indices_3)]

        for i in indices_3:
            i_index = indices_3.index(i)
            indices_adjusted.append(i + adjustment[i_index])

        for c in indices_adjusted:
            characters_list.insert((c + 2), "\n")

        text_list = ''.join((str(d) for d in characters_list))

        print(text_list)

    # For the mode of one sentence per paragraph.
    if mode == 2:

        body = input("Insert your text:  ")

        characters_list = []
        indices_adjusted = []

        for a in body:
            characters_list.append(str(a))

        indices = [i for i, x in enumerate(characters_list) if x == "."]

        adjustment = [i for i, x in enumerate(indices)]

        for i in indices:
            i_index = indices.index(i)
            indices_adjusted.append(i + adjustment[i_index])

        for c in indices_adjusted:
            characters_list.insert((c + 2), "\n")

        text_list = ''.join((str(d) for d in characters_list))

        print(text_list)

    # For the mode of a specific number of sentences per paragraph.
    if mode == 3:

        breaker = int(input("How do you many sentences per paragraph ?  "))
        body = input("Insert your text:  ")

        characters_list = []
        indices_adjusted = []

        if breaker > 0:

            for a in body:
                characters_list.append(str(a))

            indices = [i for i, x in enumerate(characters_list) if x == "."]
            indices_2 = indices[(breaker - 1):]
            indices_3 = indices_2[::breaker]
            adjustment = [i for i, x in enumerate(indices_3)]

            for i in indices_3:
                i_index = indices_3.index(i)
                indices_adjusted.append(i + adjustment[i_index])

            for c in indices_adjusted:
                characters_list.insert((c + 2), "\n")

            text_list = ''.join((str(d) for d in characters_list))

            print(text_list)

        if breaker == 0:
            print("There must be at least 1 sentence per paragraph.")
