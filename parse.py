import codecs
import re
with open('d:/WinCalender/citylist.js', 'rb') as f:
    raw = f.read()
for enc in ['utf-8', 'gbk', 'gb2312', 'gb18030']:
    try:
        txt = raw.decode(enc)
        if '北京' in txt or '深圳' in txt:
            print(f'== {enc} 编码正确 ==')
            print(txt[:500])
            print('---')
            sz = re.findall(r'"([^"]*深圳[^"]*)"\s*:', txt)
            print(f'深圳: {sz}')
            bj = re.findall(r'"([^"]*北京[^"]*)"\s*:', txt)
            print(f'北京: {bj}')
            break
    except Exception as e:
        print(f'{enc} 失败')
