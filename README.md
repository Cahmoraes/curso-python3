# Revisão

- Para listar todas as dependências do Python:
```sh
  pip list
```

- Para listar todas as dependências seguido de suas versões:
```sh
  pip freeze
```

- Para exibir detalhes de uma dependência
```sh
  pip show nome_dependencia
```

- Para salvar as dependências do projeto em um local, como o `package.json` no node, basta listar elas com suas respectivas versões e salvar em um arquivo `requirements.txt`:
```sh
  pip freeze > requirements.txt
```

- Para instalar as dependências de uma aplicação Python dentro do arquivo `requirements.txt`, basta executar:
```sh
  pip install -r requirements.txt
```

## Ambiente virtual VENV
Por padrão todas as dependências do Python são instaladas de forma global. Semelhante ao que ocorre no Node quando instalamos uma dependência global com `npm i -g node`. O problema disso é que as dependências estarão globais entre todos os projetos e pode haver conflitos entre dependências para cada projeto em específico.
Para resolver este problema e ter dependências específicas por projeto, utiliza-se o módulo virtual-env: `venv` do Python para construir um ambiente virtual. É um módulo nativo e para executá-lo é simples:

```sh
  python3 -m venv .venv
```

Este comando significa: execute o módulo `-m venv` que pedirá para sugerir um nome para o ambiente virtual. E atribua o nome `.venv`.
Após isso é necessário ativar o diretório virtual e para isso, no WSL basta executar um `source` sobre o arquivo `activate.csh`:

```sh
  source ./.venv/bin/activate
```

## Consultando todos os módulos nativos do Python
```sh
  # acesse o interpretador do Python no terminal:
  python3
  # após isso execute a função help:
  help("modules")
```