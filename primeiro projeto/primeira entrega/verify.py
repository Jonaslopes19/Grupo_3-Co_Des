import sys
import json

from string import ascii_lowercase, digits


def main():
    if len(sys.argv) < 2:
        print('Para rodar digite: {} <arquivo>'.format(sys.argv[0]))
        print('onde <arquivo> é o caminho do seu JSON')
        sys.exit(1)

    with open(sys.argv[1], encoding='utf-8') as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise TypeError('JSON não tem um dicionário principal')
    if len(data) != 1:
        raise ValueError('dicionário principal não tem exatamente um item')
    if 'portfolio' not in data:
        raise ValueError('item do dicionário principal não tem chave "portfolio"')
    lens = set()
    for key, subdata in data['portfolio'].items():
        for c in key:
            if c not in ascii_lowercase and c not in digits:
                raise ValueError('chave de subdicionário de categorias só pode ter letras minúsculas e dígitos')
        if len(subdata) != 2:
            raise ValueError('subdicionário que representa categoria só pode ter dois itens')
        if 'categoria' not in subdata:
            raise ValueError('subdicionário que representa categoria não tem chave "categoria"')
        if not isinstance(subdata['categoria'], str):
            raise TypeError('no subdicionário que representa categoria, "categoria" deve mapear para string')
        if 'projetos' not in subdata:
            raise ValueError('subdicionário que representa categoria não tem chave "projetos"')
        if not isinstance(subdata['projetos'], dict):
            raise TypeError('no subdicionário que representa categoria, "projetos" deve mapear para dicionário')
        for subkey, subsubdata in subdata['projetos'].items():
            for c in subkey:
                if c not in ascii_lowercase and c not in digits:
                    raise ValueError('chave de subdicionário de projetos só pode ter letras minúsculas e dígitos')
            if len(subsubdata) < 2:
                raise ValueError('subdicionário que representa projeto deve ter pelo menos dois itens')
            lens.add(len(subsubdata))
            if 'titulo' not in subsubdata:
                raise ValueError('subdicionário que representa projeto não tem chave "titulo"')
            if not isinstance(subsubdata['titulo'], str):
                raise TypeError('no subdicionário que representa projeto, "titulo" deve mapear para string')
            if 'descricao' not in subsubdata:
                raise ValueError('subdicionário que representa projeto não tem chave "descricao"')
            if not isinstance(subsubdata['descricao'], str):
                raise TypeError('no subdicionário que representa projeto, "descricao" deve mapear para string')
    if len(lens) != 1:
        raise ValueError('todos os projetos precisam ter o mesmo número de campos')


if __name__ == '__main__':
    main()
