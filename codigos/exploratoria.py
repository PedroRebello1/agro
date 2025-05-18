import pandas as pd

custo_por_municipio = pd.read_csv('custo_por_municipio_limpo.csv', sep=',')
custo_por_uf = pd.read_csv('custo_por_uf_limpo.csv', sep=',')
custo_producao = pd.read_csv('custo_producao_limpo.csv', sep=',')
frete_limpo = pd.read_csv('frete_limpo.csv', sep=';')
frete_processado = pd.read_csv('frete_processado_limpo.csv', sep=',')
frete_resumo = pd.read_csv('frete_resumo_limpo.csv', sep=';')
preco_minimo = pd.read_csv('preco_minimo_limpo.csv', sep=',')
precos_mensal_UF = pd.read_csv('precos_mensal_UF_limpo.csv', sep=',')

print(f"\ncusto_por_municipio_limpo.csv\n{custo_por_municipio.head()}")
print(f"\ncusto_por_uf_limpo.csv\n{custo_por_uf.head()}")
print(f"\ncusto_producao_limpo.csv\n{custo_producao.head()}")
print(f"\nfrete_limpo.csv\n{frete_limpo.head()}")
print(f"\nfrete_processado_limpo.csv\n{frete_processado.head()}")
print(f"\nfrete_resumo_limpo.csv\n{frete_resumo.head()}")
print(f"\npreco_minimo_limpo.csv\n{preco_minimo.head()}")
print(f"\nprecos_mensal_UF_limpo.csv\n{precos_mensal_UF.head()}")
