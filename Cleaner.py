from time import sleep
from os import system, getcwd, listdir
system("clear")

def verifica(cor = "\033[1;34m"):
  global arquivo
  global files
  path = getcwd()
  cor = cor
  print(cor+"digite o parâmetro completo do diretório que você quer organizar\nou digite (./) Para organizar o diretório atual\nEX:".upper()+"\n"+"\033[1;93m"+f"{path}","\033[b1;32m")
  arquivo = input(">>>>> ")
  files = listdir(arquivo)
  if arquivo == "./":
    arquivo = getcwd()
    files = listdir(arquivo)
  else:
    files = listdir(arquivo)

try:
  verifica()
  deu = True
except FileNotFoundError as error:
  print("\033[1;31m", error)
  deu = False
  sleep(2)

while deu == False:
  sleep(2)
  system("clear")
  try:
    verifica("\033[1;35m")
    deu = True
  except FileNotFoundError as error:
    print("\033[1;31m", error)
    deu = False
    sleep(2)
diretorio = ["PDFs", "APKs", "script_python", "script_bash", "scripts_shell","script_js", "imagem", "música", "vídeo", "outros"]

arquivo += "/"

lista_final = [".js", ".py", ".sh", ".pdf", ".apk", ".mp3", ".bash", ".img", ".mp4"]
for i in diretorio:
  if not i in files:
    system("mkdir {}".format(arquivo+i))
  for iten in files:
    if iten[iten.rfind("."):] == lista_final[1] and i == diretorio[2]:
      system("mv {} {}".format(arquivo+iten, arquivo+i))
    elif iten[iten.rfind("."):] == lista_final[0] and i == diretorio[5]:
      system("mv {} {}".format(arquivo+iten, arquivo+i))
    elif iten[iten.rfind("."):] == lista_final[6] and i == diretorio[3]:
      system("mv {} {}".format(arquivo+iten, arquivo+i))
    elif iten[iten.rfind("."):] == lista_final[3] and i == diretorio[0]:
      system("mv {} {}".format(arquivo+iten, arquivo+i))
    elif iten[iten.rfind("."):] == lista_final[4] and i == diretorio[1]:
      system("mv {} {}".format(arquivo+iten, arquivo+i))
    elif iten[iten.rfind("."):] == lista_final[5] and i == diretorio[7]:
      system("mv {} {}".format(arquivo+iten, arquivo+i))
    elif iten[iten.rfind("."):] == lista_final[2] and i == diretorio[4]:
      system("mv {} {}".format(arquivo+iten, arquivo+i))
    elif iten[iten.rfind("."):] == lista_final[7] and i == diretorio[6]:
      system("mv {} {}".format(arquivo+iten, arquivo+i))
    elif iten[iten.rfind("."):] == lista_final[8] and i == diretorio[8]:
      system("mv {} {}".format(arquivo+iten, arquivo+i))
    elif not iten[iten.rfind("."):] in lista_final and not i == "outros" or not iten[iten.rfind(".")] and not i == "outros":
      system("mkdir {}".format(arquivo+"outros"))
      system("mv {} {}".format(arquivo+iten, arquivo+"outros"))
system("clear")
system("ls")
