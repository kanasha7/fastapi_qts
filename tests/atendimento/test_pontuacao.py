from app.atendimento.pontuacao import (calcular_pontuacao_atendimento, classificar_atendimento)

def test_tempo_zero():
    assert calcular_pontuacao_atendimento(0, True, False) == 0

def test_tempo_negativo():
    assert calcular_pontuacao_atendimento(-3, True, False) == 0

def test_resolvido_ate_10_sem_reincidencia():
    assert calcular_pontuacao_atendimento(10, True, False) == 10

def test_resolvido_entre_11_e_20_sem_reincidencia():
    assert calcular_pontuacao_atendimento(11, True, False) == 8

def test_resolvido_acima_de_20_com_reincidencia():
    assert calcular_pontuacao_atendimento(21, True, True) == 4

def test_nao_resolvido_ate_10_sem_reincidencia():
    assert calcular_pontuacao_atendimento(10, False, False) == 5

def test_nao_resolvido_entre_11_e_20_com_reincidencia():
    assert calcular_pontuacao_atendimento(15, False, True) == 1

def test_nao_resolvido_acima_de_20_com_reincidencia():
    assert calcular_pontuacao_atendimento(25, False, True) == 0

def test_classificacao_excelente():
    pontuacao = calcular_pontuacao_atendimento(10, True, False)
    assert classificar_atendimento(pontuacao) == "Excelente"

def test_classificacao_bom():
    pontuacao = calcular_pontuacao_atendimento(11, True, False)
    assert classificar_atendimento(pontuacao) == "Bom"

def test_classificacao_regular():
    pontuacao = calcular_pontuacao_atendimento(25, True, False)
    assert classificar_atendimento(pontuacao) == "Regular"

def test_classificacao_critico():
    pontuacao = calcular_pontuacao_atendimento(25, False, True)
    assert classificar_atendimento(pontuacao) == "Crítico"