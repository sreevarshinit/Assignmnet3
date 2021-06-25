#script to dispay time day date

import datetime

display = datetime.datetime.now()
print (display.strftime("%I:%M:%S %p"))
print (display.strftime("%d/%m/%Y"))
print (display.strftime("%a"))
