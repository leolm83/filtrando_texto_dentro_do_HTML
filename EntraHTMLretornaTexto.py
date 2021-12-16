#retira mantem apenas o texto dentro de uma tag html
# exemplo "<h1> meu texto </h1>"
# retorna : meu texto
html_file = open("text.txt", "r")

for line in html_file.readlines():
    exibe=False
    for word in line:
        if(word=="<"):
            exibe=False
        elif(word==">"):
            exibe=True
        elif(exibe):
            print(word,end="")

html_file.close()
