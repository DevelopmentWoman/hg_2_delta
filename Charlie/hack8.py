# * HACK-8 
#      //agregar tú alias al final
#      [100,200,300,400,500,600,700]  result >  [100,200,300,400,500,600,700,foo]

def hack_7():
    result = [100,200,300,400,500,600,700]
    result.append("foo")
    # result.insert(7,"foo")
    return result
print(hack_7())