import pymysql
import matplotlib.pyplot as plt

# Estabelecer a comunicação com o banco de dados que
# está no container
con = pymysql.connect(host="127.0.0.1",user="root",password="senac@123",database="assessoriadb",port=6556)

dep = []
vlr = []

cur = con.cursor()
cur.execute("Select * From chamado")
resultado = cur.fetchall()
for i in resultado:
    dep.append(i[3])
    vlr.append(i[6])
cur.close

plt.figure().set_figheight(30)
plt.figure().set_figheight(5)
plt.bar(dep,vlr)
plt.xlabel("Departamentos")
plt.ylabel("Valores")
plt.savefig("/usr/share/nginx/html/dep_vlr.png")

arquivo = open("/usr/share/nginx/html/dep_vlr.html","w")
pagina = """
<html>
    <head>
    <title>Gráfico de Produtos</title>
    </head>
    <body>
        <img src="dep_vlr.png">
    </body>
</html>
"""
arquivo.write(pagina)
arquivo.close()