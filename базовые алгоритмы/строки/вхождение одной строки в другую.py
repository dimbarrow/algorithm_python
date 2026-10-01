def st_in_st(st_big, st_small):
    counter = 0
    for i in range(len(st_big)-len(st_small)+1):
        if st_big[i:i+len(st_small)] == st_small:
            counter += 1

    return counter


print(st_in_st('aaaaa', 'aa'))