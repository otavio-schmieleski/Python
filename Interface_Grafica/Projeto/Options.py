import json
from Cadastro_Produtos import Produto_name,Produto_ag,Produto_opcoes
from Users import Banco_de_dados,User_ag,User_name,User_password,banco_valores,name,ag,password
from Scanner import Scanner
from pathlib import Path

ROOT_FOLDER_USUARIOS = Path(__file__).parent / 'Users.json'
ROOT_FOLDER_PRODUTOS = Path(__file__).parent / 'Cadastro_Produtos.json'
try:
    with open(ROOT_FOLDER_USUARIOS, 'r', encoding='utf-8') as file:
        banco = json.load(file)
    list(banco)
except FileNotFoundError:
    pass

class opcao_autentic:
    def __init__(self,user):

        user_options = input("deseja [T]trasnferir Imobilizado  | [V]Vereficacao  Imobilizado  | [C]cadastrar Imobilizado")
        
        # Tranferir imobilizado
        if user_options.startswith('T') or user_options.startswith('t'):
            opcao = input("Deseja informar o [C]codigo de barras ou [S]Scannear: ")
            if opcao.startswith("C") or opcao.startswith("c"):
                codigo_barras = input("Informe o codigo de barras de 8 digitos: ")
                try:
                    with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
                        banco_produtos = json.load(file)
                    list(banco_produtos)
                except FileNotFoundError:
                    pass
                for codigo in  banco_produtos:
                    if codigo_barras == codigo['cod_barra']:
                        try:
                            Ag = int(input('Deseja Transferir para qual Agencia: '))
                            if Ag >= 1 and Ag <= 31: 
                                self.ag = Ag
                                codigo['ag'] = self.ag
                                with open(ROOT_FOLDER_PRODUTOS, 'w', encoding='utf-8') as file:
                                    json.dump(banco_produtos,file,ensure_ascii=False,indent=2)
                                print('Trasnferencia feita com Sucesso!!')
                                break
                        except TypeError and ValueError:
                            print('Informe uma agencia valida')
                            opcao_autentic(user)
                            pass
                    else:
                        continue
                    
            if opcao.startswith("S") or opcao.startswith("s"):
                Scanner()

        # vereficacao ou consulta de imobilizados por AG
        if user_options.startswith('V') or user_options.startswith('v'):
            for users in banco:
                if user == users['name']:
                    ag = users['ag']
                    try:
                        with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
                            banco_produtos = json.load(file)
                        list(banco_produtos)
                    except FileNotFoundError:
                        pass
                    for item in banco_produtos:
                        if ag == item['ag']:
                            print(item)
                    if len(item) == 0:
                        print('Nada de Imobilizados')

        #Cadastro imobilizado
        if user_options.startswith('C') or user_options.startswith('c'):
            p1 = Produto_name(),Produto_ag(),Produto_opcoes()
