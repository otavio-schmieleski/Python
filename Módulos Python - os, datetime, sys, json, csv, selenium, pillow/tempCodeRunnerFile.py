from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-b')
args = parser.parse_args()
print(args.b)

if args.b is None:
    print('voce nao passou nenhum argumeto')
else:
    print('voce passou todos os argumentos')