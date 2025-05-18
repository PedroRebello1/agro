import pandas as pd

# Carregando os arquivos
custo_por_municipio = pd.read_csv('custo_por_municipio_limpo.csv')
custo_por_uf = pd.read_csv('custo_por_uf_limpo.csv')
custo_producao = pd.read_csv('custo_producao_limpo_padronizado.csv')
frete_limpo = pd.read_csv('frete_limpo_padronizado.csv')
frete_processado_limpo = pd.read_csv('frete_processado_limpo_padronizado.csv')
frete_resumo_limpo = pd.read_csv('frete_resumo_limpo_padronizado.csv')
preco_minimo = pd.read_csv('preco_minimo_limpo.csv')
precos_mensal_UF = pd.read_csv('precos_mensal_UF_limpo_padronizado.csv')

# Adicionando a coluna 'local' padronizada

# 1. custo_por_municipio
custo_por_municipio['local'] = custo_por_municipio['Municipio de Destino'].str.extract(r'-([A-Z]{2})$')[0]
custo_por_municipio.to_csv('custo_por_municipio_com_local.csv', index=False)

# 2. custo_por_uf
custo_por_uf['local'] = custo_por_uf['Estado (UF) de Destino'].str.upper()
custo_por_uf.to_csv('custo_por_uf_com_local.csv', index=False)

# 3. custo_producao (tem data padronizada)
custo_producao['local'] = custo_producao['uf'].str.upper()
custo_producao.to_csv('custo_producao_com_local_data.csv', index=False)

# 4. frete_limpo (tem data padronizada)
frete_limpo['local'] = frete_limpo['uf_destino'].str.upper()
frete_limpo.to_csv('frete_limpo_com_local_data.csv', index=False)

# 5. frete_processado_limpo (tem data padronizada)
frete_processado_limpo['local'] = frete_processado_limpo['uf_destino'].str.upper()
frete_processado_limpo.to_csv('frete_processado_limpo_com_local_data.csv', index=False)

# 6. frete_resumo_limpo (tem data padronizada)
frete_resumo_limpo['local'] = frete_resumo_limpo['uf_destino'].str.upper()
frete_resumo_limpo.to_csv('frete_resumo_limpo_com_local_data.csv', index=False)

# 7. preco_minimo
preco_minimo['local'] = preco_minimo['uf'].str.upper()
preco_minimo.to_csv('preco_minimo_com_local.csv', index=False)

# 8. precos_mensal_UF (tem data padronizada)
precos_mensal_UF['local'] = precos_mensal_UF['uf'].str.upper()
precos_mensal_UF.to_csv('precos_mensal_UF_com_local_data.csv', index=False)

print("Todos os arquivos foram processados e salvos com sucesso.")
