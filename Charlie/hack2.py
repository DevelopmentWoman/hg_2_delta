#  * HACK-2
#      //eliminar el primer item
#      [100,200,300,400,500,600,700]  result >  [200,300,400,500,600,700]

def hack_2():
    result = [100,200,300,400,500,600,700]
    del result[0]
    return result
print(hack_2())