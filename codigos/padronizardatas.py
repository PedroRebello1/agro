import pandas as pd

# Dicionário para meses em português (maiusculas e minusculas)
meses_pt = {
    'janeiro': '01', 'fevereiro': '02', 'março': '03', 'marco': '03', 'abril': '04',
    'maio': '05', 'junho': '06', 'julho': '07', 'agosto': '08', 'setembro': '09',
    'outubro': '10', 'novembro': '11', 'dezembro': '12'
}

def mes_para_numero(mes):
    # Se já for int (ex: 1, 2), formata com zero a esquerda
    if isinstance(mes, int) or (isinstance(mes, float) and not pd.isna(mes)):
        return f"{int(mes):02d}"
    # Se for texto, converte minusculo e busca no dicionario
    mes_str = str(mes).strip().lower()
    return meses_pt.get(mes_str, '01')  # default para janeiro se não achar

def padroniza_data(row):
    # Caso tenha ano_mes no formato 201801, extrai mes e ano
    if 'ano_mes' in row and pd.notna(row['ano_mes']):
        str_ano_mes = str(int(row['ano_mes']))
        ano = str_ano_mes[:4]
        mes = str_ano_mes[4:]
        return f"{mes}/{ano}"
    # Caso tenha coluna ano e mes numéricos
    elif 'ano' in row and 'mes' in row and pd.notna(row['ano']) and pd.notna(row['mes']):
        mes_num = mes_para_numero(row['mes'])
        ano = str(int(row['ano']))
        return f"{mes_num}/{ano}"
    # Caso tenha mes texto e ano
    elif 'ano' in row and 'mes' in row and pd.notna(row['ano']) and isinstance(row['mes'], str):
        mes_num = mes_para_numero(row['mes'])
        ano = str(int(row['ano']))
        return f"{mes_num}/{ano}"
    else:
        return None

# Exemplos de como aplicar em cada dataframe:

# 1) custo_por_municipio_limpo.csv e custo_por_uf_limpo.csv
# --> Não possuem data, ignorar

# 2) custo_producao_limpo.csv
df_custo_producao = pd.read_csv('custo_producao_limpo.csv')
df_custo_producao['data_padronizada'] = df_custo_producao.apply(padroniza_data, axis=1)
df_custo_producao.to_csv('x_custo_producao_limpo_padronizado.csv', index=False)

# 3) frete_limpo.csv
df_frete = pd.read_csv('frete_limpo.csv', sep=';')
df_frete['data_padronizada'] = df_frete.apply(padroniza_data, axis=1)
df_frete.to_csv('x_frete_limpo_padronizado.csv', index=False)

# 4) frete_processado_limpo.csv
df_frete_proc = pd.read_csv('frete_processado_limpo.csv')
df_frete_proc['data_padronizada'] = df_frete_proc.apply(padroniza_data, axis=1)
df_frete_proc.to_csv('x_frete_processado_limpo_padronizado.csv', index=False)

# 5) frete_resumo_limpo.csv
df_frete_resumo = pd.read_csv('frete_resumo_limpo.csv', sep=';')
df_frete_resumo['data_padronizada'] = df_frete_resumo.apply(padroniza_data, axis=1)
df_frete_resumo.to_csv('x_frete_resumo_limpo_padronizado.csv', index=False)

# 6) preco_minimo_limpo.csv
# --> Não tem coluna de data clara, ignorar

# 7) precos_mensal_UF_limpo.csv
df_precos_mensal = pd.read_csv('precos_mensal_UF_limpo.csv')
df_precos_mensal['data_padronizada'] = df_precos_mensal.apply(padroniza_data, axis=1)
df_precos_mensal.to_csv('x_precos_mensal_UF_limpo_padronizado.csv', index=False)
