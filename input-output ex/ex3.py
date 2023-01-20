def DecimalToOctal(n):
    if(n > 0):
          DecimalToOctal(int(n/8))
          print(n%8, end='')
        
DecimalToOctal(10)
