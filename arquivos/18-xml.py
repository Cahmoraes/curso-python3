import xml.etree.ElementTree as ET

dados = """<?xml version='1.0' encoding='utf-8' ?>
<clientes>
  <cliente>
    <id>1</id>
    <nome>Rodrigo</nome>
    <cidade>BH</cidade>
  </cliente>
</clientes>
"""

caminho_arquivo = "dados/clientes.xml"

# 1 - Exportando dados para XML
with open(caminho_arquivo, "w", encoding="utf-8") as f:
    f.write(dados)

# 2 - Lendo dados do XML
tree = ET.parse(caminho_arquivo)
root = tree.getroot()

for cliente in root.findall("cliente"):
    id_cliente = cliente.find("id").text
    nome_cliente = cliente.find("nova_cliente").text
    print(f"Id: {id_cliente} -> Nome: {nome_cliente}")
