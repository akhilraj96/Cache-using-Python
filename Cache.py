#List for cache
cache = []     
#List for requests
requests =[]    

def fifo():
    global cache 
    cache = []

    for i in requests:
        if(i in cache):
            print("HIT") 
        else:
            cache.append(i)
            if(len(cache)>8):
                cache = cache[1:]   
            print("MISS")


def lfu():
    global cache
    cache = []
    hits={} #Number of hits per request

    for i in requests:
        if(i in cache):
            print("HIT")
        else:
            if(len(cache)>7):
                min_hit = max(hits.values())
                for j in range(8):
                    if min_hit>hits[cache[j]]:
                        min_hit=hits[cache[j]]

                popvalue=[]
                pop=1000000
                pos=0
                for j in range(8):
                    if(hits[cache[j]] == min_hit):
                        popvalue.append(j)
                        
                if popvalue:
                    for k in popvalue:
                        if pop>cache[k]:
                            pop=cache[k]
                            pos=k   
                            
                cache.pop(pos)
            cache.append(i)
            print("MISS")
        hits[i] = hits.get(i,0) + 1
        
def dataIn():
    print("Please select one of the following option: \n1. FIFO\n2. LFU\nQ. quit")
    choice = input("Enter your choice :")
    if(choice == 'Q' or choice == 'q'):
        quit()
    elif(choice == '1'):
        fifo()
    elif(choice == '2'):
        lfu()
    else:
        print("Invalid option, Please Try again !")       #repeats until the input is valid..!
        dataIn()

while(True):
    requests = []
    #Input request => 0 to stop          
    request = int(input("Please enter the next page to be added to the list of requests ('0' to stop): "))
    while(request != 0):
        requests.append(request)
        request = int(input("Please enter the next page to be added to the list of requests ('0' to stop): "))
    dataIn()
    print(cache)
