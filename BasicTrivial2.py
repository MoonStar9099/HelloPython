import random
#declaring all variables
userAnswer = ''
global userInCorAnsws
global userCorrAnsws
userInCorAnsws = 0
userCorrAnsws = 0
printCount = 0
global quesNum
quesNum = 1

def BasicTrivia():
    questionBank =  {'Bananas emit non-lethal levels of gamma radiation': True, 'Avacadoes emit more radiation than bananas': False,
                    "The tallest mountain in the solar system is on Jupiter": False, 'Grapes can kill a dog': True,
                    "Dogs can eat mangoes and bananas as special treats": True, "Blueberries can be used to teach dogs to catch treats in the air": True,
                    "'A' is the letter used most in the English language": False, 'In Harry Potter, Draco Malfoy has no siblings': False,
                    "The star sign Aquarius is represented by a tiger": True

                }

class Question:
    
    def __init__(self, level,quesName,answerChoices, corrAns,multiChoice=True):
        self.quesName = quesName
        self.level = level
        self.answerChoices = answerChoices
        self.corrAns = corrAns
        self.multiChoice = multiChoice


    def getQuestionName(self):
        return(self.quesName)
        
    def getQuestionAnswers(self):    
        return(self.answerChoices)
    
    def getCorrectAnswer(self):
        return(self.corrAns)


    def getQuestionLevel(self):
        return(self.level, self.multiChoice)


q1 = Question("Easy", "Which is the most radioactive?", ["A) banana", "B) grape", "C) avocado", "D) pineapple"],
              "A) banana", True)

q2 = Question("Easy", "Which is least radioactive, yet still is radioactive?", ["A) banana", "B) grape", "C) avocado", "D) pineapple"],
              "B) grape", True)

q3 = Question("Easy", "Which is not radioactive?", ["A) banana", "B) grape", "C) avocado", "D) pineapple"],
              "D) pineapple", True)

q4 = Question("Easy", "Which is the sweetest?", ["A) banana", "B) grape", "C) avocado", "D) pineapple"],
              "D) pineapple", True)


q5 = Question("Easy", "Which is the most common?", ["A) banana", "B) grape", "C) avocado", "D) pineapple"],
       "A) banana", True)

q6 = Question("Easy", "The tallest mountain in the solar system is on Jupiter", ["A) True", "B) False"], "B) False", False)

q7 = Question("Medium", "'Bananas emit non-lethal levels of gamma radiation", ["A) True", "B) False"], "A) True", False)

q8 = Question("Easy", "'A' is the letter used most in the English language", ["A) True", "B) False"], "B) False", False )

q9 = Question("Medium", 'Grapes can kill a dog', ["A) True", "B) False"], "A) True", False)

q10 = Question("Easy", "A group of kittens is called a 'kindle'", ["A) True", "B) False"], "A)", False)

q11 = Question("Medium", "'Avocadoes emit more radiation than bananas'", ["A) True", "B) False"], "B) False", False)

q12 = Question("Easy", "Blueberries can be used to teach dogs to catch treats in the air", ["A) True", "B) False"], "A) True", False)

q13 = Question("Easy", "The star sign Aquarius is represented by a tiger", ["A) True", "B) False"], "B) False", False)

q14 = Question("Medium", "' In Harry Potter, Draco Malfoy has no siblings'", ["A) True", "B) False"], "B) False", False)

q15 = Question("Medium", "The cat breed 'Angora' is just that-- a cat breed.", ["A) True", 'B) False"'], "B) False", False)


questionBank = [q1, q6, q2, q7, q3, q8, q4, q9, q5, q10, q11, q12, q13, q14, q15]

def PrintQuestions():    
    for current in questionBank:
        print(current.getQuestionName()())
        print(current.getQuestionAnswers())
        print("\n")

        
def getCorrect(self,backupCorr,backupInCorr):
                userCorrAnsws = backupCorr
                userInCorrAnsws = backupInCorr
                userAnswer = str(input())
                if userAnswer == self.getCorrectAnswer() or userAnswer in self.getCorrectAnswer()[0:2]:
                    userCorrAnsws += 1
                    print("Correct! The correct answer is ", self.getCorrectAnswer())
                                    
                elif userAnswer in self.getQuestionAnswers() and userAnswer not in self.getCorrectAnswer()[0:2]: 
                    userInCorAnsws += 1
                    print("Incorrect! The correct answer is ", self.getCorrectAnswer())
                            
                else:
                    print("We're sorry, that's not an answer. Perhaps there's a typo?")
                    backupInCorr = userInCorrAnsws
                    backupCorr = userCorrAnsws
                    getCorrect(self, backupCorr, backupInCorr)

def AskQuestions():
    quesNum = 1
    for current in questionBank:
        print("#",quesNum,".")
        quesNum += 1
        print(current.getQuestionName())
        for i in current.getQuestionAnswers():
            print(i)
            print('\n')
        
            
        getCorrect(current, 0, 0)
    print('You got ', userCorrAnsws, 'correct, and', userInCorAnsws, "incorrect.")    
AskQuestions()