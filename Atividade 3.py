# ============================================
# ANALISE DE VENDAS - SQLITE + PANDAS + MATPLOTLIB
# ============================================

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- PASSO 1: CONEXÃO COM BANCO E INSERÇÃO DE DADOS ---

# Nome do banco de dados SQLite
DB_PATH = "dados_vendas.db"

# Conectar ou criar o banco
conexao = sqlite3.connect(DB_PATH)
cursor = conexao.cursor()

# Criar tabela (se não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
''')

# Dados iniciais
dados_iniciais = [
    ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00)
]

# Inserir apenas se tabela estiver vazia
cursor.execute("SELECT COUNT(*) FROM vendas1")
total_registros = cursor.fetchone()[0]
if total_registros == 0:
    cursor.executemany('''
        INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda)
        VALUES (?, ?, ?, ?)
    ''', dados_iniciais)
    conexao.commit()

# --- PASSO 2: CARREGAR DADOS NO PANDAS ---

df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao, parse_dates=['data_venda'])

# Criar colunas auxiliares para análises
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])
df_vendas['ano'] = df_vendas['data_venda'].dt.year
df_vendas['mes'] = df_vendas['data_venda'].dt.month
df_vendas['mes_nome'] = df_vendas['data_venda'].dt.strftime('%Y-%m')

print("📌 Dados carregados com sucesso!\n")
print(df_vendas.head())

# --- PASSO 3: ANÁLISES ---

# Total de vendas por categoria
vendas_por_categoria = df_vendas.groupby('categoria')['valor_venda'].sum().reset_index().sort_values('valor_venda', ascending=False)
print("\n💰 Total de vendas por categoria:")
print(vendas_por_categoria)

# Total de vendas por mês
vendas_por_mes = df_vendas.groupby('mes_nome')['valor_venda'].sum().reset_index()
print("\n📅 Total de vendas por mês:")
print(vendas_por_mes)

# Top produtos por valor vendido
top_produtos = df_vendas.groupby('produto')['valor_venda'].sum().reset_index().sort_values('valor_venda', ascending=False)
print("\n🏆 Top produtos por valor vendido:")
print(top_produtos)

# Estatísticas descritivas
print("\n📊 Estatísticas descritivas:")
print(df_vendas['valor_venda'].describe())

# --- PASSO 4: VISUALIZAÇÕES ---

# Criar pasta para gráficos
os.makedirs("plots", exist_ok=True)

# Gráfico 1: Vendas por mês
plt.figure(figsize=(10,5))
plt.bar(vendas_por_mes['mes_nome'], vendas_por_mes['valor_venda'])
plt.title('Vendas por mês (2023)')
plt.xlabel('Mês')
plt.ylabel('Total vendido (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/vendas_por_mes.png")
plt.show()

# Gráfico 2: Vendas por categoria
plt.figure(figsize=(8,5))
plt.bar(vendas_por_categoria['categoria'], vendas_por_categoria['valor_venda'])
plt.title('Vendas por categoria (2023)')
plt.xlabel('Categoria')
plt.ylabel('Total vendido (R$)')
plt.tight_layout()
plt.savefig("plots/vendas_por_categoria.png")
plt.show()

# Gráfico 3: Vendas por data (linha)
vendas_por_data = df_vendas.groupby('data_venda')['valor_venda'].sum().reset_index().sort_values('data_venda')
plt.figure(figsize=(10,5))
plt.plot(vendas_por_data['data_venda'], vendas_por_data['valor_venda'], marker='o')
plt.title('Vendas por data (2023)')
plt.xlabel('Data')
plt.ylabel('Valor vendido (R$)')
plt.tight_layout()
plt.savefig("plots/vendas_por_data.png")
plt.show()

# Gráfico 4: Boxplot dos valores de venda
plt.figure(figsize=(6,5))
plt.boxplot(df_vendas['valor_venda'])
plt.title('Distribuição dos valores de venda')
plt.ylabel('Valor (R$)')
plt.tight_layout()
plt.savefig("plots/boxplot_valores_venda.png")
plt.show()

# --- PASSO 5: SALVAR RESULTADOS ---

vendas_por_categoria.to_csv("vendas_por_categoria.csv", index=False)
vendas_por_mes.to_csv("vendas_por_mes.csv", index=False)

print("\n✅ Análise concluída com sucesso!")
print("Gráficos salvos na pasta 'plots/'.")
print("Arquivos CSV salvos: vendas_por_categoria.csv e vendas_por_mes.csv")

# Fechar conexão com o banco
conexao.close()
