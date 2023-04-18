import matplotlib.pyplot as plt


cidades = ["São Paulo","Guarulhos","Campinas","São B. do Campo","São J. dos Campos","Santo André","Ribeirão Preto","Osasco"]
habitantes = [12396372,1404694,1223237,849974,737310,723889,720116,701428]

plt.barh(cidades, habitantes)
plt.savefig("/usr/share/nginx/html/grafico.png")
plt.show()

html = """
<html>
<body>
    <img src=grafico.png>
</body>
</html>
"""

f = open('/usr/share/nginx/html/grafico.html','w')
f.write(html)
f.close()