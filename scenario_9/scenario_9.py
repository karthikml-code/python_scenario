votes = ['john', 'johnny', 'jackie', 'jackie', 'john', 'jackie', 'jamie', 'jamie', 'john', 'jackie', 'jamie', 'johnny', 'john']
#we are going to use counters package from collections
#Counter gives the key value pair information of item and count values
from collections import Counter

count = Counter(votes) #to get the key value pair information
mx = max(count.values()) #to get max votes

top = [k for k,v in count.items() if v == mx] #it will bring the top values based on mx
top.sort() # sorting if there is any clash 
top[0] #picking up the first record 

