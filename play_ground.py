import re

strt = '1*2*3*4/5/6'
cal = re.search(r'(\d) *([*])(\d)* *', strt,)
if cal:
    print(cal.group(2))
