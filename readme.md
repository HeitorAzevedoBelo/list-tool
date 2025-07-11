
# Ferramenta de Listagem de Diretórios e Arquivos

Este script em Python permite listar recursivamente os arquivos e diretórios a partir de um caminho base, com suporte a filtros, exibição de conteúdo e exportação para arquivo.

## Funcionalidades

- Listagem completa de arquivos e pastas recursivamente
- Filtro de arquivos/pastas com base em uma lista de exclusão (`--ignore`)
- Exportação da saída para arquivo (`--output`) ou exibição no terminal

---

## Como Usar

### Requisitos

- Python 3.7+

### Execução

```
python3 list_tool.py --path <caminho> [opções]
```

### Parâmetros

| Parâmetro       | Descrição                                                                        |
| --------------- | -------------------------------------------------------------------------------- |
| `--path`        | (Obrigatório) Caminho inicial para leitura                                       |
| `--ignore`      | (Opcional) Caminho para um arquivo `.txt` com nomes de arquivos/pastas a ignorar |
| `--folder-only` | (Opcional) Lista apenas diretórios e arquivos, **sem conteúdo**                  |
| `--output`      | (Opcional) Salva a listagem em um arquivo de saída                               |


## Exemplos

### 1. Listar tudo com conteúdo
```
python3 list_tool.py --path ./meu_projeto
```

### 2. Ignorar pastas e salvar o resultado

```bash
python3 list_tool.py --path ./src --ignore ignores.txt --output resultado.txt

```

### 3. Listar somente nomes de arquivos e pastas (sem conteúdo)

```bash
python3 list_tool.py --path ./docs --folder-only

```

----------

## Formato do Arquivo de Ignore

Cada linha deve conter um **nome de arquivo ou diretório** a ser ignorado (sem path completo):

```
node_modules
.env
venv
arquivo_temporario.txt
```

----------

## Mensagens do Script

-   `[OK] Resultado salvo em: <arquivo>`
    
-   `[OK] Listagem concluída com sucesso.`
    
-   `[INFO] Iniciando leitura do caminho: <path>`
    
-   `[Erro] Caminho inválido ou inacessível: <path>`
    
-   `[Erro] Arquivo de ignore não encontrado: <arquivo>`
    
-   `[ERRO AO LER ARQUIVO] <arquivo>: <mensagem do erro>`
    