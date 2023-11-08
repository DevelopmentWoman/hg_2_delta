# * HACK-9
#      //agregar tú alias al inicio
#      [100,200,300,400,500,600,700]  result >  [foo,100,200,300,400,500,600,700]
 

def hack_9():
    result = [100,200,300,400,500,600,700]
    # result[0] = "foo"
    result.remove(100)
    result.insert(0,"foo")
    return result
print(hack_9())