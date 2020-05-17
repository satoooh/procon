def main():
    N, M = map(int, input().split())
    g = [[] for _ in range(N)]

    A, B = [0]*M, [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
        g[A[i]-1].append(B[i]-1)
        g[B[i]-1].append(A[i]-1)

    ans_list = [-1] * N

    queue = [0]
    seen = [False]*N

    while queue:
        qi = queue.pop(0)
        # qi から 1 遠い頂点が gi
        for gi in g[qi]:
            if seen[gi] == False:
                queue.append(gi)
                if ans_list[gi] == -1:
                    ans_list[gi] = qi
                    seen[gi] = True

    print("Yes")
    for ans in ans_list[1:]:
        print(ans+1)  # 1-index に直す

if __name__ == "__main__":
    main()
