import pickle

path = './raw.txt'
txt = open(path, 'r').read()
arr = txt.split('>')
filtered = [x[1:-2].strip() for x in arr if len(x) > 1] #Skip empty spaces and newlines

print(filtered)

with open('zckquotes', 'wb') as fp:
    pickle.dump(filtered, fp)

