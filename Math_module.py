import math

result = int(math.sqrt(abs(-25)))
print("\nThe square root of 25 is: ",result)

power = math.pow(abs(-25),2)
print("Power of 25 to 2 is: ",power,type(power))

print("Absolute with float:",math.fabs(-25))

divisor= math.gcd(48,-24,56)
print("Divisor of 48 and -24 is: ",divisor,type(divisor))

common= math.lcm(48,56)
print("Common factor of 48 and 56 is: ",common,type(common))