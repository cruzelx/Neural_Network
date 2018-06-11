import random,math
class Perceptron:
    def __init__(self,weights):
        self.weights = weights
        for i in range(len(self.weights)):
           self.weights[i] = random.randint(-1,1)

    def activation(self,n):
        print(1/(1+math.exp(-n)))

  
    def guess(self,inputs):
        sum=0
        for i in range(len(self.weights)):
            sum += self.weights[i]*inputs[i]
        self.activation(sum)
    

X = Perceptron([1,2,3])
X.guess([1,-1,2])
