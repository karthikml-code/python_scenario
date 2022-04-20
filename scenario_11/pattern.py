import re

topic = ['start of the pattern','This is the content we are trying to capture since its in the middle of two texts(start of the pattern)','some random text','end of pattern']

#this will search and topic list for the topics[0] and topics[3] and returns everything thats inbetween them. 
#we can also use the string here. 
re.search(rf'{str(topics[0]).strip()}(.*?){str(topics[3]).strip()}', str(headings)).group(1)
