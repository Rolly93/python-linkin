nombre = [ 'pepe','juan','pedro']
for name in nombre:
    if name =="pepe":
        continue
    print(name)
for name in nombre:
    if name == 'juan':
        break
    print(name)