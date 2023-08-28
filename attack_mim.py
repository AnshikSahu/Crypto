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
    txt1={}
    txt2={}
    for i in range(2**20):
        key=key_gen(i)
        e=encrypt(key,message)
        try:
            return (key,txt1[e])
        except:
            txt2[e]=key
        d=decrypt(key,ciphertext)
        try:
            return (txt2[d],key)
        except:
            txt1[d]=key
    return None
