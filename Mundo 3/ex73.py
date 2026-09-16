times = (
    'Flamengo',        # 1º
    'Palmeiras',         # 2º
    'Athletico-PR',     # 3º
    'Fluminense',       # 4º
    'Botafogo',         # 5º
    'São Paulo',        # 6º
    'Corinthians',      # 7º
    'Atlético-MG',      # 8º
    'Grêmio',           # 9º
    'Cruzeiro',         # 10º
    'Vasco',            # 11º
    'Bahia',            # 12º
    'Mirassol',         # 13º
    'Coritiba',         # 14º
    'Santos',           # 15º
    'Sport',            # 16º
    'Bragantino',       # 17º
    'Internacional',    # 18º
    'Remo',             # 19º
    'Chapecoense'       # 20º
)


print('-=' * 30)


print(f'Os 5 primeiros colocados são: {times[:5]}')

print('-=' * 30)


print(f'Os últimos 4 colocados são: {times[-4:]}')

print('-=' * 30)


print(f'Times em ordem alfabética: {sorted(times)}')

print('-=' * 30)


print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição')