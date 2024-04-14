def html():
   with open('obras.html', 'a') as pagina:
    
    pagina.write('<!DOCTYPE html>\n')
    pagina.write('<html lang="en">\n')
    pagina.write('<head>\n')
    pagina.write('\t<meta charset="UTF-8">\n')
    pagina.write('\t<meta name="viewport" content="width=device-width, inital-scale=1.0">\n')
    pagina.write('\t<title>Document</title>\n')
    pagina.write('</head>\n')
    pagina.write('<body>\n')
    
    pagina.write    ('\t<table>\n')
    
    pagina.write        ('\t\t<tr>\n')
    pagina.write            ('\t\t\t<th colspan="6">RELATORIO DE OBRAS GALERIA VIRTUAL</th>\n')
    pagina.write        ('\t\t</tr>\n')
    
    pagina.write        ('\t\t<tr>\n')
    pagina.write            ('\t\t\t<th>Ano/Mes</th>\n')
    pagina.write            ('\t\t\t<th>Nome</th>\n')
    pagina.write            ('\t\t\t<th>Estilo</th>\n')
    pagina.write            ('\t\t\t<th>Autor</th>\n')
    pagina.write            ('\t\t\t<th>Valor</th>\n')
    pagina.write            ('\t\t\t<th>Imagem</th>\n')
    pagina.write        ('\t\t</tr>\n')
    
    pagina.write    ('\t</table>\n')
    
    pagina.write('</body>\n')
    pagina.write('</html>\n')
    
html()