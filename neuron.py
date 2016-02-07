class Neuron(object):
    def __init__(self, num_inputs, weights, threshold):
        self.num_inputs = num_inputs
        self.weights = weights
        self.threshold = threshold

    def get_output(self, inputs):
        return inputs


class Layer(object):
    def __init__(self, neurons):
        self.neurons = neurons
        self.outputs = []

    def feed(self, inputs):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.get_ouput(inputs))
        self.outputs = outputs
        return outputs

    def __repr__(self):
        template = ('{} | ' * len(self.neurons)).strip()
        import ipdb; ipdb.set_trace()
        return template.format(*[o for o in self.outputs])

