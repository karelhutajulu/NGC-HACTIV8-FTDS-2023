def celtokelv ( value , type ):
# Function that converts Celcius to Kelvin and Vice-Versa

    if type.lower() == "celcius":
        #lower case the input 'type' so that the answer would not be error despite user typing in Celcius instead of celcius
        answer = value + 273.15
        # equation to calculate kelvin
        print("Result: " + str(answer) + " Kelvin")
        #print calculation result
    elif type.lower() == "kelvin":
         # ==/== would not be error despite user typing in Kelvin instead of kelvin
        answer2 = value - 273.15
        # equation to calculate celcius
        print("Result: " + str(answer2) + " Celcius")
        #print calculation result
    else:
        print('Please specify a correct temperature type')

celtokelv( 
    #Input Celcius to conver to Kelvin Vice-Versa, make sure to include the temperature type
    value = 534 ,
    type  =  'Celcius'
     )

def suhutofarh ( value , type ):
# Function that converts Celcius/Kelvin to Farrenheit

    if type.lower() == "celcius":
        #lower case the input 'type' so that the answer would not be error despite user typing in Celcius instead of celcius
        answer = (value * 9/5) + 32
        # equation to calculate farrenheit from Celcius
        print("Result: " + str(answer) + " Farenheit")
        #print calculation result
    elif type.lower() == "kelvin":
         # ==/== would not be error despite user typing in Kelvin instead of kelvin
        answer2 = (value -  273.15) * 1.8  + 32
        # equation to calculate farrenheit from Kelvin
        print("Result: " + str(answer2) + " Farenheit")
        #print calculation result
    else:
        print('Please specify a correct temperature type')
        #Incase user does not write correct type (kelvin/celcius)

suhutofarh( 
    #Input Celcius to conver to Kelvin Vice-Versa, make sure to include the temperature type
    value = 534 ,
    type  =  'Celcius'
     )

def farhtosuhu ( value , convert_to ):
# Function that converts Celcius/Kelvin to Farrenheit

    if convert_to.lower() == "celcius":
        #lower case the input 'type' so that the answer would not be error despite user typing in Celcius instead of celcius
        answer = (value - 32) / 1.8
        # equation to calculate celcius from farrenheit
        print("Result: " + str(answer) + " Celcius")
        #print calculation result
    elif convert_to.lower() == "kelvin":
         # ==/== would not be error despite user typing in Kelvin instead of kelvin
        answer2 = (value -  32) / 1.8  + 273.15
        # equation to calculate kelvin from farrenheit
        print("Result: " + str(answer2) + " Kelvin")
        #print calculation result
    else:
        print('Please specify a correct destination temperature ')
        #Incase user does not write correct type (kelvin/celcius)

farhtosuhu( 
    #Input Celcius to conver to Kelvin Vice-Versa, make sure to include the temperature type
    value = 534 ,
    convert_to  =  'Celcius'
     )






