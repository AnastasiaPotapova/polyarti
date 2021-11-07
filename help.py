def f1(n, mass):
    ans = []
    for i in mass:
        if i > n:
            ans.append(i)
    return ans


def f2(kvadrat):
    if sum(kvadrat[0]) == sum(kvadrat[1]) == sum(kvadrat[2]):
        if kvadrat[0][0] + kvadrat[1][0] + kvadrat[2][0] == kvadrat[0][1] + kvadrat[1][1] + kvadrat[2][1] == kvadrat[0][2] + kvadrat[1][2] + kvadrat[2][2]:
            return True
    return False


slov = {}
s = input()
for i in s:
    if i in slov.keys():
        slov[i] += 1
    else:
        slov[i] = 1
