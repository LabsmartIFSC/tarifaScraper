from utils import getHtmlSoup
import os

#
nomeDiretorioEscrita = "output"
nomeArquivo = "paginaTarifa"
paginaTarifas = "http://www.celesc.com.br/portal/index.php/duvidas-mais-frequentes/1140-tarifa"

diretorioEscrita = os.path.join(os.path.dirname(__file__), nomeDiretorioEscrita)
diretorioArquivo = os.path.join(diretorioEscrita, nomeArquivo)
#

arquivo = open(diretorioArquivo, "w")
arquivo.write(getHtmlSoup(paginaTarifas).prettify())
arquivo.close()

print("printed")
