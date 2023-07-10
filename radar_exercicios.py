velocidade = 61 # velocidade do carro atual
local_carro = 99 # local em que o carro esta na estrada km
 
RADAR_1 = 60 # velocidade maxizima do radar1 e é constate
LOCAL_1 = 100 # local onde o rar 1 está
RADAR_RANGE = 1 # a distancia onde o radar pega
EXCESSO_VELOCIDADE = velocidade > RADAR_1
CARRO_MULTADO = local_carro >= (LOCAL_1 - RADAR_RANGE) and (LOCAL_1 + RADAR_RANGE)

if EXCESSO_VELOCIDADE : 
    print("velocidade carro passou do radar 1")

if CARRO_MULTADO and EXCESSO_VELOCIDADE:
    print("o carro foi multado em radar 1")