import huffman_encoding, webcrawler_ptt

if __name__ == "__main__":
    month_org = input('select month (1,2,11...) = ')
    if len(month_org) == 1:
        month = ' '+month_org
    date = input('select date (1,2,11,21...) = ')
    if len(date) == 1:
        date = '0'+date
    if input("save the raw article? [Y/n]: ") not in ["n", "N", "No", "no"]:
        article_file = input('file name for save raw articles (with .txt) : ')
    else:
        article_file = "AAA"
    webcrawler_ptt.PTT(month, date, article_file)
    huffman_encoding.main(article_file, month_org, date)