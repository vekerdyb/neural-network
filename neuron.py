class Neuron(object):
    def __init__(self, num_inputs, weights, threshold):
        self.num_inputs = num_inputs
        self.weights = weights
        self.threshold = threshold

    def get_output(self, inputs):
        return [self.weights[i] * inp for i, inp in enumerate(inputs)]


class Layer(object):
    def __init__(self, neurons):
        self.neurons = neurons
        self.outputs = []

    def feed(self, inputs):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.get_output(inputs))
        self.outputs = outputs
        return outputs

    def __repr__(self):
        return ' | '.join([str(o) for o in self.outputs])


def create_dummy_layer():
    n1 = Neuron(num_inputs=2, weights=[.75, .25], threshold=0.5)
    n2 = Neuron(num_inputs=2, weights=[.05, .95], threshold=1)
    l1 = Layer([n1, n2])
    l1.feed([1, 2])
    print(l1)
