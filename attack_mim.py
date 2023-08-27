from des import encrypt, decrypt, key_gen

"""
You can implement helper function here if you want
"""

def attack(message, ciphertext):
    """
    TODO: Implement your code here, You can use encrypt, decrypt and key_gen functions for your attack
    """
    
    """
    Return the keys (k1, k2) such that ct = Enc(Enc(m, k1), k2) [ordering of keys matter]
    """
    key=[]
    txt=[]
    for i in range(2**20):
        key.append(key_gen(i))
        e=encrypt(key[i],message)
        try:
            return (key[i],key[txt.index(e)//2])
        except:
            txt.append(e)
        d=decrypt(key[i],ciphertext)
        try:
            return (key[txt.index(d)//2],key[i])
        except:
            txt.append(d)
    return None
