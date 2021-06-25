#script to dispay time

import datetime

display = datetime.datetime.now()
print (display.strftime("%I:%M:%S %p"))
print (display.strftime("%d/%m/%Y"))
