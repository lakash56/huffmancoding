from collections import Counter
class Node(object):
    def __init__(self,left=None, right=None):
       
        self.left = left      
        self.right = right
    def getChild(self):
        return self.right, self.left

def make_the_tree(sorted_frequency):
    
    while len(sorted_frequency)>1:
        
        sorted_frequency =sorted_frequency[2:]
        key1, value1 =sorted_frequency[0]
        key2, value2 = sorted_frequency[1]
        
        #print(value1,value2)
        new_value=value1+value2
        new_node = Node(key1, key2)
        sorted_frequency.append((new_node,new_value))
        
        sorted_frequency = sorted(sorted_frequency, key=lambda item: item[1])
    
    
        
        #sort again
        print(sorted_frequency[0][0])
    return sorted_frequency[0][0]    
message = 'AAABBBBBBEEEDABEEDCC'
#count the char

#print(Counter(message))
frequency = (Counter(message))
#print(frequency['A'])
sorted_frequency = sorted(frequency.items(), key=lambda item: item[1])

#lamda = ??

#print(sorted_frequency) {'D': 2, 'C': 2, 'A': 4, 'E': 5, 'B': 7}

root=make_the_tree(sorted_frequency)

huffman_code = get_code(root)
#sort them from samll to big

#make the tree by combining the smallest one and delete those guys
