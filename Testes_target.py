""" 1) Soma de números inteiros """

INDICE = 13
SOMA = 0
K = 0
while (K < INDICE):
    K = K + 1
    SOMA = SOMA + K
print(SOMA);

""" 2) Sequência de Fibonacci """
def fibonacci(x):
    sequencia = [0, 1]
    while True:
        i = sequencia[-1] + sequencia[-2]
        if i > x:
            break
        sequencia.append(i)
    return sequencia

# Definindo o tamanho da lista
n = 100
sequencia = fibonacci(n)
print(sequencia)

""" 3) """
import xml.etree.ElementTree as ET
# Parse do XML fornecido

def calcular_faturamento(faturamento_util):
    # Ignorar valores iguais a zero
    faturamento_util = [valor for valor in faturamento_util if valor != 0]

    # Calcula o menor e maior valor de faturamento
    menor_faturamento = min(faturamento_util)
    maior_faturamento = max(faturamento_util)

    # Calcula a média mensal de faturamento
    media_mensal = sum(faturamento_util) / len(faturamento_util)

    # Calcula o número de dias com faturamento superior à média mensal
    dias_acima_media = len([faturamento for faturamento in faturamento_util if faturamento > media_mensal])
    
    return menor_faturamento, maior_faturamento, media_mensal, dias_acima_media

# Carregar dados do arquivo XML
tree = ET.parse('dados.xml')
root = tree.getroot()

# Lista de faturamentos úteis (ignora finais de semana e feriados)
faturamento_util = []
ano, mes = 2024, 11  # Definimos o ano e o mês dos dados

for row in root.findall('row'):
    dia = int(row.find('dia').text)
    valor = float(row.find('valor').text)
    faturamento_util.append(valor)
    
# Calcular valores
menor_faturamento, maior_faturamento, media_mensal, dias_acima_media = calcular_faturamento(faturamento_util)

# Resultado do menor faturamento ignorando valores iguais a zero
print(f"Menor faturamento diário ignorando zeros: R${menor_faturamento:.2f}")
print(f"Maior faturamento diário: R${maior_faturamento:.2f}")
print(f"Média mensal de faturamento: R${media_mensal:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")


"""4)"""
# Valores de faturamento por estado
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calculando o valor total de faturamento
total_faturamento = sum(faturamento.values())

# Calculando o percentual de representação de cada estado
percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento.items()}

# Exibindo os resultados
print("Valor percentual de representação de cada estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

"""5)"""
def inverter_string(s):
    string_invertida = ""
    for caractere in s:
        string_invertida = caractere + string_invertida
    return string_invertida

# Defina a string diretamente no código ou peça ao usuário para inseri-la
string_original = input("Digite uma string: ")
while True:
    string_invertida = inverter_string(string_original)
    break
print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")