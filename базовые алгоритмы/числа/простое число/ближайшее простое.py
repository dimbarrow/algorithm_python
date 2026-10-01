our_num = int(input())

def is_common(num):
    if num < 2:
        return False

    for i in range(2, num//2+1):
        if num % i == 0:
            return False

    return True

def the_closest(our_num):
    step = 1
    while True:
        if is_common(our_num+step):
            return our_num+step
        elif is_common(our_num-step):
            return our_num-step
        step += 1

print(the_closest(our_num))