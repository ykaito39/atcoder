strs = [s[::-1] for s in ["dream", "dreamer", "erase", "eraser"]]

def is_match(s):
    #sのi番目からの文字列がstrsのどれかに一致する
    if len(s) == 0:
        return True

    for j in range(5,8):
        if s[::-1][:j] in strs: #文字列反転させればdreameraser解ける
            return is_match(s[::-1][j:][::-1])

    return False

if __name__ == "__main__":
    input_s = input()

    if is_match(input_s):
        print("YES")
    else:
        print("NO")

#どっかでREになる