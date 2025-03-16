def main():
    while True:  # Mantém o programa rodando até o usuário digitar 0
        op = int(input('Selecione o número da atividade desejada entre 1 e 11 ou digite 0 para sair: '))
        if op == 0:
            print("Saindo...")
            break  # Encerra o loop
        operacao(op)

def operacao(op):
    match op:
        case 1:
            atv1()
        case 2:
            atv2()
        case 3:
            atv3()
        case 4:
            atv4()
        case 5:
            atv5()
        case 6:
            atv6()
        case 7:
            atv7()
        case 8:
            atv8()
        case 9:
            atv9()
        case 10:
            atv10()
        case 11:
            atv11()
        case _:
            print("Opção inválida. Tente novamente.")
    
def atv1():
    a = float(input('Digite um número:'))
    b = float(input('Digite um número:'))
    c = float(input('Digite um número:'))
    media = (a+b+c)/3
    return print('A média e:',media)

#2. Crie um programa capaz de ler um número que representa o número de bytes de um
#arquivo, e converter para KB. Obs: Um KB possui 1024 bytes.
def atv2():
    a = int(input('Digite o tamanho do arquivo byte:'))
    tamanho=a/1024
    return print('O tamanho do arquivo em KB e:',tamanho)

#3. Crie um programa capaz de receber 3 números, em sequência, do menor para o maior, e
#imprimir esses mesmos números, porém agora na sequência do maior para o menor.
def atv3():
    a = int(input('Digite o menor número:'))
    b = int(input('Digite o segundo maior número:'))
    c = int(input('Digite o maior número:'))
    return print('A ordem do maior pro menor é:',c,b,a)

#4. Supondo um empréstimo no valor de 𝑐 Reais, por 𝑚 meses a juros de 𝑡% ao mês, crie uma
#programa capaz de ler os valores de c, m e t e descobrir os juros cobrados nesse
#empréstimo. A fórmula para cálculo dos juros simples é a que se segue: 𝑗 = 𝑐 ∗ 𝑚 ∗ 𝑡.
def atv4():
    a = float(input('Digite o valor do emprestimo: R$'))
    b = int(input('Digite o número de meses do emprestimo:'))
    c = float(input('Digite a taxa de juros em porcentagem:'))/100
    valor = a+a*b*c
    return print('O valor total do emprestimo é:',valor)
    
#5. Repita o exercício 4, porém agora usando a fórmula de juros compostos. Para calcular juros
#compostos a fórmula é a que se segue: 𝑗 = 𝑐 ∗ (1 + 𝑡).
def atv5():
    a = float(input('Digite o valor do emprestimo: R$'))
    b = int(input('Digite o número de meses do emprestimo:'))
    c = float(input('Digite a taxa de juros em porcentagem:'))/100
    valor = a*(1+c)**b
    return print('O valor total do emprestimo é:',valor)

#6. Crie um programa capaz de ler 2 números, que indicam respectivamente peso e altura, e
#imprimir seu IMC. A fórmula do IMC é
#
#∗.
def atv6():
    a = float(input('Digite o valor da sua altura:'))
    b = float(input('Digite o valor do seu peso:'))
    valor = b/a**2
    return print('Seu IMC é:',valor)

#7. Crie um programa capaz de ler 3 variáveis a, b e c, que representam valores para uma
#equação do segundo grau, e imprimir o delta. A fórmula do delta é ∆ = 𝑏 − 4 ∗ 𝑎 ∗ 𝑐.
def atv7():
    a = float(input('Digite o valor de a:'))
    b = float(input('Digite o valor de b:'))
    c = float(input('Digite o valor de c:'))
    delta=b**2-4*a*c
    return print('O valor de delta é:',delta)

#8. Crie uma função capaz de calcular a ℎ𝑖𝑝𝑜𝑡𝑒𝑛𝑢𝑠𝑎 de um triângulo retângulo. A formula é
#a que se segue: ℎ𝑖𝑝𝑜𝑡𝑒𝑛𝑢𝑠𝑎 = 𝑐𝑎𝑡𝑒𝑡𝑜𝑂𝑝𝑜𝑠𝑡𝑜 + 𝑐𝑎𝑡𝑒𝑡𝑜𝐴𝑑𝑗𝑎𝑐𝑒𝑛𝑡𝑒.
def atv8():
    a = float(input('Digite o valor do cateto adjacente:'))
    b = float(input('Digite o valor do cateto oposto:'))
    hipotenusa = (a**2+b**2)**(1/2)
    return print('O valor total da hipotenusa é:',hipotenusa)

#9. Crie um programa capaz de ler o raio de um círculo e imprimir sua área. A fórmula para
#área é 𝑎 = 𝜋 ∗ 𝑟.
def atv9():
    a = float(input('Digite o valor do raio:'))
    area = 3.141592653589793*a**2
    return print('O valor total da area é:',area)

#10. Crie um programa capaz de ler a altura (h) e o raio (r) de um cilindro e imprimir seu volume.
#A fórmula para área é v = π ∗ r ଶ ∗ h.
def atv10():
    a = float(input('Digite o valor do raio do cilindro:'))
    b = float(input('Digite o valor do altura do cilindro:'))
    volume = 3.141592653589793*a**2*b
    return print('O valor total do volume é:',volume)
    

#11. Dados os lados a, b e c de um triângulo, elaborar um programa para calcular e exibir o
#perímetro e a área do mesmo. Use o semi-perímetro como base para seu cálculo. Fórmulas:
#sp =
#௔ା௕ ା௖
#ଶ
#, a = ඥsp ∗ (sp − a) ∗ (sp − b) ∗ (sp − c)
def atv11():
    a = float(input('Digite o valor de a:'))
    b = float(input('Digite o valor de b:'))
    c = float(input('Digite o valor de c:'))
    sp=(a+b+c)/2
    area = (sp*(sp-a)*(sp-b)*(sp-c))**(1/2)
    return print('O valor total do semi perimetro é ',sp,' e p valor da area e de ',area)


main()