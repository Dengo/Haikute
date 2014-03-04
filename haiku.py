import random
from test_dict import naomis_dict

paradigms = [
    ["NP", "TP", "NP"],
    ["PP", "TP", "NP"],
    ["NP", "TransTP", "NP"]
]

NPs = [
    ["NN5"],  # noun, common, singular or mass is NN
    ["NNS5"],  # noun, common, plural is NNS
    ["D1", "NN4"],
    ["D1", "NNS4"],
    ["D2", "Adj2", "NN1"],
    ["D2", "Adj2", "NNS1"],
    # ["D1", "Adj1", "NN3"],
    # ["D1", "Adj1", "NNS3"],
    # ["D1", "Adj2", "NN2"],
    # ["D1", "Adj2", "NNS2"],
    # ["D1", "Adj3", "NN1"],
    # ["D1", "Adj3", "NNS1"],
    # ["Adj1", "NN4"],
    # ["Adj1", "NNS4"],
    # ["Adj2", "NN3"],
    # ["Adj2", "NNS3"],
    # ["Adj3", "NN2"],
    # ["Adj3", "NNS2"],
    # ["Adj4", "NN1"],
    # ["Adj4", "NNS1"],
    # ["Adv2", "Adj2", "NN1"],
    # ["Adv2", "Adj2", "NNS1"]
]

PPs = [
    ["P2", "D1", "NN2"],
    ["P1", "D1", "NNS3"],
]

TPs = [
    ["V3", "P2", "D1", "NN1"],
    ["V3", "P2", "D1", "NNS1"],
    ["D1", "NNS3", "V1", "D1", "NN1"],
]

TTPs = [
    ["NN2", "V1", "D1", "NN2", "NNS1"],
    ["D1", "Adj2", "D2", "NN1", "NNS1"],
]


class Haiku(object):
    def __init__(self):
        phrase_dict = {'NP': NPs, 'PP': PPs, 'TP': TPs, 'TransTP': TTPs}
        self.result = ''
        phrases = random.choice(paradigms)
        for p in phrases:
            line = random.choice(phrase_dict[p])
            self.string_line = ''
            for w in line:
                self.string_line += " %s" % random.choice(naomis_dict[w])
            self.result += "%s\n" % self.string_line[1:]

    def __str__(self):
        return self.result


if __name__ == '__main__':
    h = Haiku()
    print h
