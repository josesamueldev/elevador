from config import peso_suportado
from config import andares

historicos = []

def verificar_elevador():
    print("=" * 40)
    print("   SISTEMA DE CONTROLE DE ELEVADOR")
    print("=" * 40)
    
    for andar in andares:
        print(f"  [{andar}] andar {andar}")
    
    print("-" * 40)
    
    while True:
        try:
            destino = int(input("Digite o andar desejado: "))
            if destino in andares:
                print(f"\nDestino selecionado: andar {destino}")
                break
            else:
                print(f" Andar invalido: Digite entre 1 e {len(andares)}.")
        except ValueError:
            print(" Digite apenas números!")

    print("\nPara sua segurança e dos demais, informamos que o elevador suporta somente 300 KG. Por favor informe os pesos para que seja avaliado.\n")

    while True:
        try:
            n1 = float(input("Digite o seu peso (KG): "))
            n2 = float(input("Digite o peso do seu amigo (KG): "))
            break
        except ValueError:
            print("\n⚠ Erro: Digite apenas números!\n")

    total = n1 + n2

    if total < peso_suportado:
        print("✅ O elevador pode subir. Indo ate o andar selecionado!")
    elif total == peso_suportado:
        print("⚠ O elevador atingiu o peso máximo! O elevador irá subir, porem com instabilidade")
    else:
        print("❌ O elevador não suporta o peso atual!")

    print("=" * 40)
