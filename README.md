# Huffman coding with internet data
In this project, we implement web crawling, Huffman encoding/decoding to compress and save the text data from the website (PTT). 
## Requirements:
beautifulsoup4==4.10.0\
requests==2.26.0
## File description
There's three way to use our program.
1. For compressing the text of all article in the gossiping board on PTT in any ended day, run `main.py` and input the date.
2. For directly compressing the txt file that you have, run `huffman_encoding.py` and complete the requirements.
3. For decoding your file, run `huffman_decoding.py` and input the bin file and the tree file.

For example, `sample.txt` in this folder is an sample text file which is the 5,000-word letter from Lee Jinglei's instagram.

To encode it, you can follow the steps below.

    $ python3 huffman_encoding.py
    txt file: sample.txt
    Print code table? [Y/n]: n
    Make a new file? [Y/n]: y
    file name for save code(with .bin): output.bin
    file name for save tree(with .txt): tree.txt
    Your original file size is 14700 bytes
    Output file size is 9024 bytes
    The compression rate is 0.6138775510204082

So you will get `output.bin` and `tree.txt`, representing the encoded code and the information of the huffman tree. Also, the two file is in this folder.

To decode the file, you can follow the steps below.

    $ python3 huffman_decoding.py
    code file: output.bin
    tree file: tree.txt
    output file name: decode.txt
Finally, you'll get `decode.txt`, which is totally the same as the original input file, and it's also in this folder.
