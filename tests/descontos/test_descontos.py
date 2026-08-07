from app.descontos.descontos import calcular_desconto

def test_valor_invalido_negativo():
    assert calcular_desconto(-1, True) == 0

def test_cliente_vip_valor_valido():
    assert calcular_desconto(100, True) == 100 * 0.2

def test_cliente_nao_vip_valor_valido():
    assert calcular_desconto(100, False) == 100 * 0.1

def test_valor_invalido_exatamente_zero():
    assert calcular_desconto(0, True) == 0

def test_valor_positivo_pequeno():
    resultado =  calcular_desconto(0.01, True)
    assert round(resultado, 3) == 0.002

def test_valor_positivo_maior():
    assert calcular_desconto(200, True) == 200 * 0.2
