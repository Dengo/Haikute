#!/usr/bin/env Python

# **** account for a/an

paradigms = [
            ["NP", "TP", "NP"],
            ["PP", "TP", "NP"],
    # ["NP", "TransTP", "NP"]
]

# CNN = singular/mass common nouns... [CNN1, CNN2, CNN3, CNN4, CNN5]
# CNNS = plural common nouns... [CNNS1, CNNS2, CNNS3, CNNS4, CNNS5]
# D = determiner... [D1, D2]
# DS = determiner for plural noun... [DS1, DS2]
# P = preposition... [P1, P2]
# CADJ = adjective... [CADJ1, CADJ2, CADJ3, CADJ4]
# CADV = adverb... [CADV1, CADV2]
# VBD = past tense verb... [VBD1]
# VBP = present tense 3rd-person non-singular verb... [VBP1, VBP2, VBP3]
# VBZ = present tense 3rd-person singular verb... [VBZ1, VBZ2, VBZ3]
# VBG = present participle... [VBG2, VBG3]

NPs = [
      ["CNN5"],  # singular
      ["D1", "CNN4"],
      ["D2", "CADJ2", "CNN1"],
      ["D1", "CADJ1", "CNN3"],
      ["D1", "CADJ2", "CNN2"],
      ["D1", "CADJ3", "CNN1"],
      ["CADJ1", "CNN4"],
      ["CADJ2", "CNN3"],
      ["CADJ3", "CNN2"],
      ["CADJ4", "CNN1"],
      ["CADJ2", "CADJ2", "CNN1"],
      ["CADJ3", "CADJ1", "CNN1"],
      ["CADJ1", "CADJ3", "CNN1"],
      ["CADV2", "CADJ2", "CNN1"],
      ["CNNS5"],  # plural
      ["DS1", "CNNS4"],
    # ["DS2", "CADJ2", "CNNS1"],
      ["DS1", "CADJ1", "CNNS3"],
      ["DS1", "CADJ2", "CNNS2"],
      ["DS1", "CADJ3", "CNNS1"],
      ["CADJ1", "CNNS4"],
      ["CADJ2", "CNNS3"],
      ["CADJ3", "CNNS2"],
      ["CADJ4", "CNNS1"],
      ["CADJ2", "CADJ2", "CNNS1"],
      ["CADJ3", "CADJ1", "CNNS1"],
      ["CADJ1", "CADJ3", "CNNS1"],
      ["CADV2", "CADJ2", "CNNS1"],
      ["VNN5"],  # singular
      ["D1", "VNN4"],
      ["D2", "VADJ2", "VNN1"],
      ["D1", "VADJ1", "VNN3"],
      ["D1", "VADJ2", "VNN2"],
      ["D1", "VADJ3", "VNN1"],
      ["VADJ1", "VNN4"],
      ["VADJ2", "VNN3"],
      ["VADJ3", "VNN2"],
      ["VADJ4", "VNN1"],
      ["VADJ2", "VADJ2", "VNN1"],
      ["VADJ3", "VADJ1", "VNN1"],
      ["VADJ1", "VADJ3", "VNN1"],
      ["VADV2", "VADJ2", "VNN1"],
      ["VNNS5"],  # plural
      ["DS1", "VNNS4"],
    # ["DS2", "VADJ2", "VNNS1"],
      ["DS1", "VADJ1", "VNNS3"],
      ["DS1", "VADJ2", "VNNS2"],
      ["DS1", "VADJ3", "VNNS1"],
      ["VADJ1", "VNNS4"],
      ["VADJ2", "VNNS3"],
      ["VADJ3", "VNNS2"],
      ["VADJ4", "VNNS1"],
      ["VADJ2", "VADJ2", "VNNS1"],
      ["VADJ3", "VADJ1", "VNNS1"],
      ["VADJ1", "VADJ3", "VNNS1"],
      ["VADV2", "VADJ2", "VNNS1"]
]

PPs = [
      ["P1", "D1", "CADJ1", "CNN2"],  # singular
      ["P1", "D1", "CADJ1", "CADJ1", "CNN1"],
      ["P1", "D1", "CADV1", "CADJ1", "CNN1"],
      ["P2", "D1", "CADJ1", "CNN1"],
    # ["P2", "CADJ2", "CNN1"],
    # ["P1", "CADJ2", "CNN2"],
      ["P1", "D1", "CNN3"],
      ["P1", "DS1", "CADJ1", "CNNS2"],  # plural
      ["P1", "DS1", "CADJ1", "CADJ1", "CNNS1"],
      ["P1", "CADV2", "CADJ1", "CNNS1"],
      ["P1", "CADJ3", "CNNS1"],
      ["P2", "DS1", "CADJ1", "CNNS1"],
      ["P2", "CADJ2", "CNNS1"],
      ["P1", "CADJ2", "CNNS2"],
      ["P1", "DS1", "CNNS3"],
      ["P1", "D1", "VADJ1", "VNN2"],  # singular
      ["P1", "D1", "VADJ1", "VADJ1", "VNN1"],
      ["P1", "D1", "VADV1", "VADJ1", "VNN1"],
      ["P2", "D1", "VADJ1", "VNN1"],
    # ["P2", "VADJ2", "VNN1"],
    # ["P1", "VADJ2", "VNN2"],
      ["P1", "D1", "VNN3"],
      ["P1", "DS1", "VADJ1", "VNNS2"],  # plural
      ["P1", "DS1", "VADJ1", "VADJ1", "VNNS1"],
      ["P1", "VADV2", "VADJ1", "VNNS1"],
      ["P1", "VADJ3", "VNNS1"],
      ["P2", "DS1", "VADJ1", "VNNS1"],
      ["P2", "VADJ2", "VNNS1"],
      ["P1", "VADJ2", "VNNS2"],
      ["P1", "DS1", "CNNS3"]
]

