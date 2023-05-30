import matplotlib.pyplot as plt

# Lista para armazenar os valores de 'dsp'
dsp_values = []

# Leitura dos dados do arquivo
with open('data.txt', 'r') as file:
    for line in file:
        if '[SSTF] dsp' in line:
            value = int(line.split(' ')[-1])
            dsp_values.append(value)

# Criação dos pontos para o eixo x (representado pelo índice da lista)
x_points = list(range(len(dsp_values)))

# Configuração do gráfico de dispersão com linhas
plt.plot(x_points, dsp_values, marker='', linestyle='-', color='b')
plt.xlabel('Número de acessos ao disco')
plt.ylabel('Regiões do disco')
plt.title('Gráfico de Dispersão - noop with stress')

# Exibição do gráfico
plt.show()
