#Python Dictionari


## request a 'fake' key with .get() method
switch = { "hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}
print(switch["hostname"])
print(switch["ip"])

print(switch.get("hostname"))
print(switch.get("ip"))
#printing keys
print(switch.keys())
#Print values
print(switch.values())
print(switch)
