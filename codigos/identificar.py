import pandas as pd

# Carregar bases
custo_por_municipio = pd.read_csv('custo_por_municipio_limpo.csv', sep=',')
custo_por_uf = pd.read_csv('custo_por_uf_limpo.csv', sep=',')
custo_producao = pd.read_csv('custo_producao_limpo.csv', sep=',')
frete_limpo = pd.read_csv('frete_limpo.csv', sep=';')
frete_processado = pd.read_csv('frete_processado_limpo.csv', sep=',')
frete_resumo = pd.read_csv('frete_resumo_limpo.csv', sep=';')
preco_minimo = pd.read_csv('preco_minimo_limpo.csv', sep=',')
precos_mensal_UF = pd.read_csv('precos_mensal_UF_limpo.csv', sep=',')

def resumo_chaves(df, nome_base):
    print(f"\n=== Resumo da base: {nome_base} ===")
    
    # Mostrar colunas da base
    print(f"Colunas: {list(df.columns)}\n")
    
    # Identificar colunas relacionadas a UF, municipio, ano, mes, produto
    cols_uf = [c for c in df.columns if 'uf' in c.lower()]
    cols_mun = [c for c in df.columns if 'municipio' in c.lower()]
    cols_ano = [c for c in df.columns if 'ano' in c.lower()]
    cols_mes = [c for c in df.columns if 'mes' in c.lower()]
    cols_produto = [c for c in df.columns if 'produto' in c.lower()]
    
    def print_unique(col_list):
        for col in col_list:
            uniques = df[col].dropna().unique()
            uniques_sorted = sorted(uniques, key=lambda x: str(x))
            print(f"Únicos em '{col}' ({len(uniques)}): {uniques_sorted[:10]}{'...' if len(uniques) > 10 else ''}")

    # Mostrar valores únicos dessas colunas chave
    print_unique(cols_uf)
    print_unique(cols_mun)
    print_unique(cols_ano)
    print_unique(cols_mes)
    print_unique(cols_produto)
    
    # Se ano e mês existirem, mostrar tipos e exemplos para ver se precisam padronizar
    if cols_ano and cols_mes:
        for a, m in zip(cols_ano, cols_mes):
            print(f"\nExemplos de ano ({a}) e mês ({m}):")
            print(df[[a,m]].drop_duplicates().head(10))
    
for base, nome in [
    (custo_por_municipio, 'custo_por_municipio'),
    (custo_por_uf, 'custo_por_uf'),
    (custo_producao, 'custo_producao'),
    (frete_limpo, 'frete_limpo'),
    (frete_processado, 'frete_processado'),
    (frete_resumo, 'frete_resumo'),
    (preco_minimo, 'preco_minimo'),
    (precos_mensal_UF, 'precos_mensal_UF')
]:
    resumo_chaves(base, nome)
