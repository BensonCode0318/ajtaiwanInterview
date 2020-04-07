import re
str1 = '<script type="text/javascript">location.href="http://astro.click108.com.tw/daily_10.php?iAstro=10";</script>'
patten = r'l'
a = re.match(patten,str1)
print(a)