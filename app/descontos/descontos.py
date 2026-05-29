def calcular_desconto(valor: float, cliente_vip: bool) -> float:
    if valor <= 0:
        return 0
    if cliente_vip == True:
        return valor * 0.2
    if cliente_vip == False:
        return valor * 0.1