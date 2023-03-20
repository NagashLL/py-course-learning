def greet(lang):
    #definining the greet function with the argument lang
    if lang == 'es' : 
        print ('Hola!')
    elif lang == 'pl' :
        print ('Cześć!')
    else :
        print ('Hello!')

greet ('pl')
greet ('es')