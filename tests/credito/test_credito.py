import pytest

from app.credito.credito import classificar_credito

@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, retorno_esperado",
    [
        (0, 0, False, "renda invalida"),
        (-1, -2, True, "renda invalida"),
        (1, -1, False, "score invalido"),
        (100, 1100, False, "score invalido"),
        (100, 1000, True, "reprovado"),
        (10, 399, False, "reprovado"),
        (200, 500, False, "aprovado padrao"),
        (300, 1000, False, "aprovado premium")
    ]
)

def test_classificar_credito(
    renda_mensal, score_credito, restrito, retorno_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == retorno_esperado


@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, retorno_esperado",
    [
        (0, 1, False, "renda invalida"),
        (0.01, 1, False, "reprovado"),
        (100, -1, False, "score invalido"),
        (100, 0, False, "reprovado"),
        (100, 399, True, "reprovado"),
        (100, 400, False, "aprovado padrao"),
        (100, 699, False, "aprovado padrao"),
        (100, 700, False, "aprovado premium"),
        (100, 1000, False, "aprovado premium"),
        (100, 1001, False, "score invalido")
    ]
)
def test_fronteira(
    renda_mensal, score_credito, restrito, retorno_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == retorno_esperado
