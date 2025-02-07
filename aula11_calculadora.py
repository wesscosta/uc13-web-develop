import math

def soma(num1, num2):
  #return ['SOMA', num1+num2] # Usando Lista  
  return {'operacao':'SOMA','resultado':num1+num2}

def sub(num1, num2):
  return {'operacao':'SUBTRACAO','resultado':num1-num2}

def mult(num1, num2):
  return {'operacao':'MULTIPLICAÇÃO','resultado':num1*num2}

def div(num1, num2):
  return {'operacao':'DIVISAO','resultado':num1/num2}

def porc(num1, num2):
  return {'operacao':'PORCENTAGEM','resultado': (num1*num2)/100 }

def potencia(num1,num2):
  # resultado = math.pow(num1,num2)
  resultado =  num1**num2
  return {'operacao':'POTENCIA', 'resultado': resultado}

def raiz(num1,num2):
  # resultado = math.sqrt(num1)
  resultado = math.pow(num1,1/num2)
  return {'operacao':'RAIZ', 'resultado': resultado}

def resto(num1,num2):
  return {'operacao':'POTENCIA', 'resultado': num1%num2}

# Usando (if - elif - else)



opcao = int(input('Digite o número referente a operação escolhida: \n 1 - soma \n 2 - subtração\n 3 - multiplicacao \n 4 - divisão\n 5 - porcentagem\n 6 - potencia\n 7 - raiz\n 8 - resto \n\n Escolha:'))

a = float(input('Digite um numero: '))
b = float(input('Digite outro numero: '))
calc = 0


if opcao == 1:
  calc = soma(a,b)
elif opcao ==2:
  calc = sub(a,b)
elif opcao == 3:
  calc = mult(a,b)
else:
  print('escolha uma opção valida')
  
# print(f'O resultado da operação de {calc[0]} de {a} e {b} é {calc[1]}')
print(f'O resultado da operação de {calc['operacao']} de {a} e {b} é {calc['resultado']}')
