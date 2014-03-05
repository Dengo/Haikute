#!/usr/bin/env Python

# **** account for a/an

paradigms = [
            ["NP", "TP", "NP"],
            ["PP", "TP", "NP"],
# ["NP", "TransTP", "NP"]
]

# NN = singular/mass common nouns... [NN1, NN2, NN3, NN4, NN5]
# NNS = plural common nouns... [NNS1, NNS2, NNS3, NNS4, NNS5]
# D = determiner... [D1, D2]
# DS = determiner for plural noun... [DS1, DS2]
# P = preposition... [P1, P2]
# ADJ = adjective... [ADJ1, ADJ2, ADJ3, ADJ4]
# ADV = adverb... [ADV1, ADV2]
# VBD = past tense verb... [VBD1]
# VBP = present tense 3rd-person non-singular verb... [VBP1, VBP2, VBP3]
# VBZ = present tense 3rd-person singular verb... [VBZ1, VBZ2, VBZ3]
# VBG = present participle... [VBG2, VBG3]

NPs = [
      ["NN5"],  # singular
      ["D1", "NN4"],
      ["D2", "ADJ2", "NN1"],
      ["D1", "ADJ1", "NN3"],
      ["D1", "ADJ2", "NN2"],
      ["D1", "ADJ3", "NN1"],
      ["ADJ1", "NN4"],
      ["ADJ2", "NN3"],
      ["ADJ3", "NN2"],
      ["ADJ4", "NN1"],
      ["ADJ2", "ADJ2", "NN1"],
      ["ADJ3", "ADJ1", "NN1"],
      ["ADJ1", "ADJ3", "NN1"],
      ["ADV2", "ADJ2", "NN1"],
      ["NNS5"],  # plural
      ["DS1", "NNS4"],
      ["DS2", "ADJ2", "NNS1"],
      ["DS1", "ADJ1", "NNS3"],
      ["DS1", "ADJ2", "NNS2"],
      ["DS1", "ADJ3", "NNS1"],
      ["ADJ1", "NNS4"],
      ["ADJ2", "NNS3"],
      ["ADJ3", "NNS2"],
      ["ADJ4", "NNS1"],
      ["ADJ2", "ADJ2", "NNS1"],
      ["ADJ3", "ADJ1", "NNS1"],
      ["ADJ1", "ADJ3", "NNS1"],
      ["ADV2", "ADJ2", "NNS1"]
]

PPs = [
      ["P1", "D1", "ADJ1", "NN2"],  # singular
      ["P1", "D1", "ADJ1", "ADJ1", "NN1"],
      ["P1", "D1", "ADV1", "ADJ1", "NN1"],
      ["P2", "D1", "ADJ1", "NN1"],
    # ["P2", "ADJ2", "NN1"],
    # ["P1", "ADJ2", "NN2"],
      ["P1", "D1", "NN3"],
      ["P1", "DS1", "ADJ1", "NNS2"],  # plural
      ["P1", "DS1", "ADJ1", "ADJ1", "NNS1"],
      ["P1", "ADV2", "ADJ1", "NNS1"],
      ["P1", "ADJ3", "NNS1"],
      ["P2", "DS1", "ADJ1", "NNS1"],
      ["P2", "ADJ2", "NNS1"],
      ["P1", "ADJ2", "NNS2"],
      ["P1", "DS1", "NNS3"]
]

TPs = [
    # ["D1", "NN1", "VBD1", "P2", "NN1"],  # singular
      ["D1", "NN1", "VBD1", "P2", "NNS1"],
    # ["D1", "NN1", "VBZ1", "P2", "NN1"],
      ["D1", "NN1", "VBZ1", "P2", "NNS1"],
      ["VBG3", "P2", "D1", "NN1"],
      ["VBG2", "P1", "D1", "NN3"],
      ["VBG2", "P1", "D1", "ADJ2", "NN1"],
    # ["D1", "NN2", "P1", "NN1", "VBZ2"],
    # ["D1", "NN1", "P1", "NN2", "VBZ2"],
      ["D1", "NN2", "P1", "NNS1", "VBZ2"],
      ["D1", "NN1", "P1", "NNS1", "VBZ3"],
      ["D1", "NN1", "P1", "NNS2", "VBZ2"],
      ["D1", "NN1", "P1", "NNS1", "VBG3"],
      ["D1", "NN1", "P1", "NNS2", "VBG2"],


      ["DS1", "NNS1", "VBD1", "P2", "NN1"],  # plural
      ["DS1", "NNS1", "VBD1", "P2", "NNS1"],
      ["DS1", "NNS1", "VBP1", "P2", "NN1"],
      ["DS1", "NNS1", "VBP1", "P2", "NNS1"],
      ["VBG3", "P2", "DS1", "NNS1"],
      ["VBG2", "P1", "DS1", "NNS3"],
      ["VBG2", "P1", "DS1", "ADJ2", "NNS1"],
      ["DS1", "NNS2", "P1", "NNS1", "VBP2"],
      ["DS1", "NNS1", "P1", "NNS2", "VBP2"],
      ["NNS3", "P1", "NNS1", "VBP2"],
      ["NNS2", "P1", "NNS1", "VBP3"],
      ["NNS1", "P1", "NNS3", "VBP2"],
      ["NNS1", "P1", "NNS2", "VBP3"],
      ["NNS3", "P1", "NNS1", "VBG2"],
      ["NNS2", "P1", "NNS1", "VBG3"],
      ["NNS1", "P1", "NNS3", "VBG2"],
      ["NNS1", "P1", "NNS2", "VBG3"],

]
