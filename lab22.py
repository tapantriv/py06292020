#Looping with for
# create the list called vendors
vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
for x in vendors:
    print("the vendor is :"+x)
print("\nOur loop has ended.")
# logic with if else
vendors1 = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
approved_vendors = ["cisco", "juniper", "big_ip"]
for x in vendors1:
    if x not in approved_vendors:
        print("not an approved vendor ", end=" ")