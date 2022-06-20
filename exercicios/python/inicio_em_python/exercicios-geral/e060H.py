# Uso de *arqgs e **kwargs


# exemplo 1 ( argumentos sem parametrizacao )
# Uso de *args
def titulos_copa(pais, *args):
    print("Pais: ", pais)
    for i in args:
        print('ano: ', i)


titulos_copa('Brasil', '1958', '1962', '1970', '1994', '2002')
titulos_copa('Espanha', '2010')


# # exemplo 2 ( um argumento + parametros )

def calcula_valor_venda(valor, **kwargs):    
    acrescimo = kwargs.get('acrescimo')            
    if acrescimo:        
        valor += valor * (acrescimo/100)
        # valor = valor + (valor*(acrescimo/100)) Esta linha é igual a linha de cima. 

    desconto = kwargs.get('desconto')
    if desconto:
        valor -= valor * (desconto/100)

    return valor

print("ZERO acrescimo ou desconto.....: ", calcula_valor_venda(100))
print("5% de acrescimo................: ", calcula_valor_venda(100,acrescimo=5))
print("10% de desconto................: ", calcula_valor_venda(100,desconto=10))
print("20% de acrescimo e 10% desconto: ", calcula_valor_venda(100,acrescimo=20, desconto=10))


# # exemplo 3 - Multiplos argumentos e multiplos parametros.
def calcula_diversos_valores(*valores, **kwargs):
    acrescimo = kwargs.get('acrescimo')
    desconto = kwargs.get('desconto')

    valor = 0           
    for i in valores: # 100,150
        valor += i
        # print(valor,i)
    if acrescimo:
        valor += valor * (acrescimo/100)

    if desconto:
        valor -= valor * (desconto/100)

    return valor


print("ZERO acrescimo ou desconto.....: ", calcula_diversos_valores(100,150,200,50,500))
print("5% de acrescimo................: ", calcula_diversos_valores(100,150,200,50,500,acrescimo=5))
print("10% de desconto................: ", calcula_diversos_valores(100,150,200,50,500,desconto=10))
print("20% de acrescimo e 10% desconto: ", calcula_diversos_valores(100,150,200,50,500,acrescimo=20,desconto=10))
