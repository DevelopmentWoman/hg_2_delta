# * HACK-7 
#      //remplazar el item 300 
#      //por tú alias
#      [100,200,300,400,500,600,700]  result >  [100,200,foo,400,500,600,700]


def hack_7():
    result = [100,200,300,400,500,600,700]
    result.insert(2,"foo")
    # result[2] = "foo"
    return result
print(hack_7()) 