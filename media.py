def obter_nota(numero):
    while True:
        try:
            nota = float(input(f"Digite a {numero}ª nota (0.0 a 10.0): "))
            if 0.0 <= nota <= 10.0:
                return nota
            else:
                print("❌ Nota fora do intervalo! Digite novamente.")
        except ValueError:
            print("❌ Valor inválido! Digite um número decimal válido.")


def calcular_media(notas):

    return sum(notas) / len(notas)


def exibir_resultado(nome, notas, media):
    """Exibe o boletim do aluno"""
    print("\n📋 Resultado Final")
    print(f"Aluno: {nome}")
    print(f"Notas: {', '.join([f'{n:.2f}' for n in notas])}")
    print(f"Média: {media:.2f}")

    if media >= 7.0:
        print("Status: Aprovado 🎉")
    else:
        print("Status: Reprovado 😢")
    print("-" * 40)


def main():
    while True:
        print("\n=== Calculadora de Média de Alunos ===")
        nome = input("Digite o nome do aluno: ")

        notas = [obter_nota(i) for i in range(1, 5)]
        media = calcular_media(notas)
        exibir_resultado(nome, notas, media)

        continuar = input("\nDeseja avaliar outro aluno? (s/n): ").strip().lower()
        if continuar != "s":
            print("\n👋 Programa encerrado. Até a próxima!")
            break


if __name__ == "__main__":
    main()
