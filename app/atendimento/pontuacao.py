def calcular_pontuacao_atendimento(tempo_minutos, resolvido_primeiro_contato, reincidencia):
    if tempo_minutos <= 0:
        return 0

    if resolvido_primeiro_contato == True:
        if tempo_minutos <= 10:
            pontuacao = 10
        elif tempo_minutos <= 20:
            pontuacao = 8
        else:
            pontuacao = 6

    if resolvido_primeiro_contato == False:
        if tempo_minutos <= 10:
            pontuacao = 5
        elif tempo_minutos <= 20:
            pontuacao = 3
        else:
            pontuacao = 1

    if reincidencia == True:
        pontuacao = pontuacao - 2

    if pontuacao < 0:
        return 0

    return pontuacao


def classificar_atendimento(pontuacao):
    if pontuacao >= 9:
        return "Excelente"

    if pontuacao >= 7:
        return "Bom"

    if pontuacao >= 4:
        return "Regular"

    return "Crítico"