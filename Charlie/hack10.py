# * HACK-10 
#      //agregar después del item 500
#      //los alias qux y thud
#      [100,200,300,400,500,600,700]  result >  [100,200,300,400,500,qux,thud,600,700]


def hack_10():
    result = [100,200,300,400,500,600,700]
    result.insert(5,"qux")
    result.insert(6,"thud")
    return result
print(hack_10())

