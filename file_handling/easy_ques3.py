#waf to find in which line of the file does the word learning exist..


word="learning"
data=True
line_no=1
with open("practice.txt","r") as f:
 while data:
  data=f.readline()
  if (word in data):
   print(line_no)
  line_no+=1