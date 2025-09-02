# Consultando funcionalidades do módulo OS
import os
import platform
import sys

# 1 - Retornar a pasta atual
print(os.getcwd())

# 2 - Listar arquivos e pastas
print(os.listdir())

# 3 - Versão do sistema operacional
# os.system('cmd.exe /c ver')

# # 4 - Configurações da máquina
# os.system('cmd.exe /c systeminfo')

# # 5 - Limpar a tela do terminal
# os.system('cmd.exe /c cls')

## Usando o sys e platform
print("Sistema:", platform.system())
print("Arquitetura:", platform.architecture())
print("Versão:", platform.version())
print("Release:", platform.release())
print("Máquina:", platform.machine())
print("Python:", sys.version)

# 6 - Desligar o computador
os.system('shutdown /s')
os.system('shutdown /a')

def turn_off_one_hour():
  os.system("shutdown /s /t 3600")
