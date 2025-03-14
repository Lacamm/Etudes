def moyPond(notes,coeff):
    sommeP = 0
    sommeCoeff= 0

    for i in range(len(notes)):
        sommeP += notes[i] * coeff[i]
        sommeCoeff += coeff[i]
        
    moyenne = sommeP / sommeCoeff
    return moyenne

notes = [12,5,9,23]
coeff = [3,2,5]
print(moyPond(notes,coeff))
