from queue import Queue

class Tree:
    def __init__(self, info, children):
        self.info = info
        self.children = children
        
    def get_children(self):
        return self.children

       
def build_tree(str_info, cache):#str_info is an array of strings
    """
    str_info: a string of the topic name
    cache: a dictionary of type QueryCache that stores refrences to Tree objects corresponding to a unique topic name
    returns a Tree object that contains multiple children
    """
    info = str_info.pop(0)
    children = read_children(str_info, cache)
    t = Tree(info, children)
    cache.insert(info, t)
    return t
def read_children(str_info, cache):
        """
        read_children is a helper function that parses the information in parenthesis 
        returns a list of children (Tree refrences) 
        """
        ret_list = []
        if (len(str_info)== 0 or str_info[0]!='('):
            return None
        else:# reading '('
            str_info.pop(0)# pop off '('
            while True:#keep reading children until we hit a ')'
              
                ret_list.append(build_tree(str_info, cache))#each child is treated as a new tree
                if( str_info[0] == ')'):
                    str_info.pop(0)#pop off any ')'
                    break;
              
                
        
        return ret_list 
        

def match_prefix(str1,str2):
    """
    returns true if either string is a prefix of one anohter, false otherwise
    """
    length = min(len(str1), len(str2))
    
    for i in range(length):
        if (str1[i] != str2[i]):
            return False
   
    return True
    
def search_tree(dictionary, tree, question):#BF search of the tree till we hit the desired topic
    """
    dictionary: is an actual dictionary that holds every topic as key and a list of questions corresponding to those topics as values
    tree: a reference to a node in the tree that holds root information of the desired queried topic
    question: the queestion part related to the query (string)
    returns an integer count for the number of occurences of the question as a prefix within the desired range of topics
    """
    sub_q = Queue()
    sub_q.put(tree)
    total = 0
    while(not sub_q.empty ()):
        removed = sub_q.get()
       
        try:
            query_values = dictionary[removed.info]
            for query in query_values:
               
                if (match_prefix(query, question)):
                    total+=1
        except KeyError:
            pass
                
        children = removed.children
        if (children):
            for item in children:
                sub_q.put(item)
    
    return total
   
    
class CacheQuery:#not really needed for now, but is very useful for further search and memory optimization 
    def __init__(self):
        self.cache = {}
    def __getitem__(self, node_name):#returns a reference down the tree of the given node name(string)
        return self.cache[node_name]

    def insert(self, node_name, tree_node):
        self.cache[node_name] = tree_node
        
def main():
    q_dictionary = {};
    
    cache = CacheQuery()
    size = int(input())#I was actual able to parese the flat tree string without the use of its size
    
    tree = build_tree(input().split(' '), cache)
    questions = int(input())
    
    
    for _ in range(questions):
        line = input().split(':')# split :
        key = line[0]
        value = line[1][1:]
        if key not in q_dictionary:
            q_dictionary[key] = [value]
        else:
            q_dictionary[key].append(value)
            
    num_queries = int(input())

    total = []
    for _ in range(num_queries):
        l = input().split()
        q = [l[0], ' '.join(l[1:])]
        
        total.append(search_tree(q_dictionary,cache[q[0]],q[1]))
      
    for num in total:
        print (num)
    
       
    
if __name__ == '__main__':
    main()  
        
    
            
