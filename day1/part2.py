with open('in.txt') as f:

    cals = 0
    total_cals = []

    for line in f:
        if line.strip() != '':
            cals = cals + int(line.strip())
        else:
            total_cals.append(cals)
            cals = 0
    print(sum(sorted(total_cals)[-3:]))
