#!/usr/bin/env python3

import argparse
import os
import sys
from pathlib import Path


def load_ignore_list(ignore_file_path):
    try:
        with open(ignore_file_path, 'r', encoding='utf-8') as file:
            return set(line.strip() for line in file if line.strip())
    except Exception as e:
        print(f"[Erro] Não foi possível ler o arquivo de ignore: {e}")
        sys.exit(1)


def indent_text(text, spaces=4):
    indent = ' ' * spaces
    return '\n'.join(indent + line for line in text.splitlines())


def list_directory_content(base_path, ignore_list, folder_only):
    results = []

    for root, dirs, files in os.walk(base_path):
        rel_root = os.path.relpath(root, base_path)

        if any(ignored in Path(root).parts for ignored in ignore_list):
            continue

        results.append(f"[DIR] {rel_root}")

        for file_name in files:
            full_path = os.path.join(root, file_name)
            rel_file = os.path.relpath(full_path, base_path)

            if any(ignored in Path(full_path).parts for ignored in ignore_list):
                continue

            try:
                results.append(f"  [FILE] {rel_file}")
                if not folder_only:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content = f.read().strip()
                        if content:
                            results.append(f"    [CONTEÚDO]\n{indent_text(content, 6)}")
                        else:
                            results.append("    [CONTEÚDO] (vazio)")
            except Exception as e:
                results.append(f"    [ERRO AO LER ARQUIVO] {rel_file}: {e}")

    return results


def validate_path(path):
    if not os.path.exists(path) or not os.access(path, os.R_OK):
        print(f"[Erro] Caminho inválido ou inacessível: {path}")
        sys.exit(1)


def output_results(results, output_path=None):
    try:
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write('\n'.join(results))
            print(f"[OK] Resultado salvo em: {output_path}")
        else:
            print('\n'.join(results))
    except Exception as e:
        print(f"[Erro] Falha ao salvar o resultado: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Ferramenta para listar diretórios e arquivos com opções de filtro.")
    parser.add_argument('--path', required=True, help="Caminho inicial da leitura.")
    parser.add_argument('--ignore', help="Arquivo com nomes de arquivos/pastas a ignorar (um por linha).")
    parser.add_argument('--folder-only', action='store_true', help="Listar apenas diretórios e arquivos, sem conteúdo.")
    parser.add_argument('--output', help="Arquivo para salvar o resultado. Se omitido, exibe no terminal.")

    args = parser.parse_args()

    validate_path(args.path)

    ignore_list = set()
    if args.ignore:
        if not os.path.isfile(args.ignore):
            print(f"[Erro] Arquivo de ignore não encontrado: {args.ignore}")
            sys.exit(1)
        ignore_list = load_ignore_list(args.ignore)

    print(f"[INFO] Iniciando leitura do caminho: {args.path}")
    results = list_directory_content(args.path, ignore_list, args.folder_only)

    output_results(results, args.output)
    print("[OK] Listagem concluída com sucesso.")


if __name__ == "__main__":
    main()
