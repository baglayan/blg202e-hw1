def rational_to_integer():
    print("Decimal rational number to binary rational number converter")
    
    print("Use the format a/b where a and b are integers.")
    print()
    
    resultText = "Binary number"
    
    # Getting user input
    decimalInput = input("Rational decimal number: ")
    numerator = int(decimalInput.split("/")[0])
    denominator = int(decimalInput.split("/")[1])
    
    factorsOfDenominator = []
    hasFactorOthenThanTwo = False
    
    # Recurrence handling
    for num in range (1, denominator + 1):
        if (denominator % num == 0):
            factorsOfDenominator.append(num)
        
    for factor in range (1, len(factorsOfDenominator)):
        if (factor % num != 0):
            hasFactorOthenThanTwo = True
    
    preRadix = ""
    postRadix = ""
    
    # Negative input handling
    if (numerator < 0 and denominator > 0):
        numerator *= -1
        preRadix += "-"
    elif (denominator < 0 and numerator > 0):
        denominator *= -1
        preRadix += "-"
    elif (numerator < 0 and denominator < 0):
        numerator *= -1
        denominator *= -1
    
    # Initial checks
    if (numerator < denominator):
        preRadix += "0"
    elif (numerator > denominator):
        preRadix += "1"
        numerator = numerator - denominator
    else:
        preRadix += "1"
    
    # Main loop
    while (True):
        if (numerator == denominator):
            break
        
        numerator *= 2
        
        if (numerator < denominator):
            postRadix += "0"
        elif (numerator == denominator):
            postRadix += "1"
            break
        elif (numerator == 0):
            postRadix += "0"
            break
        else:
            numerator = numerator - denominator
            postRadix += "1"
        
        # Recurrence check
        if (hasFactorOthenThanTwo and len(postRadix) == 20):
            resultText += " (approximately): "
            break
            
    if (resultText == "Binary number"):
        resultText += ": "
    
    # Printing the result
    print(resultText + preRadix) if postRadix == "" else print(resultText + preRadix + "." + postRadix)
    
rational_to_integer()