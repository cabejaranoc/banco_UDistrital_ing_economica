import math
#Formula Interes Compuesto S=P(1+i)^n
def interesCompuesto(valorPresente, tasa, n):
    return valorPresente*pow((1+tasa),n)
#Formula para hallar valor presente desde interes compuesto
def interesCompuestoP(valorFuturo, tasa, n):
    return valorFuturo/(pow((1+tasa),n))

#Formula para calcular la n en IC log(s)/log(p+i) = n
def interesCompuestoN(valorF,valorP,tasa):
    a=valorF/valorP
    b =1+tasa
    return ((math.log10(a))/(math.log10(b)))

#Formula para calcular la tasa en IC (S/P)^1/n-1=i
def interesCompuestoI(valorF,valorP,n):
    return(((valorF/valorP)**(1/n))-1)


#Cambiando entre i
def equivalenciaTasas(i1,n,m):
    return ((pow((i1+1),n))**(1/m))-1

#cambiando entre i-j
def convertirJI(i,j,opt,m):
    if(opt==1): # convertir de i a j
        return (i*m)
    elif(opt==2): # convertir de j a i

        return (j/m)
#Cambiando entre periodo n y periodo tasa
def Cambiar_n(n,ptasa,pn):
    conversiones = {
        'M': 1,  # Mensual
        'B': 2,   # Bimestral
        'T': 3,   # Trimestral
        'C': 4,   # Cuatrimestral
        'S': 6,   # Semestral
        'A': 12    # Anual
    }

    if(conversiones[ptasa] == conversiones[pn]):
        return int(n)
    else:
        if pn == "M":
            return (n/conversiones[ptasa])
        else:
            return ((n)*conversiones[pn])/conversiones[ptasa]

#Cambiando entre anticipadas
def convertirIA(i,ia,opt):
    if(opt==1): # convertir de i a ia
        return (i/(1+i))
    elif(opt==2): # convertir de ia a i
        return (ia/(1-ia))
    
#Anualidad Ordinaria

def AnualidadOS(cuota,interes,periodos):
    return (cuota*((pow((1+interes),periodos)-1)/(interes)))

def AnualidadOS_A(valor,interes,periodos):
    return ((valor)/(((pow((1+interes),periodos)-1)/(interes))))

def AnualidadOa(cuota,interes,periodos):
    return (cuota*((1-pow((1+interes),-periodos))/(interes)))

def AnualidadOa_A(valor,interes,periodos):
    return ((valor)/(((1-pow((1+interes),-periodos))/(interes))))

# Anualidad Anticipada

def AnualidadAS(cuota,interes,periodos):
    return (cuota*((pow((1+interes),periodos)-1)/(interes))*(1+interes))

def AnualidadAS_A(valor,interes,periodos):
    return ((valor)/(((pow((1+interes),periodos)-1)/(interes))*(1+interes)))

def AnualidadAa(cuota,interes,periodos):
    return (cuota*((1-pow((1+interes),-periodos))/(interes))*(1+interes))

def AnualidadAa_A(valor,interes,periodos):
    return ((valor)/(((1-pow((1+interes),-periodos))/(interes))*(1+interes)))

#Anualidad Diferida
def AnualidadDiferida(cuota,interes,periodos,m):
    return (cuota*((1-pow((1+interes),-periodos))/(interes))*pow((1+interes),-m))

def AnualidadDiferidaA(valor,interes,periodos,m):
    return ((valor)/(((1-pow((1+interes),-periodos))/(interes))*pow((1+interes),-m)))