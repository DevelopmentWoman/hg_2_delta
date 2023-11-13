#  * HACK-4
#      //eliminar los items 300 y 500
#      [100,200,300,400,500,600,700]  result >  [100,200,400,600,700]

def hack_4():
    result = [100,200,300,400,500,600,700]
    del result[2 and 4]
    return result
print(hack_4())