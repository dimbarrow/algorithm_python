def is_point_in_triangle(triangle, point):
    tr_xn = list()
    tr_yn = list()
    len_otr_from_point_x = list()
    len_otr_from_point_y = list()
    otr_from_point = list()
    s_lst = 0
    for i in range(len(triangle)):
        tr_xn.append(triangle[i][0])
        tr_yn.append(triangle[i][1])
    tr_x = sorted(tr_xn, reverse=True)
    print(tr_x)
    tr_y = sorted(tr_yn, reverse=True)
    otr = list()

    for i in range(len(tr_x)-1):
        otr.append((tr_x[i]-tr_x[i+1], tr_y[i]-tr_y[i+1]))
    otr.append((tr_x[0]-tr_x[2], tr_y[0]-tr_y[2]))
    l_otr = list()
    for i in range(len(otr)):
        l_otr.append((otr[i][0]**2 + otr[i][1]**2)**0,5)
    p_lst = 0
    for i in range(len(otr)):
        p_lst += l_otr[i]
    s_lst += (p_lst//2*(p_lst-l_otr[0])*(p_lst-l_otr[1])*(p_lst-l_otr[2]))**0,5

    for i in range(len(otr)):
        len_otr_from_point_x.append(abs(tr_x[i]-point[0]))
        len_otr_from_point_y.append(abs(tr_y[i]-point[1]))

    slen_otr_from_point_x = sorted(len_otr_from_point_x, reverse=True)
    slen_otr_from_point_y = sorted(len_otr_from_point_y, reverse=True)

    for i in range(3):
        otr_from_point.append((slen_otr_from_point_x[i] - slen_otr_from_point_x[i + 1], slen_otr_from_point_y[i] - slen_otr_from_point_y[i + 1]))
    otr_from_point.append((slen_otr_from_point_x[0] - slen_otr_from_point_x[2], slen_otr_from_point_y[0] - slen_otr_from_point_y[2]))

    #p_point1 =
    for i in range(3):
        otr_from_point.append()

    return False


print(is_point_in_triangle([(-0.05,-0.05), (0, 2), (2, 4)], (0,0)))