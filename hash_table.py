class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hash_key = self.hash(key)
        
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
        
        self.collection[hash_key][key] = value

    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            del(self.collection[hash_key][key])
            return ("deleted!")
        return 
     

    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            return self.collection[hash_key][key]
        return None

test = HashTable()
test.add('golf', 'sport')
print(test.hash('golf'))
print(test.lookup('golf'))
print(test.remove('golf'))