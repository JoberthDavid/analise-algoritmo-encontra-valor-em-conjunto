# arquivos de entrada
arquivo_entrada_1 = 'dataset-1-a.csv'
arquivo_entrada_2 = 'dataset-1-b.csv'
arquivo_entrada_3 = 'dataset-1-c.csv'

lista_arquivos = [arquivo_entrada_1, arquivo_entrada_2, arquivo_entrada_3]

path = None

# arquivos de saídas
arquivo_saida = open('saida_{}.txt'.format(path), 'w', encoding="utf-8")


# Considere que um arquivo de entrada (em formato texto) tenha o seguinte formato:
# ●	a primeira linha contém o número n;
# ●	a segunda linha possui um número inteiro t, que corresponde à quantidade de números do conjunto  ; e
# ●	da terceira linha em diante, estão os números do conjunto  .
# Crie um programa que leia o arquivo de entrada e procure o número   no conjunto  , gerando um arquivo de saída contendo três números, um em cada linha:
# ●	a palavra True, se  , ou False, se  ;
# ●	um número inteiro  , que corresponde à posição de   em  . Se  , então o valor de   deve ser  ; e
# ●	um número real  , que corresponde ao tempo de execução do programa em milissegundos.
# Para testar o programa programa, use os três arquivos fornecidos como anexos na atividade.

for entrada in lista_arquivos:

    path = entrada
    arquivo_saida.write('\n#### Para o arquivo {} seguem os resultados:\n'.format(entrada))

    with open(entrada,'r') as manipulador:

        rows = manipulador.readlines()

        i=0
        n = 0
        t = 0
        p = 0
        flag = False

        for row in rows:
            if i == 0:
                arquivo_saida.write('Número (n): {}'.format(row))
                n = row

            elif i == 1:
                arquivo_saida.write('Quantidade de números do conjunto (t): {}'.format(row))
                t = row
                arquivo_saida.write('Segue conjunto D:\n')

            elif (i > 1) and (row == n):
                p = i - 1
                arquivo_saida.write('True\n')
                flag = True

            elif (i > 1):
                arquivo_saida.write('False\n')

            i += 1

        if flag:
            arquivo_saida.write('O valor de p é: {}'.format(p))
        else:
            arquivo_saida.write('O valor de p é: -1\n')