def calcular_iof(dias):
    tabela_iof = {
        1: 96, 2: 93, 3: 90, 4: 86, 5: 83, 6: 80, 7: 76, 8: 73, 9: 70, 10: 66,
        11: 63, 12: 60, 13: 56, 14: 53, 15: 50, 16: 46, 17: 43, 18: 40, 19: 36,
        20: 33, 21: 30, 22: 26, 23: 23, 24: 20, 25: 16, 26: 13, 27: 10, 28: 6,
        29: 3, 30: 0
    }
    return tabela_iof.get(dias, 0) / 100


def calcular_ir(dias):
    if dias <= 180:
        return 0.225
    elif dias <= 360:
        return 0.20
    elif dias <= 720:
        return 0.175
    else:
        return 0.15


def calcular_rendimento(valor_inicial, dias):
    taxa_ano = 0.1415
    taxa_dia = (1 + taxa_ano) ** (1 / 365) - 1
    rendimento_bruto = valor_inicial * (1 + taxa_dia) ** dias
    lucro_bruto = rendimento_bruto - valor_inicial


    iof_percentual = calcular_iof(dias)
    imposto_iof = lucro_bruto * iof_percentual


    lucro_pos_iof = lucro_bruto - imposto_iof
    ir_percentual = calcular_ir(dias)
    imposto_ir = lucro_pos_iof * ir_percentual

    lucro_liquido = lucro_pos_iof - imposto_ir
    valor_final = valor_inicial + lucro_liquido

    return {
        "valor_inicial": valor_inicial,
        "dias": dias,
        "rendimento_bruto": rendimento_bruto,
        "lucro_bruto": lucro_bruto,
        "iof": imposto_iof,
        "ir": imposto_ir,
        "lucro_liquido": lucro_liquido,
        "valor_final": valor_final
    }



valor = float(input("Informe o valor a ser investido (R$): "))
dias = int(input("Informe o prazo do investimento em dias: "))

resultado = calcular_rendimento(valor, dias)

print("\nRESULTADO DO INVESTIMENTO")
print(f"Valor Inicial: R$ {resultado['valor_inicial']:.2f}")
print(f"Dias Investidos: {resultado['dias']} dias")
print(f"Lucro Bruto: R$ {resultado['lucro_bruto']:.2f}")
print(f"Imposto IOF: R$ {resultado['iof']:.2f}")
print(f"Imposto IR: R$ {resultado['ir']:.2f}")
print(f"Lucro Líquido: R$ {resultado['lucro_liquido']:.2f}")
print(f"Valor Final Disponível: R$ {resultado['valor_final']:.2f}")
