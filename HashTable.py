class HashClass:
        def __init__(self):
                self.Max = 100
                self.arr = [None for i in range(self.Max)]
        def get_Hash(self, key):
                count = 0
                for k in key:
                        count += ord(k)
                return count % self.Max
        def add(self, key, value):
                h = self.get_Hash(key)
                self.arr[h] = value
                print("Insertion into the hashtable successful")
        def get(self, key):
                h = self.get_Hash(key)
                return self.arr[h]
        def __setitem__(self, key, value):
                h = self.get_Hash(key)
                self.arr[h] = value
                print("Insertion into the hashtable successful")
        def __getitem__(self, key):
                h = self.get_Hash(key)
                return self.arr[h]
hc = HashClass()
a = hc.add("Mahesh Vardhan", 100)
print(hc.get("Mahesh Vardhan"))
print(hc.arr)
