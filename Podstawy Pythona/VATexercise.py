cennaNettoJava = 10
cennaNettoAjax = 20

VAT = 21
obliczonyVAT = (1 + VAT / 100)
cennaBruttoJava = cennaNettoJava * obliczonyVAT
cennaBruttoAjax = cennaNettoAjax * obliczonyVAT

print('cennaBruttoJava = ' + str(cennaBruttoJava))
print('cennaBruttoAjax = ' + str(cennaBruttoAjax))
