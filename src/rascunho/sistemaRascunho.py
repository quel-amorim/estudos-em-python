
import json

ARQUIVO = "usuarios.json"


def carregarUsuarios():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivoJson:
            return json.load(arquivoJson)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Erro: o arquivo JSON está inválido.")
        return []


def salvarUsuarios(usuarios):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivoJson:
        json.dump(
            usuarios,
            arquivoJson,
            indent=4,
            ensure_ascii=False
        )


def cadastra(nomeUsuario, senha):
    usuarios = carregarUsuarios()

    # Verifica se o nome já está cadastrado
    for dados in usuarios:
        if dados["usuario"] == nomeUsuario:
            print("Este usuário já está cadastrado!")
            return

    novoCliente = {
        "usuario": nomeUsuario,
        "senha": senha
    }

    usuarios.append(novoCliente)
    salvarUsuarios(usuarios)

    print(f"Usuário {nomeUsuario} cadastrado com sucesso!")


def saudacao(nomeUsuario):
    print(f"Olá, {nomeUsuario}! Bem-vindo ao sistema.")


def entraLogin(dadosUsuario, dadosSenha):
    usuarios = carregarUsuarios()

    for dados in usuarios:
        if (
            dadosUsuario == dados["usuario"]
            and dadosSenha == dados["senha"]
        ):
            saudacao(dadosUsuario)
            return True

    print("Usuário ou senha incorretos!")
    return False


while True:
    print("\n" + "-=-" * 15)
    print("[1] Entrar")
    print("[2] Cadastrar")
    print("[3] Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um número válido!")
        continue

    if opcao == 1:
        dadosUsuario = input("Usuário: ")
        dadosSenha = input("Senha: ")

        if entraLogin(dadosUsuario, dadosSenha):
            break

    elif opcao == 2:
        nomeUsuario = input("Registre um nome de usuário: ")
        senha = input("Registre uma senha: ")

        cadastra(nomeUsuario, senha)

    elif opcao == 3:
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")