TPs = [
    # ["D1", "CNN1", "VBD1", "P2", "CNN1"],  # singular
      ["D1", "CNN1", "VBD1", "P2", "CNNS1"],
    # ["D1", "CNN1", "VBZ1", "P2", "CNN1"],
      ["D1", "CNN1", "VBZ1", "P2", "CNNS1"],
      ["VBG3", "P2", "D1", "CNN1"],
      ["VBG2", "P1", "D1", "CNN3"],
      ["VBG2", "P1", "D1", "CADJ2", "CNN1"],
    # ["D1", "CNN2", "P1", "CNN1", "VBZ2"],
    # ["D1", "CNN1", "P1", "CNN2", "VBZ2"],
      ["D1", "CNN2", "P1", "CNNS1", "VBZ2"],
      ["D1", "CNN1", "P1", "CNNS1", "VBZ3"],
      ["D1", "CNN1", "P1", "CNNS2", "VBZ2"],
      ["D1", "CNN1", "P1", "CNNS1", "VBG3"],
      ["D1", "CNN1", "P1", "CNNS2", "VBG2"],


      ["DS1", "CNNS1", "VBD1", "P2", "CNN1"],  # plural
      ["DS1", "CNNS1", "VBD1", "P2", "CNNS1"],
      ["DS1", "CNNS1", "VBP1", "P2", "CNN1"],
      ["DS1", "CNNS1", "VBP1", "P2", "CNNS1"],
      ["VBG3", "P2", "DS1", "CNNS1"],
      ["VBG2", "P1", "DS1", "CNNS3"],
      ["VBG2", "P1", "DS1", "CADJ2", "CNNS1"],
      ["DS1", "CNNS2", "P1", "CNNS1", "VBP2"],
      ["DS1", "CNNS1", "P1", "CNNS2", "VBP2"],
      ["CNNS3", "P1", "CNNS1", "VBP2"],
      ["CNNS2", "P1", "CNNS1", "VBP3"],
      ["CNNS1", "P1", "CNNS3", "VBP2"],
      ["CNNS1", "P1", "CNNS2", "VBP3"],
      ["CNNS3", "P1", "CNNS1", "VBG2"],
      ["CNNS2", "P1", "CNNS1", "VBG3"],
      ["CNNS1", "P1", "CNNS3", "VBG2"],
      ["CNNS1", "P1", "CNNS2", "VBG3"],

    # ["D1", "VNN1", "VBD1", "P2", "VNN1"],  # singular
      ["D1", "VNN1", "VBD1", "P2", "VNNS1"],
    # ["D1", "VNN1", "VBZ1", "P2", "VNN1"],
      ["D1", "VNN1", "VBZ1", "P2", "VNNS1"],
      ["VBG3", "P2", "D1", "VNN1"],
      ["VBG2", "P1", "D1", "VNN3"],
      ["VBG2", "P1", "D1", "VADJ2", "VNN1"],
    # ["D1", "VNN2", "P1", "VNN1", "VBZ2"],
    # ["D1", "VNN1", "P1", "VNN2", "VBZ2"],
      ["D1", "VNN2", "P1", "VNNS1", "VBZ2"],
      ["D1", "VNN1", "P1", "VNNS1", "VBZ3"],
      ["D1", "VNN1", "P1", "VNNS2", "VBZ2"],
      ["D1", "VNN1", "P1", "VNNS1", "VBG3"],
      ["D1", "VNN1", "P1", "VNNS2", "VBG2"],


      ["DS1", "VNNS1", "VBD1", "P2", "VNN1"],  # plural
      ["DS1", "VNNS1", "VBD1", "P2", "VNNS1"],
      ["DS1", "VNNS1", "VBP1", "P2", "VNN1"],
      ["DS1", "VNNS1", "VBP1", "P2", "VNNS1"],
      ["VBG3", "P2", "DS1", "VNNS1"],
      ["VBG2", "P1", "DS1", "VNNS3"],
      ["VBG2", "P1", "DS1", "VADJ2", "VNNS1"],
      ["DS1", "VNNS2", "P1", "VNNS1", "VBP2"],
      ["DS1", "VNNS1", "P1", "VNNS2", "VBP2"],
      ["VNNS3", "P1", "VNNS1", "VBP2"],
      ["VNNS2", "P1", "VNNS1", "VBP3"],
      ["VNNS1", "P1", "VNNS3", "VBP2"],
      ["VNNS1", "P1", "VNNS2", "VBP3"],
      ["VNNS3", "P1", "VNNS1", "VBG2"],
      ["VNNS2", "P1", "VNNS1", "VBG3"],
      ["VNNS1", "P1", "VNNS3", "VBG2"],
      ["VNNS1", "P1", "VNNS2", "VBG3"],

]
