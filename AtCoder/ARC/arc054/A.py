L, X, Y, S, D = map(int, input().split())

if Y <= X:
    # このとき反時計回りの相対速度 Y-X が負になるので時計回りに進むことが確定
    if S < D:
        print((D-S)/(Y+X))
    else:
        print((L-S+D)/(Y+X))
elif S < D:
    print(min((D-S)/(Y+X), (L-D+S)/(Y-X)))
else:
    print(min((L-S+D)/(Y+X), (S-D)/(Y-X)))
