class Node:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
        self.next =None 

class Interlacedlist:
    def __init__(self):
        self.head=None 

    def add(self, name, phoneNumber):
        new_node = Node(name, phoneNumber)
        new_node.next = self.head
        self.head = new_node


    def search(self, name):
        actual = self.head 
        while actual:
            if actual.name == name:
                return actual.phoneNumber
            actual = actual.next 
        return None 
    
    def delete(self,name):
       actual = self.head
       previus = None
       while actual:
           if actual.name == name: 
              if previus:
               previus.next=actual.next
              else: 
                 self.head = actual.next
              return True
           previus = actual
           actual =actual.siguiente 
       return False


class TableHash:
    def __init__(self, size=10): 
        self.size = size 
        self.table = [Interlacedlist() for _ in range(size)]

    def _hash(self, Key):
        return sum(ord(c)for c in Key)% self.size
    
    def add(self, name, phoneNumber):
        index = self._hash(name)
        self.table[index].add(name, phoneNumber)

    def search(self,name):
        index = self._hash(name)
        return self.table[index].search(name)
    
    def delete(self,name):
        index = self._hash(name)
        return self.table[index].delete(name)
    
directory = TableHash()
directory.add("Juan", "12345678")
directory.add("Pedro", "12345678")
directory.add("Carlos", "13131221")

print(directory.search("Juan"))  # Debería imprimir "12345678"
print(directory._hash("Juan"))  # Debería imprimir "0"

directory.delete("Pedro")  
print(directory.search("Pedro"))  # Debería imprimir "None"