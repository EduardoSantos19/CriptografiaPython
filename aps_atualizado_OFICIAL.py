import os
import random
import time

msg = ""
chave = random.randint(0, 1000)

def criptografia():
    global msg
    msg = ""
    arq = open("criptografada.txt", "w")
    texto = input("\nO'que você deseja criptografar: ")
    for i in texto:
        msg += str(ord(i) * chave) + " "
    arq.write(msg)
    arq.close

def descriptografia():
    lista = msg.split()
    msg_2 = ""
    arq = open("descriptografada.txt", "w")
    for i in lista:
        x = chr(int(i) // chave)
        msg_2 += chr(int(i) // chave)
        letra = x
        time.sleep(1)
        print(f"{i} // chave = {letra}")
    arq.write(msg_2)
    arq.close()

    
titulo1 = "------------------------"
titulo2 = "PROGRAMA DE CRIPTOGRAFIA"

print(f"{titulo1.center(50)} \n{titulo2.center(50)} \n{titulo1.center(50)}")
print("\n1 - Criptografia \n2 - Descriptografia \n3 - Sair")

opcao = input("\nDigite a opção que você deseja: ")

while not opcao.isdigit():
    print("\nERROR: Apenas números.")
    opcao = input("\nDigite a opção que você deseja: ")
    
if opcao.isdigit():
    opcao = int(opcao)
    
while (opcao <= 3) or (opcao > 3):
    if (opcao > 3) or (opcao < 1):
        print("\nOpção inválida.")
        time.sleep(1)
        
    elif opcao == 1:
        confirmar = input("\nDigite [s] para confirmar ou [n] para voltar: ").upper()
                
        if confirmar == "S":
            criptografia()
            print("\nCriando arquivo com sua mensagem", end="")

            for i in range(0, 3):
                time.sleep(1)
                print(".", end="")

            time.sleep(1)
            print()
            print("\nCriptografia bem sucedida!")

            time.sleep(1)
            print("\nMensagem Criptografada:")

            time.sleep(1)
            arq = open("criptografada.txt", "r")
            msg_crip = arq.readlines()
            print(f"\n{msg_crip}")
            arq.close()
                
            time.sleep(2)
            print("\nSua chave de acesso é:", chave)

            time.sleep(2)
                
    elif opcao == 2:
        if msg == "":
                print("\nERROR: Não há nada para ser descriptografado. ")
                time.sleep(1.5)
        else:
            confirmar = input("\nDigite [s] para confirmar ou [n] para voltar: ").upper()

            if confirmar == "S":

                chaveCerta = input("\nDigite a Chave de acesso para realizar a descriptografia, (tentativa 1 de 3): ")

                while not chaveCerta.isdigit():
                    print("\nERROR: A chave é um valor numérico.")
                    chaveCerta = input("\nDigite a Chave de acesso para realizar a descriptografia, (tentativa 1 de 3): ")
                    
                if chaveCerta.isdigit():
                    chaveCerta = int(chaveCerta)
                    

                i = 1
                while i <= 4:
                    i += 1
                    if chaveCerta == chave:
                        print("\nDescriptografando sua mensagem: \n")
                        descriptografia()
                            
                        time.sleep(1)
                        print("\nDescriptografia bem sucedida!")
                        time.sleep(1)
                            
                        print("\nAqui está sua mensagem Descriptografada:")
                        arq = open("descriptografada.txt", "r")
                        msg_descrip = arq.readlines()
                        print(f"\n{msg_descrip}")
                        arq.close()
                            
                        time.sleep(3)
                        i -= i
                        break
                        
                    elif i == 4:    
                        os.remove("criptografada.txt")

                        time.sleep(1)
                        print("\nAcesso negado, seu arquivo foi excluído permanentemente.")
                        print("Bloquando seu acesso ao programa. Por favor reinicie o terminal para uma nova utilização.")
                        break
                        
                    elif chaveCerta != chave:
                        print(f"\nChave de acesso incorreta, tentativa {i} de 3")
                        
                    chaveCerta = input("Digite a Chave de acesso para realizar a descriptografia: ")
                    
                    while not chaveCerta.isdigit():
                        print("\nERROR: A chave é um valor numérico.")
                        chaveCerta = input(f"\nDigite a Chave de acesso para realizar a descriptografia, (tentativa {i} de 3): ")
                    
                    if chaveCerta.isdigit():
                        chaveCerta = int(chaveCerta)
            if i == 4:
                break
                
    elif opcao == 3:
        confirmar = input("\nTem certeza que deseja sair? [s] ou [n]: ").upper()  

        if confirmar == "S":
            break
                
    print("\n1 - Criptografia \n2 - Descriptografia \n3 - Sair")
    opcao = input("\nDigite a opção que você deseja: ")
    
    while not opcao.isdigit():
        print("\nERROR: Apenas números.")
        opcao = input("\nDigite a opção que você deseja: ")
    
    if opcao.isdigit():
        opcao = int(opcao)
 
