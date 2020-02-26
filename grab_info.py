import requests
from openpyxl import Workbook


# class _Result:
#     def __init__(self):
#         self._desc = ''
#         self._ganhuo_id = ''
#         self._publishedAt = ''
#         self._readability = ''
#         self._type = ''
#         self._url = ''
#         self._who = ''


def get_json(url, page, lang_name):
    json = requests.get(url).json()
    result_array = json['results']
    info_list = []
    for item in result_array:
        info = [item['desc'], item['ganhuo_id'], item['publishedAt'], item['readability'], item['type'], item['url'],
                item['who']]
        info_list.append(info)
    return info_list


def main():
    _page = 31

    lang_name = input('类型\nall | Android | iOS | 休息视频 | 福利 | 拓展资源 | 前端 | 瞎推荐 | App:\n')
    print('正在抓取。。。[type: ' + lang_name + '][page: ' + _page + ']')
    page = 1
    url = 'http://gank.io/api/search/query/listview/category/' + lang_name + '/count/10/page/1'
    info_result = [['desc', 'ganhuo_id', 'publishedAt', 'readability', 'type', 'url', 'who']]
    while page < _page:
        result = get_json(url, page, lang_name)
        info_result += result
        page += 1
    wb = Workbook()
    ws1 = wb.active
    ws1.title = lang_name

    for row in info_result:
        ws1.append(row)

    file_name = "./gen/" + lang_name + "_queryApiResult.xlsx"
    wb.save(file_name)


if __name__ == '__main__':
    main()
