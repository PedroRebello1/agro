import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import warnings
warnings.filterwarnings('ignore')

# Carregar e limpar os dados

frete_df = pd.read_csv('frete_limpo.csv', sep=';')

for col in ['valor_frete_tonelada', 'valor_tonelada_km']:
    frete_df[col] = frete_df[col].astype(str).str.replace(',', '.').astype(float)

frete_df['distancia_km'] = frete_df['distancia_km'].astype(float)

frete_df['ano'] = frete_df['ano'].astype(int)
frete_df['mes'] = frete_df['mes'].astype(int)
frete_df['date'] = pd.to_datetime(dict(year=frete_df['ano'], month=frete_df['mes'], day=1))

frete_df['month'] = frete_df['date'].dt.month

def get_season(month):
    if month in [12, 1, 2]:
        return 'Summer'
    elif month in [3, 4, 5]:
        return 'Autumn'
    elif month in [6, 7, 8]:
        return 'Winter'
    else:
        return 'Spring'
frete_df['season'] = frete_df['month'].apply(get_season)

# analise exploratoria
print("Summary Statistics:")
print(frete_df[['valor_frete_tonelada', 'distancia_km', 'valor_tonelada_km']].describe().round(2))

# media de frete ao tempo
monthly_avg = frete_df.groupby('date')['valor_frete_tonelada'].agg(['mean', 'std']).reset_index()
plt.figure(figsize=(12,6))
sns.lineplot(data=monthly_avg, x='date', y='mean', errorbar='sd')
plt.title('Média de frete por tonelada ao longo do tempo (com desvio padrão)')
plt.xlabel('Data')
plt.ylabel('Custo (Reais/ton)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# frete por mes
plt.figure(figsize=(12,6))
sns.boxplot(data=frete_df, x='month', y='valor_frete_tonelada')
plt.title('Distribuição do custo do Frete por Mês')
plt.xlabel('Mês')
plt.ylabel('Custo (Reais/ton)')
plt.show()

# distancia x frete
plt.figure(figsize=(12,6))
sns.scatterplot(data=frete_df, x='distancia_km', y='valor_frete_tonelada', alpha=0.5)
plt.title('Distancia vs Custo do frete')
plt.xlabel('Distancia (km)')
plt.ylabel('Custo (Reais/ton)')
plt.show()

# correlacao distancia e custo
corr = frete_df[['distancia_km', 'valor_frete_tonelada']].corr().iloc[0,1]
print(f"Correlação entre distância e custo de frete: {corr:.3f}")

# pipeline do modelo
features = frete_df[['distancia_km', 'month', 'season', 'uf_origem', 'uf_destino']]

# recursos categóricos one-hot
categorical_cols = ['season', 'uf_origem', 'uf_destino']
ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoded = ohe.fit_transform(features[categorical_cols])
encoded_df = pd.DataFrame(encoded, columns=ohe.get_feature_names_out(categorical_cols))

# combinar recursos numéricos + codificados
X = pd.concat([features[['distancia_km', 'month']].reset_index(drop=True), encoded_df], axis=1)
y = frete_df['valor_frete_tonelada']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# treinar Regressor de Reforço de Gradiente
gb_model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=6, random_state=42)
gb_model.fit(X_train, y_train)

# predizer e avaliar
y_pred = gb_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Desempenho do modelo de reforço de gradiente ajustado:')
print(f'Erro absoluto médio: {mae:.2f} BRL/ton')
print(f'R² Score: {r2:.3f}')

# importância das caracteristicas
importances = gb_model.feature_importances_
indices = np.argsort(importances)[::-1]
top_features = X.columns[indices][:10]
top_importances = importances[indices][:10]

print('\nTop 10 principais características:')
for feat, imp in zip(top_features, top_importances):
    print(f"{feat}: {imp:.3f}")

# Plotar Real vs Previsto
plt.figure(figsize=(10,6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Custo Real do Frete (R$/tonelada)')
plt.ylabel('Custo Previsto do Frete (R$/tonelada)')
plt.title('Custos Reais vs. Previstos do Frete (Modelo Ajustado)')
plt.tight_layout()
plt.show()
