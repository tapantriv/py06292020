#Lab 9 List Objects and Methods
# Labis about  create, append, and extend list
photo=  ["ssh", "http", "https"]
print(photo)
# if you want to  know which method you can perform on photo
#print(dir(photo))
#this line will add d, n, and s
photo.extend("dns")
print(photo)
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns")
protoa.append("dns")
print(proto)
proto2 = [ 22, 80, 443, 53 ]
proto.extend(proto2)
print(proto)
protoa.append(proto2)
print(protoa)
