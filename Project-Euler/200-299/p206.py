from tqdm import tqdm

def is_concealed_square(n):
    s = str(n)
    if len(s) != 19:
        return False
    if [int(s[2*i]) for i in range(10)] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        return True
    else:
        return False

for i in tqdm(range(10**9, int((2**0.5)*10**9)+1, 10)):
    # 先頭が 1 なので 1.~e+9 を調べれば十分で、さらに1.414...より下をみればよい
    # 末尾が 0 なので 10 ごとに調べれば十分
    if is_concealed_square(i**2):
        print(i)
        exit()
