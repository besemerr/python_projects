#initialize
hourlyRate = 15
overtimeRate = 20
salaryRate = 500

x = salaryRate

#calculate payrate 
if x == salaryRate:
    totalPay = salaryRate
elif x < 41:
    totalPay = hourlyRate * x
else:
    totalPay = overtimeRate * x

#print results
print("${:,.2f}".format(totalPay))

