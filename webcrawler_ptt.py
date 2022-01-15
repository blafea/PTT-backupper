import requests
from bs4 import BeautifulSoup
def PTT(month , date , raw_txt):
    #進入ptt網頁並通過滿18歲認證
    res = requests.get('https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html')
    payload = {'from':'/bbs/Gossiping/index.html','yes':'yes'}
    rs = requests.session()
    res = rs.post('https://www.ptt.cc/ask/over18',data=payload)
    #清空txt檔文字
    with open(raw_txt,'a', encoding='UTF-8') as f:
        f.truncate(0)
        f.close()
    res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html')
    soup = BeautifulSoup(res.text,"html.parser")
    #透過按上一頁尋找最新網址index
    for index in soup.find_all('a'):
        if index.text == '‹ 上頁':
            now_index = index['href'][-10:-5]
    #從最新的頁面往前尋找符合日期的文章
    now_index = int(now_index)+1
    a = 0
    for i in range(now_index):
        url = f'https://www.ptt.cc/bbs/Gossiping/index{now_index-i}.html'
        res = rs.get(url)
        soup = BeautifulSoup(res.text,"html.parser")
        flag = 0
        for link in soup.select('.r-ent'):
            if (link.find('div','date').text == (month+'/'+date)):
                if '刪除' in (link.find('div','title').text):
                    continue
                a = 1
                flag = 1
                page_url = "https://www.ptt.cc"+link.a["href"]
                es = rs.get(page_url)
                oup = BeautifulSoup(es.text,"html.parser")
                with open(raw_txt,'a', encoding='UTF-8') as f:
                    f.write(oup.find(id = 'main-content').text)
            else:
                break
        if (flag==0 )and(a==1):
            break
if __name__ == '__main__':
    month = input('select month (1,2,11...) = ')
    if len(month) == 1:
        month = ' '+month
    date = input('select date (1,2,11,21...) = ')
    if len(date) == 1:
        date = '0'+date

    article_file = input('file name for save raw articles (with .txt) : ')
    PTT(month,date,article_file)
