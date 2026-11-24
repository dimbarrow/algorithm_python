def generation(l, s, prefix = ''):
    if l == 0:
        print(prefix)
        return

    for i in range(s):
        generation(l-1, s, prefix+str(i))

generation(3, 3)