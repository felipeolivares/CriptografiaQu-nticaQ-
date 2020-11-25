import qsharp
import random
from Qrng import KeyBB84, RandomBit

def CriptografaMensagem(msg):     
    Msg_Cript = []
    Keys = []
    for i in msg:
        key = GeraChaveCompartilhada()
        Keys.append(key)
        Msg_Cript.append(CriptografaCaracter(i, key))
    return (Msg_Cript, Keys)

def CriptografaCaracter(c, key):
    c = (ord(c) + int(key, 2)) % 255
    return bin(c)

def DescriptografaMensagem(msgs, keys): 
    Msg_Cript = []
    for i in range(len(msgs)):
        Msg_Cript.append(DescriptografaCaracter(msgs[i], keys[i]))
    Msg_Cript = "".join(Msg_Cript) 
    return Msg_Cript

def DescriptografaCaracter(c, key):
    d = (int(c, 2) - int(key, 2)) % 255
    return chr(d)

def GeraChaveCompartilhada():
    key = []
    while len(key) <= 8: 
      
        tam = 16
     
        Alice = QubitsRandomBits(tam) 
        AliceBase = QubitsRandomBits(tam) 
        BobBase = QubitsRandomBits(tam) 
     
        key = KeyBB84.simulate(AliceBits = Alice, AliceBase = AliceBase, BobBase = BobBase, tamanho = tam)
   
    for i in range(len(key)):
        key[i] = str(key[i])
    key = "".join(key)

    return key

def QubitsRandomBits(tam): 
    vetor = []
    for i in range(tam):
        vetor.append(RandomBit.simulate())
    return vetor

msg = list(input("Digite uma palavra para enviar: "))
print(f"Mensagem: {msg}")

Msg_Cript, keys = CriptografaMensagem(msg) 
print(f"Chaves: {keys}")
print(f"Mensagem Criptografada: {Msg_Cript}")

Msg_Descript = DescriptografaMensagem(Msg_Cript, keys) 
print(f"Mensagem Descriptografada: {Msg_Descript}")

