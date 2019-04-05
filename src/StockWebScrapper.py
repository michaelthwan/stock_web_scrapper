import requests

from bs4 import BeautifulSoup


def parse_table(table):
    data = []
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Get rid of empty values
    return data


def fetch_one_row(code, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    all_tables = soup.findAll('table')
    價值評估 = parse_table(all_tables[0])
    財經焦點 = parse_table(all_tables[1])
    盈利能力 = parse_table(all_tables[2])
    管理效益 = parse_table(all_tables[3])
    損益表 = parse_table(all_tables[4])
    資產負債表 = parse_table(all_tables[5])
    現金流量表 = parse_table(all_tables[6])
    股票價格記錄 = parse_table(all_tables[7])
    股票統計數據 = parse_table(all_tables[8])
    股息和拆股 = parse_table(all_tables[9])

    row = f"{code}\t{價值評估[5][1]}\t{價值評估[6][1]}\t{價值評估[7][1]}\t{盈利能力[0][1]}\t{股票價格記錄[1][1]}\t{股息和拆股[0][1]}\t{股息和拆股[1][1]}\t{股息和拆股[4][1]}\t{股息和拆股[5][1]}".replace("%", "")
    return row


if __name__ == '__main__':
    watched_stocks = [836, 178, 23, 5, 322, 2388, 2600, 52, 4, 590, 1929, 1668, 11, 386, 3988, 1088, 939, 1398, 2378, 1211, 700, 1169, 1, 168, 1928, 914, 1044, 405, 2319, 151, 762, 62, 6, 2638, 435,
                      16, 2, 315, 2380, 883, 2628, 270, 12, 1972, 144, 3328, 388, 941, 17, 669, 267, 101, 83, 823, 1038, 3, 66, 3331, 345, 808, 1199, 293, 87, 6823, 19, 548]
    header = "StockId\t股價營收比(過去十二個月)\t股價淨值比(估值比率)\t企業價值/收入\t利潤率\t52週變化\t預測年度股息率\t預測年度股息收益\t5年平均股息率\t派息率"

    print(header)
    for stock_id in watched_stocks:
        code = f"{str(stock_id).zfill(4)}.HK"
        url = f'https://hk.finance.yahoo.com/quote/{code}/key-statistics?p={code}&.tsrc=fin-srch-v1'
        row = fetch_one_row(code, url)
        print(row)
