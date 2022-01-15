def decode_tree(tree_fname):
    with open(tree_fname, "r", encoding="UTF-8") as f:
        offset = int(f.read(1))
        tree_code = list(f.read())
    i = 0
    j = len(tree_code)
    temp = ""
    dic = dict()
    try:
        while i < j:
            if tree_code[i] == "ª":
                temp += "0"
            elif tree_code[i-1] == "ª":
                dic[temp] = tree_code[i]
                temp = temp[:-1] + "1"
            else:
                dic[temp] = tree_code[i]
                temp2 = list(reversed(temp))
                pos = temp2.index("0")
                temp = temp[:len(temp)-pos-1] + "1"
            i += 1
    except:
        pass
    return dic, offset

def decode(dic, offset, code_fname, out_fname):
    with open(code_fname, "rb") as f:
        code = []
        for i in f.read():
            code.append("0"*(10-len(bin(i))) + bin(i)[2:])
        code = "".join(code)
        if offset:
            code = code[:-offset]
    i = 0
    k = 0
    j = len(code)
    ans = []
    while k <= j:
        if code[i:k] in dic:
            ans.append(dic[code[i:k]])
            i = k
            k += 1
        else:
            k += 1
    with open(out_fname, "w", encoding="UTF-8") as f:
        f.write("".join(ans))


if __name__ == "__main__":
    code_fname = input("code file: ")
    tree_fname = input("tree file: ")
    out_fname = input("output file name: ")
    dic, offset = decode_tree(tree_fname)
    decode(dic, offset, code_fname, out_fname)