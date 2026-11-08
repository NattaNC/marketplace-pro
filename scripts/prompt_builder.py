#!/usr/bin/env python3
"""Cria prompts padronizados para os 100 comandos da Marketplace Pro.

Não gera imagens, não acessa arquivos de imagem e não faz upload.

Exemplos:
  python scripts/prompt_builder.py --list
  python scripts/prompt_builder.py --show /cleanflyer
  python scripts/prompt_builder.py --command /herooffer-minimal --product "Mouse Attack Shark X11" --color Black --theme1 "Mouse super leve" --theme2 "63g" --image img.png --options /pixel-lock,/quality-check
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / 'skills/marketplace-pro/references/catalogo-100-comandos.json'


def load_commands():
    data = json.loads(CATALOG.read_text(encoding='utf-8'))
    commands = data['commands']
    if len(commands) != 100 or len({c['command'] for c in commands}) != 100:
        raise ValueError('Catálogo inválido: esperado conjunto de 100 comandos únicos')
    return {c['command']: c for c in commands}


def build_prompt(command: str, product: str, color='', theme1='', theme2='', image='', options='', quantity='') -> str:
    commands = load_commands()
    if command not in commands:
        raise ValueError(f'Comando desconhecido: {command}')
    option_list = [part.strip() for part in options.split(',') if part.strip()]
    invalid = [value for value in option_list if value not in commands]
    if invalid:
        raise ValueError(f'Opções desconhecidas: {", ".join(invalid)}')
    if not product.strip():
        raise ValueError('Product é obrigatório')
    values = [command,'', f'Product: {product.strip()}']
    for label, value in [('Color', color),('Theme1', theme1),('Theme2', theme2),('Image', image),('Quantity', quantity)]:
        if value.strip():
            values.append(f'{label}: {value.strip()}')
    if option_list:
        values.append('Options: ' + ', '.join(option_list))
    values.append('')
    values.append('Preserve o produto original; não invente especificações ou ângulos. A foto mencionada precisa estar anexada.')
    return '\n'.join(values)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument('--list', action='store_true', help='Listar todos os comandos')
    modes.add_argument('--show', metavar='COMMAND', help='Exibir detalhe do comando')
    modes.add_argument('--command', metavar='COMMAND', help='Gerar prompt')
    parser.add_argument('--product', default='')
    parser.add_argument('--color', default='')
    parser.add_argument('--theme1', default='')
    parser.add_argument('--theme2', default='')
    parser.add_argument('--image', default='')
    parser.add_argument('--quantity', default='')
    parser.add_argument('--options', default='')
    args = parser.parse_args()
    cmds = load_commands()
    if args.list:
        for c in cmds.values():
            print(f"{c['command']:<24} {c['category']:<25} {c['description']}")
    elif args.show:
        if args.show not in cmds:
            parser.error(f'Comando desconhecido: {args.show}')
        print(json.dumps(cmds[args.show], ensure_ascii=False, indent=2))
    else:
        try:
            print(build_prompt(args.command,args.product,args.color,args.theme1,args.theme2,args.image,args.options,args.quantity))
        except ValueError as exc:
            parser.error(str(exc))


if __name__ == '__main__':
    main()
