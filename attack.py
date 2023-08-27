from encrypt import encrypt

"""
You can implement helper function here if you want
"""

def attack():
    """
    TODO: Implement your code here, You can use encrypt or decrypt or both function for your attack
    """

    """
    Return the secret
    """
    found=''
    d={}
    for i in range(24):
        for ch in range(97,123):
            e=encrypt(found+chr(ch)+" "*(23-i))
            d[ch]=len(e)
        c=min(d.keys(),key= lambda x: d[x])
        found+=chr(c)
    return found

print(attack())