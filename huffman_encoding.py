import os, math

class node:
    def __init__(self, lchild = None, rchild = None, freq = 0, father = None, name = None):
        '''建立節點之左右子節點、出現頻率(或其子節點總和)、父節點'''
        self.lchild = lchild
        self.rchild = rchild
        self.freq = freq
        self.father = father
        self.name = name
    def isLeft(self):
        #判斷該節點是否為其父節點之左子節點
        return self.father.lchild == self
    def __str__(self):
        return f"lchild: {self.lchild}, rchild: {self.rchild}, freq: {self.freq}, father: {self.father}, name: {self.name}"

def find_freq(fname):
    '''計算文檔內所有文字出現次數'''
    with open(fname, "r", encoding="UTF-8") as f:
        text = f.read()
    dic = dict()
    for i in text:
        try:
            dic[i] += 1
        except:
            dic[i] = 1
    return sorted(dic.items(), key=lambda x:x[1])

def create_leaf(freq_dic):
    '''將文字出現頻率建為樹葉節點'''
    node_list = []
    for nodes in freq_dic:
        node_list.append(node(name = nodes[0], freq = nodes[1]))
    return node_list

def find_pos(L, value):
    '''利用二分搜尋尋找某值應插入之位置'''
    i = 0
    j = len(L)
    while i < j:
        mid = (i+j)//2
        if L[mid].freq == value:
            return mid
        elif L[mid].freq > value:
            j = mid - 1
        else:
            i = mid + 1
    return i

def create_tree(node_list):
    '''建立huffman tree'''
    L = node_list.copy()
    while len(L) > 1:
        lchild = L.pop(0)
        rchild = L.pop(0)
        father = node(lchild=lchild, rchild=rchild, freq=lchild.freq+rchild.freq)
        L.insert(find_pos(L, father.freq), father)
        lchild.father = father
        rchild.father = father
    return L[0]

def huffman_encoding(node_list, root):
    '''由各節點出發，往根節點前進並建立編碼'''
    code = [""] * len(node_list)
    for i in range(len(node_list)):
        temp = node_list[i]
        while temp != root:
            if temp.isLeft():
                code[i] = "0" + code[i]
            else:
                code[i] = "1" + code[i]
            temp = temp.father
    return code

def print_code_table(code, freq_dic):
    '''印出編碼表'''
    for i in range(len(code)):
        print("character: ", repr(freq_dic[i][0]), "frequency: ", freq_dic[i][1], "code: ", code[i])

def txt_to_code(fname, code_dic):
    '''將文檔改寫為對應之編碼'''
    with open(fname, "r", encoding="UTF-8") as f:
        text = f.read()
    out = []
    for i in text:
        out.append(code_dic[i])
    return "".join(out)

def code_to_file(new_fname, txt_code):
    '''將編碼寫至bin檔案中'''
    binary_list = []
    while len(txt_code) > 8:
        binary_list.append(txt_code[:8])
        txt_code = txt_code[8:]
    if txt_code:
        offset_length = 8-len(txt_code)
        binary_list.append(txt_code + "0" * offset_length)
    string = []
    for binary_value in binary_list:
        string.append(int(binary_value, 2))
    string = bytes(string)
    with open(new_fname, "wb") as f:
        f.write(string)

if __name__ == "__main__":
    fname = input("input txt file: ")
    freq_dic = find_freq(fname)
    node_list = create_leaf(freq_dic)
    root = create_tree(node_list)
    code = huffman_encoding(node_list, root)
    node_name = []
    for i in range(len(code)):
        node_name.append(freq_dic[i][0])

    if input("Print code table? [Y/n]: ") not in ["n", "N", "No", "no"]:
        print_code_table(code, freq_dic)

    code_dic = dict(zip(node_name, code))
    txt_code = txt_to_code(fname, code_dic)

    if input("Make a new file? [Y/n]: ") not in ["n", "N", "No", "no"]:
        new_fname = input("file name (with .bin): ")
        code_to_file(new_fname, txt_code)
    
    original_file_size = os.path.getsize(fname)
    compressed_file_size = math.ceil(len(txt_code)/8)
    print("Your original file size is", original_file_size, "bytes")
    print("Output file size is", compressed_file_size, "bytes")
    print("The compression rate is", compressed_file_size/original_file_size)
