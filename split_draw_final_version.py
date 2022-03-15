
def paula(l):
    arquivo = open(l, "r")
    aqr = arquivo.read()
    aqr_split = aqr.split("\n")
    tamanho = len(aqr_split)
    arquivo2 = open("splited.html", "w")
    arquivo2.write("<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"UTF-8\"><title>spliter</title>\n</head>\n<body>\n")
    for c in range(tamanho):
        atl = open("splited.html", "a")
        atl.write("<marquee>{}</marquee>\n".format(aqr_split[c]))
    atl2 = open("splited.html", "a")
    atl2.write("</body>\n</html>")



paula("F:\code\exto\[texte]\draw_text.txt")
