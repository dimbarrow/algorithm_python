def hIndex(citations):
    index = 0
    for i in range(len(citations) - 1, -1, -1):
        if citations[i] > index:
            index += 1

    return index