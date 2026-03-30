#create a class ScoreBoard
#Add an __init__ with a score parameter and store it as a private attribute
#Add a method called get_score that returns the private score
#Create an object s1 with a score of 0
#Print the score of s1






class scoreBoard:
    def __init__(self,score,name):
        self._score=score
        self.name=name

    def show(self):
        print("the name is:" , self.name)

    def get_score(self):
     return self._score
    
s1 =scoreBoard(0,"AKSHAT")
print(s1.get_score())
s1.show()