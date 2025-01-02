import pandas as pd
from nomes import nomes_completos
# Gerando 25 nomes completos aleatórios

# Criando um DataFrame com as duas colunas
df = pd.DataFrame({
    "Nomes Completos": nomes_completos,
})

# Salvando o DataFrame em um arquivo Excel
df.to_excel("Exemplo.xlsx", index=False)
print("Arquivo Excel criado com sucesso!")
