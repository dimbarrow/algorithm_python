def generation(lt_l, prefix = ''):
    if lt_l == 0:
        print(prefix)
        return

    generation(lt_l-1, prefix+'0')
    generation(lt_l-1, prefix+'1')

generation(3)