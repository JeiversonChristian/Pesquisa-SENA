print("Exemplo: 24 56 1 3 51 37")
print("NÃO PODE TER NÚMERO REPETIDO!")
print("TEM QUE TER 6 NÚMEROS!")
numeros = input("Digite sua sequência de números separados por espaço: ").split()
print("")
print("Pesquisando jogo...")
print("")

parou = 0
quant_jogos_encontrados = 0

with open("resultados-mega.txt", "r") as resultados_mega:
  linhas = resultados_mega.readlines()
for i in range(len(linhas)):
  quant_jogos_encontrados == 0
  informacoes_linha = linhas[i].split("\t")
  informacoes_linha[7] = informacoes_linha[7].rstrip('\n')
  parou = 0
  for j in range(6):
    if not(numeros[j] in informacoes_linha):
      parou = 1
      break
  if parou == 0:
    print(linhas[i])

  if parou == 0:
    quant_jogos_encontrados = quant_jogos_encontrados + 1

print("Quantidade de jogos encontrados: ", quant_jogos_encontrados)
print("Fim do programa")