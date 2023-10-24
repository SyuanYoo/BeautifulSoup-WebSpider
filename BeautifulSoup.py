import urllib.request as req

def getSubject(url, pageTotal):
    print("當前頁數：" + str(pageTotal))
    pageTotal -= 1

    # 建立Request物件，觀察網站後提供request所需的Header資訊
    request = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    # 安裝 beautifulsoup4 => pip install beautifulsoup4
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")  # 解析Html
    # titles = root.find # 找到一個
    titles = root.find_all("div", class_="title")  # 找到所有
    # 取得當前頁面標題
    for title in titles:
        if title.a != None:
            print(title.a.string)
    print("\n")
    # 取得上一頁連結
    nextLink = root.find("a", string="‹ 上頁")
    if nextLink != None and pageTotal > 0:
        getSubject("https://www.ptt.cc" + nextLink["href"], pageTotal)


# Ptt八卦版
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
getSubject(url, 5)
