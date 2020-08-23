import requests
from bs4 import BeautifulSoup

headers = {}
headers["cookie"] = "_bl_uid=CdkwXd8bnyL7g8jjnqb7rjg6p0ak; lastCity=101020100; __zp_seo_uuid__=efcc4fc8-0430-4b32-b899-80c33574aa91; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1598165030,1598165067,1598165122,1598169087; __c=1596984799; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Fc101020100-p100901%2F%3Fpage%3D2%26ka%3Dpage-2&friend_source=0&g=&friend_source=0; __a=69307904.1596984789.1596984789.1596984799.22.2.21.22; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1598170185; __zp_stoken__=de00bJA5nSAEIEFsNGWttI0wJdGgVRA1FVSxLGB1nVjpAcRt4VmYrBUhbNgRhAQN8BUcJPBddXX1HRBxCAm4SGAUjPAhuGn4mB0VoODRzMiI%2FcmIEJC1HEhFFMVowdAkUAxZ0Wld9R3dsPAohFg%3D%3D"
headers["referer"] = "https://www.zhipin.com/wapi/zpAntispam/verify/sliderNew?u=IA%7E%7E&callbackUrl=http%3A%2F%2Fwww.zhipin.com%2Fc101020100-p100901%2F%3Fpage%3D2%26ka%3Dpage-2&p=IvJY62ezW3IGW3c1PA%7E%7E"

bossPage = requests.get("https://www.zhipin.com/c101020100-p100901/?page=2&ka=page-2", headers=headers).text
soup = BeautifulSoup(bossPage, 'html.parser')
print(bossPage)