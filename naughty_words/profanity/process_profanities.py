with open('List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/en') as file:
    for line in file:
        nl = line.strip('\n')
        print(f"\'{nl}\',")