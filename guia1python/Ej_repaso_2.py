def es_bisiesto(año):
    if (año%4==0 or año%400==0 and año%100 !=0):
        print("el año es bisiesto")
    
    else:
        print("no es bisiesto")
    
        
   
bisiesto=es_bisiesto(2013)