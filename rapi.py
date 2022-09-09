a=input('digite el nombre del productoa comprar:')
valor=int(input('valor del producto'))

if valor>100000:
    envio=True
    print('su envio es gratis')
else:
    envio=False
    valor=valor+12000
    print('su envio tiene un costo de 12000',a)