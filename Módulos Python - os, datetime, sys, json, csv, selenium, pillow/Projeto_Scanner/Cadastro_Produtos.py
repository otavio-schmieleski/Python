from Scanner import Scanner
class Produtos:
    def __init__(self):
        try:
            Name = input("Informe o Nome do Produto ")
            if Name == "" or Name == " " or Name =="  " or Name == "   ":
                print("Informe um nome valido")
                Produtos()
        except:
            print("...")
            pass
        
        try:
            Ag = input("Informe o numero da Agencia ")
            if Ag.isdigit() == False:
                print("Informe uma agencia valida")
                Produtos()
        except:
            pass
        
        opcao = input("Deseja informar o [C]codigo de barras ou [S]Scannear")
        if opcao.startswith("C"):
            codigo = input("Informe o codigo de barras de 8 digitos ")
            try:
                if codigo.isdigit() and len(codigo) == 8:
                    print("Produto cadastrado com sucesso!!")
                    pass
            except:
                Produtos()
                
        if opcao.startswith("c"):
            codigo = input("Informe o codigo de barras de 8 digitos ")
            try:
                if codigo.isdigit():
                    print("Produto cadastrado com sucesso!!")
            except:
                Produtos()
                
        if opcao.startswith("S"):
            Scanner()
            
        if opcao.startswith("s"):
            Scanner()
        

Produtos()