import math
class cache_line:
    def __init__(self,address, number_of_ways):
        self.n = number_of_ways
        self.m = int(math.log2(number_of_ways))
        self.myaddress = address
        self.tag_l = []
        self.tag_l.append(self.myaddress[0:7+self.m])
        self.index = self.myaddress[30-(23-self.m):30]
    
    def get_index(self):
        return self.index

    def get_tag(self):
        return self.tag_l[0]

    def get_taglist(self):
        return self.tag_l
    
    def taglist_isfull(self):
        if len(self.get_taglist()) == n :
            return True

    def taglist_isempty(self):
        if len(self.get_taglist()) == 0 :
            return True


def hit_or_miss(obj_, new_obj): # Returns an index acccording to which hit or miss is decided, also performs required operations. 
    index_ = 0
    if obj_.index == new_obj.index:
        if new_obj.get_tag() in obj_.tag_l: # If the object's tag is in the tag list.
            index_ = 1 #HIT
            lru_same = obj_.tag_l.index(new_obj.get_tag())  #LRU replacement
            new_t = obj_.tag_l.pop(lru_same)
            obj_.tag_l.append(new_t)
        
        else:
            if(obj_.taglist_isfull()):
                index_ = 2 # index_ is matching but tag is not (tag list is full)
                obj_.tag_l.pop(0)       #LRU replacement
                obj_.tag_l.append(new_obj.tag_l[0])
                
            else:
                obj_.tag_l.append(new_obj.tag_l[0])
            index_ = 3 # index_ is matching but tag is not (tag list is not full), appends new tag.
    else:
        index_ = 4 # Both index_ and tags are not matching. So, it's a definite miss. Object is added to cache.
    return index_


def hexa_to_binary(hexa_addr): # Converts hexa decimal address to binary.
    new_hexa_addr = hexa_addr[2:]
    binary_addr = "{0:08b}".format(int(new_hexa_addr, 16))
    
    l = 32 - binary_addr.__len__()
    binary_addr = "0"*l + binary_addr 
    return binary_addr

def segregate(input_string): # Segregates file read line into instructon and address
    instruction = input_string[0]
    add = input_string[2:12]
    return [instruction, add]


if __name__ == "__main__":

    n = input("Enter number of ways n:")
    cache_list = [] #cache
    no_of_hits = -1
    no_of_misses = 1
    count_T = 0
    
    f = open("test.trace", "r") #Trace file. Change this to test on other trace files
    count2 = 0
    s = []

    for i in f:
        s.append(hexa_to_binary(segregate(i)[1]))
    
    
    for addr in s:
        count_T += 1
        print(count_T)

        index = 0
        j = 0
        obj_cl = cache_line(addr,n)
        s.pop(0)

        if cache_list.__len__() == 0:
            cache_list.append(obj_cl)

        for obj in cache_list: 
            index = hit_or_miss(obj, obj_cl) 
            if index == 1:
                no_of_hits = no_of_hits + 1
                break

        if index == 4:
            no_of_misses = no_of_misses+1
            cache_list.append(obj_cl)
        
        elif index !=  1:
            no_of_misses = no_of_misses+1 #LRU replacement is used   

    hit_percent = (no_of_hits*(1.0)) / ((1.0)*(no_of_hits+no_of_misses))*(100*1.0)
    print(f.name)
    print ("Number of ways = ", n)
    print ("Number of hits : ", no_of_hits)
    print ("Number of miss : ", no_of_misses)
    print ("Hit percent : ", hit_percent)

    f.close()    
