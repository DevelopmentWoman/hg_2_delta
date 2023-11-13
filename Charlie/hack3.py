#  * HACK-3
#      //eliminar el último item
#      [100,200,300,400,500,600,700]  result >  [100,200,300,400,500,600]

def hack_3():
    result = [100,200,300,400,500,600,700] 
    result.pop()
    return result
print(hack_3())