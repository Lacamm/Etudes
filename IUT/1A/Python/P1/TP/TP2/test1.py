def test1(x,y,z):
    trace = 'Je suis pasśe pars'
    if(x<y):
        trace = trace + ' x<y'
    else:
        trace = trace + ' x>=y'
        if(y<z):
            trace = trace + ' y<z'
        else:
            trace = trace + ' z<=y'
            if(x<z):
                trace = trace + ' x<z'
            else:
                trace = trace + ' x>=z'
    return trace

trace = ''

print(test1(14,12,18))