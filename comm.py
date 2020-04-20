import ast


def list_to_bytes(liste):
 listToStr ="["+','.join(map(str, liste))+"]"
 r=listToStr.encode()
 return r

def bytes_to_list(msg):
 x=msg.decode()
 res=ast.literal_eval(x)
 return res
