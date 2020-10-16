def winner3(data):
    dataSplit = [i.split(';') for i in data]
    ballotCount = {}
    for ballot in dataSplit:
        if ballot[0] not in ballotCount:
            ballotCount[ballot[0]] = 0
        ballotCount[ballot[0]] += 1
    maxNum = 0
    mostPopular = ''
    for k, v in ballotCount.items():
        if v > maxNum:
            mostPopular = k
    mostPopularCount = ballotCount[mostPopular]
    percentage = mostPopularCount / len(data)
    if percentage > 0.5:
        return mostPopular
    else:
        leastPopular = ''
        for k, v in ballotCount.items():
            if v < maxNum:
                leastPopular = k
        print(leastPopular)
        print(ballotCount)
        for ballot in dataSplit:
            if ballot[0] == leastPopular:
                ballotCount[ballot[1]] += 1
        for k,v in ballotCount.items():
            if v > maxNum:
                mostPopular = k
        percentage = ballotCount[mostPopular]/len(data)
        print(ballotCount)
        print(percentage)
        print(mostPopular)
        if percentage > 0.5:
            return mostPopular
    return 'Tie'

if __name__ == "__main__":
    data = ['Ezekiel;Joyce;Lakia', 'Ezekiel;Joyce;Lakia']
    print(winner3(data))
    print(winner3(['Jackqueline;Mckenzie;Angelena', 'Jackqueline;Mckenzie;Angelena', 'Jackqueline;Angelena;Mckenzie','Mckenzie;Jackqueline;Angelena','Angelena;Jackqueline;Mckenzie']))
