from utils import getHtmlSoup
import os
import sys

print("DEV mode on")
# Constantes #
nomeDiretorioEscrita = "output"
nomeArquivo = "paginaTarifa"
paginaTarifas = "http://www.celesc.com.br/portal/index.php/duvidas-mais-frequentes/1140-tarifa"
separator = "****"
diretorioEscrita = os.path.join(os.path.dirname(__file__), nomeDiretorioEscrita)
diretorioArquivo = os.path.join(diretorioEscrita, nomeArquivo)
##############
#arquivo = open(diretorioArquivo, "w")

html = getHtmlSoup(paginaTarifas)
tabelas = []

for table in html.find_all('table'):
	print("\n" + separator)
	titulo = table.find_all('caption')[0].get_text()
	print("titulo: " + titulo)
	for row in table.find_all('tr'):
		for cell in row.find_all('td'):
			if cell.get_text() != "":
				print(cell.get_text(), end='~')
		print("\n")

#arquivo.write(getHtmlSoup(paginaTarifas).prettify())
#arquivo.close()

print("printed")
