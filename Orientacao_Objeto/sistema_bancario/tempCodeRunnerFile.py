def Listar_Usuarios_Cadastrados():
    with open(CAMINHO_ARQUIVO,'r',encoding='utf8') as arquivo:
        banco =json.load(arquivo)
    list(banco)
    for i in banco:
        print(i)