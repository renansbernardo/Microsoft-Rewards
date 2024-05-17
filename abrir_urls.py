import random
import webbrowser
import time

# Lista de possíveis partes da URL
dominios = ["a", "b", "c", "d", "e"]
terminacoes = ["f", "g", "h", "i", "j"]
outras = ["l", "m", "n","o","p"]
dessas = ["q", "r", "s", "t", "u"]

for i in range(30):
    # Escolhe uma parte de cada lista aleatoriamente
    dominio = random.choice(dominios)
    terminacao = random.choice(terminacoes)
    outra = random.choice(outras)
    dessa = random.choice(dessas)

    # Combina as partes para formar a URL
    url = "https://www.bing.com/search?q=" + dominio + terminacao + outra + dessa +"&qs=SC&pq=bolpgol&sk=SC3&sc=6-6&cvid=DB0EF218B47946FB99C73B08A2DE5689&FORM=QBRE&sp=4&lq=0"

    # Abre a URL no navegador
    webbrowser.open(url)
    
    # Pausa o programa por 7 segundos
    time.sleep(7)
