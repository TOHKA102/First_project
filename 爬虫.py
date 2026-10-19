# 调用第三方库
import requests
# 打包Referer和User-Agent信息
headers = {'referer':'https://ssr1.scrape.center/','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# 发射网络请求
response = requests.get('https://p0.meituan.net/movie/283292171619cdfd5b240c8fd093f1eb255670.jpg@464w_644h_1e_1c', headers=headers)
print(response) # 返回状态码
print(response.content)  # 二进制数据
# 转换形式并在当前文件夹下创建
with open('tst.jpg', 'wb') as f:
    f.write(response.content)