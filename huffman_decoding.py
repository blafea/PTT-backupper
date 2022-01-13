class node:
    def __init__(self, lchild = None, rchild = None, freq = 0, parent = None, name = None):
        '''建立節點之左右子節點、出現頻率(或其子節點總和)、父節點'''
        self.lchild = lchild
        self.rchild = rchild
        self.freq = freq
        self.parent = parent
        self.name = name
    def isLeft(self):
        '''判斷該節點是否為其父節點之左子節點'''
        return self.parent.lchild == self
    def __str__(self):
        if self.lchild == None:
            lchild = None
        else:
            lchild = self.lchild.name
        if self.rchild == None:
            rchild = None
        else:
            rchild = self.rchild.name
        if self.parent == None:
            parent = None
        else:
            parent = self.parent.name
        return f"lchild: {lchild}, rchild: {rchild}, freq: {self.freq}, parent: {parent}, name: {self.name}"

def decode_tree(tree_fname):
    with open(tree_fname, "r", encoding="UTF-8") as f:
        offset = int(f.read(1))
        tree_code = f.read()
    root = node()
    tree_code = list(tree_code)
    now = root
    i = 0
    end = len(tree_code)
    try:
        while i < end:
            if tree_code[i] == "‡":
                now.lchild = node(parent = now)
                now = now.lchild
            elif now.isLeft():
                now.name = tree_code[i]
                now.parent.rchild = node(parent = now.parent)
                now = now.parent.rchild
            else:
                now.name = tree_code[i]
                while not now.isLeft():
                    now = now.parent
                now.parent.rchild = node(parent = now.parent)
                now = now.parent.rchild
            i += 1
    except:
        pass
    return root, offset

def decode(root, offset, code_fname, out_fname):
    with open(code_fname, "rb") as f:
        code = []
        for i in f.read():
            code.append("0"*(10-len(bin(i))) + bin(i)[2:])
        code = "".join(code)
    if offset:
        code = code[:-offset]
    now = root
    ans = []
    code = list(code)
    while code:
        if now.name == None:
            if code[0] == "0":
                now = now.lchild
            else:
                now = now.rchild
            code.pop(0)
        else:
            ans.append(now.name)
            now = root
    ans.append(now.name)
    with open(out_fname, "w", encoding="UTF-8") as f:
        f.write("".join(ans))


if __name__ == "__main__":
    code_fname = input("code file: ")
    tree_fname = input("tree file: ")
    out_fname = input("output file name: ")
    root, offset = decode_tree(tree_fname)
    decode(root, offset, code_fname, out_fname)