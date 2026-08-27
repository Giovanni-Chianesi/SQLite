import os #Biblioteca para habilitar cmd's terminal
import sqlite3 #Banco de dados Aura

CAMINHO_BANCO = "jogos.db" #Variável com o nome do BD

def exibir_cabecalho(texto):
    os.system('cls') #Limpa a tela do terminal

    # Cria um efeito aurudo na palavra "GameVault"
    linha = "*" *len(texto)
    print(linha)
    print(texto)
    print(linha)
    print() #Linha em branco para separar o cabeçalho do restante do conteúdo

exibir_cabecalho("GameVault")

def inicializar_banco():
    conn = sqlite3.connect(CAMINHO_BANCO) 

    # Diz ao BD que o SQL está habilitado
    cursor = conn.cursor()

    # Executa o comando SQL descrito abaixo
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            plataforma TEXT NOT NULL,
            zerado BOOLEAN NOT NULL DEFAULT 0
        )
        """
    )

    # Funciona como "Ctrl + S" ou salva, ele que grava
    conn.commit()
    # Fecha a conexão
    conn.close()

# Chamando a função
inicializar_banco()

def listar_jogos():
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()
    cursor.execute("SELECT titulo, plataforma, zerado FROM jogos")
    
    # "fetchall" - Devolve TODAS as linhas do resultado como uma Tupla
    jogos = cursor.fetchall()
    
    conn.close()
    
    #Se BD vazio mostrará a mensagem abaixo
    if not jogos:
        print("Nenhum jogo resenhudo cadastrado ainda!\n")
        return
    
    #Formam o cabeçalho visual antes de listar com 55 traços e alinhamento a esquerda "ljust"
    print(f"{'Título'.ljust(25)} | {'Plataforma'.ljust(12)} | Status")
    print("-" * 55)
    
    # Laço para exibir todos os jogos cadastrados
    for titulo, plataforma, zerado in jogos:
        status = "zerado" if zerado else "jogando"
        print(f"{titulo.ljust(25)} | {plataforma.ljust(12)} | {status}")
        
    print() #Linha em branco para não colar no proximo print
    
#Chamando a função
listar_jogos()

def adicionar_jogo(titulo, plataforma):
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()
    
    # SQL - Para inserir novo jogos
    cursor.execute("INSERT INTO jogos (titulo, plataforma, zerado) VALUES (?, ?, ?)", (titulo, plataforma, False),)
    
    conn.commit()
    conn.close()
    
# Chamando a função
#adicionar_jogo("GTA Sander","Mobile")
#adicionar_jogo("Forsaken","Roblox")
#adicionar_jogo("Pokémon Soul Silver","Nintendo DS")
#adicionar_jogo("FIFA 23","Playstation 4/5")
#adicionar_jogo("BOMBANANA!","Steam")
#listar_jogos()

def marcar_como_zerado(titulo):
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()
    
    # SQL - Para atualizar Status de: jogando para zerado
    cursor.execute("UPDATE jogos SET zerado = ? WHERE titulo = ?", (True, titulo),)
    
    #Guarda quantas linhas mudaram na atualização
    encontrou = cursor.rowcount > 0
    
    conn.commit()
    conn.close()
    return encontrou

def deletar_jogo(titulo):
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jogos WHERE titulo = ?", (titulo,))
    
    encontrou = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return encontrou

def exibir_menu():
    exibir_cabecalho(" GameVault")
    print("1. Adicionar Jogo")
    print("2. Listar Jogo")
    print("3. Marcar jogo como zerado")
    print("4. Sair\n")
    
def pausar():
    input("Pressione Enter para voltar ao menu...")
    
def main():
    while True:
        exibir_cabecalho("GameVault")
        print("1 - Adicionar jogo")
        print("2 - Listar jogos")
        print("3 - Marcar como zerado")
        print("4 - Deletar jogo")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_cabecalho("Adicionar jogo")
            titulo = input("Título do jogo: ")
            plataforma = input("Plataforma: ")
            adicionar_jogo(titulo, plataforma)
            print(f"\n{titulo} adicionado com sucesso!")
            pausar()

        elif opcao == "2":
            exibir_cabecalho("Seus Jogos Gulosos")
            listar_jogos()
            pausar()

        elif opcao == "3":
            exibir_cabecalho("Marcar como zerado")
            titulo = input("Título do jogo que zerou: ")

            if marcar_como_zerado(titulo):
                print(f"\n{titulo} marcado como zerado!")
            else:
                print(f"\n{titulo} não encontrado!")
                print("Confira se digitou corretamente.")

            pausar()

        elif opcao == "4":
            exibir_cabecalho("Deletar jogo")
            titulo = input("Título do jogo que deseja deletar: ")
            
            if deletar_jogo(titulo):
                print(f"\n{titulo} deletado com sucessox!")
            else:
                print(f"\n{titulo} não encontrado!")
                print("Confira se digitou corretamente.")
                
            pausar()
            
        elif opcao == "5":
            print("Até a próxima!")
            break

        else:
            print("Opção inválida! Escolha um número de 1 a 5.")
            pausar()
# Fechamento da função main
if __name__== "__main__":
    main()