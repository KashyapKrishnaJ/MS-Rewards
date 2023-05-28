import webbrowser as w
import random as r

for i in range(34):
    u = 'https://www.bing.com/search?q='
    for j in range(10):
        a = chr(r.randint(65, 100)) 
        u += str(a)
    w.open(u, 2)