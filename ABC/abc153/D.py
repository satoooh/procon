def attack_count(N):
    if N == 1:
        return 1
    else:
        return 2 * attack_count(N//2) + 1


H = int(input())
print(attack_count(H))
