from neuralnetwork.FeedForward import FeedForward
from neuralnetwork.Sigmoid import Sigmoid
from neuralnetwork.Backpropagation import Backpropagation

sigmoid = Sigmoid()

networkLayer = [2,2,1]

feedForward = FeedForward(networkLayer, sigmoid)

backpropagation = Backpropagation(feedForward,0.7,0.3)

trainingSet = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

while True:
    backpropagation.initialise()
    result = backpropagation.train(trainingSet)

    if(result):
        break

feedForward.activate([0,0])
outputs = feedForward.getOutputs()
print(outputs[0])

feedForward.activate([0,1])
outputs = feedForward.getOutputs()
print(outputs[0])

feedForward.activate([1,0])
outputs = feedForward.getOutputs()
print(outputs[0])

feedForward.activate([1,1])
outputs = feedForward.getOutputs()
print(outputs[0])
