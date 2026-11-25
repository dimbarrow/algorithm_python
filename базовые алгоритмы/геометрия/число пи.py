import random
def pi(n):
    points = 0
    points_inside = 0
    for i in range(n):
        point_x = random.uniform(0, 1)
        point_y = random.uniform(0, 1)
        d = (0-point_x)**2 + (0-point_y)**2
        if d <= 1:
            points_inside += 1
            points += 1
        else:
            points += 1

    p_s = points_inside/points #промежуточная площадь
    return p_s*4


print(pi(1000000))
