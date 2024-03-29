def calculate_probabilities():
    m1 = {}
    combs = {}
    output = {}
    
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j in m1:
                m1[i + j] += 1
                combs[i + j].append((i, j))
            else:
                m1[i + j] = 1
                combs[i + j] = [(i, j)]

    for i in range(2, 13):
        if i in m1:
            probability = f"{m1[i]}/36"
            combinations = combs[i]
            output[i] = {'probability': probability, 'combinations': combinations}
        else:
            output[i] = {'probability': '0/36', 'combinations': []}
    
    return output
