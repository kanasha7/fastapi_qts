import time
import pytest
from app.faturamento.cobranca import processar_cobranca

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso",
    [
        (-1,"BRONZE",0),
        (0,"OURO",100),
        (100,"PRATA",-1)
    ]
)
def test_entradas_invalidas_valor_prazo(valor_base, plano, dias_atraso):
    assert processar_cobranca(valor_base, plano, dias_atraso) == -1


@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso",
    [
        (200,"DIAMANTE",0),
        (100,"",0),
        (200,"PREMIUM",0)
    ]
)
def test_validar_plano(valor_base, plano, dias_atraso):
    assert processar_cobranca(valor_base, plano, dias_atraso) == -2

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso",
    [
        (100,"OUro",0),
        (100," ouro ",0),
        (100,"OUro ",0)
    ]
)
def test_validação_escrita(valor_base, plano, dias_atraso):
    assert processar_cobranca(valor_base, plano, dias_atraso) == 75



@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, desconto",
    [
        (100,"BRONZE",0,100),
        (100,"PRATA",0,85),
        (100,"OURO",0,75)
    ]
)
def test_desconto_plano_em_dia(valor_base, plano, dias_atraso, desconto):
    assert processar_cobranca(valor_base, plano, dias_atraso) == desconto


@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, valor_multa",
    [
        (100,"BRONZE",1,108.40),
        (100,"PRATA",1,93.34),
        (100,"OURO",1,83.30)
    ]
)
def test_cobranca_atraso_moderado(valor_base, plano, dias_atraso, valor_multa):
    assert processar_cobranca(valor_base, plano, dias_atraso) == valor_multa


@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, valor_multa",
    [
        (100, "BRONZE", 21, 146.80),
        (100, "PRATA", 21, 129.28),
        (100, "OURO", 21, 117.60)
    ]
)
def test_cobranca_atraso_severo(valor_base, plano, dias_atraso, valor_multa):
    assert processar_cobranca(valor_base, plano, dias_atraso) == valor_multa


def test_nao_funcional_tempo_maximo_de_execucao():
    inicio = time.perf_counter()

    processar_cobranca(100, "BRONZE", 10)

    fim = time.perf_counter()

    tempo = fim - inicio

    assert tempo < 0.08