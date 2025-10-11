estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

estacoes = {}
estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "id", "mt"])
estacoes["ktres"] = set(["or", "nv", "ca"])
estacoes["kquatro"] = set(["nv", "ut"])
estacoes["kcinco"] = set(["ca", "az"])

estacoes_final = set()

while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()
    for estacao, estados_por_estacao in estacoes.items():
        cobertos = estados_abranger & estados_por_estacao
        print("Estação {} cobre os estados: {}".format(estacao, cobertos))
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos

    estados_abranger -= estados_cobertos
    print("Estados cobertos por {}: {}".format(melhor_estacao, estados_cobertos))
    print()
    estacoes_final.add(melhor_estacao)
    estacoes.pop(melhor_estacao)
    
print(estacoes_final)
