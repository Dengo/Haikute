#!/usr/bin/env Python

paradigms = {("NP", "TP", "NP"): 65.0, ("PP", "TP", "NP"): 35.0}
# paradigms = [["NP", "TP", "NP"], ["PP", "TP", "NP"]]

# --------- KEY ---------
# __# = syllable count
# C__ = begins with consonant
# V__ = begins with vowel
# CNN = singular/mass common noun (1-5)
# CNNS = plural common noun (1-5)
# D = determiner (1-2)
# DS = determiner for plural noun (1)
# P = preposition (1-2)
# ADJ = adjective (1-4)
# ADV = adverb (C2-6, V1-6)
# VBD = past tense verb (1-5)
# VBP = present/3rd-person/non-singular verb (1-5)
# VBZ = present/3rd-person/singular verb (1-5)
# VBG = present participle (2-5)


NPs = {("CNN5", ): 0.5,  # consonants - singular
       ("D1", "CNN4"): 1.0,
       ("D2", "CADJ2", "CNN1"): 1.0,
       ("D1", "CADJ1", "CNN3"): 2.0,
       ("D1", "CADJ2", "CNN2"): 3.0,
       ("D1", "CADJ3", "CNN1"): 2.0,
       ("CADJ1", "CNN4"): 1.0,
       ("CADJ2", "CNN3"): 2.0,
       ("CADJ3", "CNN2"): 2.0,
       ("CADJ4", "CNN1"): 2.0,
       ("CADJ2", "CADJ2", "CNN1"): 3.0,
       ("CADJ3", "CADJ1", "CNN1"): 2.0,
       ("CADJ1", "CADJ3", "CNN1"): 2.0,
       ("CADV2", "CADJ2", "CNN1"): 3.0,

       # consonants - plural
       ("CNNS5", ): 0.5,
       ("DS1", "CNNS4"): 1.0,
       ("DS1", "CADJ1", "CNNS3"): 1.5,
       ("DS1", "CADJ2", "CNNS2"): 1.5,
       ("DS1", "CADJ3", "CNNS1"): 1.5,
       ("CADJ1", "CNNS4"): 1.0,
       ("CADJ2", "CNNS3"): 2.0,
       ("CADJ3", "CNNS2"): 2.0,
       ("CADJ4", "CNNS1"): 2.0,
       ("CADJ2", "CADJ2", "CNNS1"): 3.0,
       ("CADJ3", "CADJ1", "CNNS1"): 2.0,
       ("CADJ1", "CADJ3", "CNNS1"): 2.0,
       ("CADV2", "CADJ2", "CNNS1"): 3.0,

       # vowels - singular
       ("VNN5", ): 0.5,
       ("D1", "VNN4"): 1.0,
       ("D2", "VADJ2", "VNN1"): 1.0,
       ("D1", "VADJ1", "VNN3"): 2.0,
       ("D1", "VADJ2", "VNN2"): 3.0,
       ("D1", "VADJ3", "VNN1"): 3.0,
       ("VADJ1", "VNN4"): 1.0,
       ("VADJ2", "VNN3"): 2.0,
       ("VADJ3", "VNN2"): 2.0,
       ("VADJ4", "VNN1"): 2.0,
       ("VADJ2", "VADJ2", "VNN1"): 3.0,
       ("VADJ3", "VADJ1", "VNN1"): 2.0,
       ("VADJ1", "VADJ3", "VNN1"): 2.0,
       ("VADV2", "VADJ2", "VNN1"): 3.0,

       # vowels - plural
       ("VNNS5", ): 0.5,
       ("DS1", "VNNS4"): 1.0,
       ("DS1", "VADJ1", "VNNS3"): 1.5,
       ("DS1", "VADJ2", "VNNS2"): 1.5,
       ("DS1", "VADJ3", "VNNS1"): 1.5,
       ("VADJ1", "VNNS4"): 1.0,
       ("VADJ2", "VNNS3"): 2.0,
       ("VADJ3", "VNNS2"): 2.0,
       ("VADJ4", "VNNS1"): 2.0,
       ("VADJ2", "VADJ2", "VNNS1"): 3.0,
       ("VADJ3", "VADJ1", "VNNS1"): 2.0,
       ("VADJ1", "VADJ3", "VNNS1"): 2.0,
       ("VADV2", "VADJ2", "VNNS1"): 3.0
       }

PPs = {("P1", "D1", "CADJ2", "CNN1"): 3.8,  # consonants - singular
       ("P1", "D1", "CADJ1", "CNN2"): 3.8,
       ("P1", "D1", "CADJ1", "CADJ1", "CNN1"): 2.0,
       ("P1", "D1", "CADV1", "CADJ1", "CNN1"): 2.0,
       ("P2", "D1", "CADJ1", "CNN1"): 3.0,
       ("P1", "D1", "CNN3"): 3.8,

       # consonants - plural
       ("P1", "DS1", "CADJ2", "CNNS1"): 3.8,
       ("P1", "DS1", "CADJ1", "CNNS2"): 3.8,
       ("P1", "DS1", "CADJ1", "CADJ1", "CNNS1"): 2.0,
       ("P1", "CADV2", "CADJ1", "CNNS1"): 3.8,
       ("P1", "CADJ3", "CNNS1"): 3.8,
       ("P2", "DS1", "CADJ1", "CNNS1"): 3.0,
       ("P2", "CADJ2", "CNNS1"): 3.8,
       ("P1", "CADJ2", "CNNS2"): 3.8,
       ("P1", "DS1", "CNNS3"): 3.8,

       # vowels - singular
       ("P1", "D1", "VADJ2", "VNN1"): 3.8,
       ("P1", "D1", "VADJ1", "VNN2"): 3.8,
       ("P1", "D1", "VADJ1", "VADJ1", "VNN1"): 2.0,
       # ("P1", "D1", "VADV1", "VADJ1", "VNN1"): 2.0,
       ("P2", "D1", "VADJ1", "VNN1"): 3.0,
       ("P1", "D1", "VNN3"): 3.8,

       # vowels - plural
       ("P1", "DS1", "VADJ2", "VNNS1"): 3.8,
       ("P1", "DS1", "VADJ1", "VNNS2"): 3.8,
       ("P1", "DS1", "VADJ1", "VADJ1", "VNNS1"): 2.0,
       ("P1", "VADV2", "VADJ1", "VNNS1"): 3.8,
       ("P1", "VADJ3", "VNNS1"): 3.8,
       ("P2", "DS1", "VADJ1", "VNNS1"): 3.0,
       ("P2", "VADJ2", "VNNS1"): 3.8,
       ("P1", "VADJ2", "VNNS2"): 3.8,
       ("P1", "DS1", "CNNS3"): 3.8
       }

TPs = {("CADV5", "VBD2"): 1.0,  # consonants - singular
       ("CADV6", "VBD1"): 1.0,
       ("VBD2", "CADV5"): 1.0,
       ("VBD1", "CADV6"): 1.0,
       ("D1", "CNN1", "VBD1", "P2", "CNNS2"): 1.0,  # past
       ("D1", "CNN1", "VBZ1", "P2", "CNNS2"): 1.0,  #
       ("D1", "CNN2", "VBD1", "P2", "CNNS1"): 1.0,  # past
       ("D1", "CNN2", "VBZ1", "P2", "CNNS1"): 1.0,  #
       ("D1", "CNN1", "VBD1", "VADV4"): 1.0,  # past
       ("D1", "CNN1", "VBZ1", "VADV4"): 1.0,  #
       ("D1", "CNN2", "VBD1", "VADV3"): 1.0,  # past
       ("D1", "CNN2", "VBZ1", "VADV3"): 1.0,  #
       ("D1", "CNN1", "VBD1", "CADV4"): 1.0,  # past
       ("D1", "CNN1", "VBZ1", "CADV4"): 1.0,  #
       ("VBG3", "P2", "D1", "CNN1"): 1.0,  # present participle
       ("VBG2", "P1", "D1", "CNN3"): 1.0,  # present participle
       ("VBG2", "P1", "D1", "CADJ2", "CNN1"): 1.0,  # present participle
       ("D1", "CNN2", "P1", "CNNS1", "VBZ2"): 1.0,  #
       ("D1", "CNN1", "P1", "CNNS1", "VBZ3"): 1.0,  #
       ("D1", "CNN1", "P1", "CNNS2", "VBZ2"): 1.0,  #
       ("D1", "CNN1", "P1", "CNNS1", "VBG3"): 1.0,  # present participle
       ("D1", "CNN1", "P1", "CNNS2", "VBG2"): 1.0,  # present participle
       ("D1", "CADV3", "VBG3"): 1.0,  # present participle
       ("D1", "CADV2", "VBG4"): 1.0,  # present participle
       ("CADV3", "VADV3", "VBD1"): 1.0,

       # consonants - plural
       ("CNNS3", "VBD1", "CADV3"): 1.0,  # past
       ("CNNS3", "VBD1", "VADV3"): 1.0,  #
       ("DS1", "CNNS2", "VBD1", "P2", "CNN1"): 1.0,  # past
       ("DS1", "CNNS2", "VBD1", "P2", "CNNS1"): 1.0,  # past
       ("DS1", "CNNS2", "VBP1", "P2", "CNN1"): 1.0,
       ("DS1", "CNNS2", "VBP1", "P2", "CNNS1"): 1.0,
       ("DS1", "CNNS1", "VBD1", "P2", "CNN2"): 1.0,  # past
       ("DS1", "CNNS1", "VBD1", "P2", "CNNS2"): 1.0,  # past
       ("DS1", "CNNS1", "VBP1", "P2", "CNN2"): 1.0,
       ("DS1", "CNNS1", "VBP1", "P2", "CNNS2"): 1.0,
       ("VBG3", "P2", "DS1", "CNNS1"): 1.0,  # present participle
       ("VBG2", "P1", "DS1", "CNNS3"): 1.0,  # present participle
       ("VBG2", "P1", "DS1", "CADJ2", "CNNS1"): 1.0,
       ("DS1", "CNNS2", "P1", "CNNS1", "VBP2"): 1.0,
       ("DS1", "CNNS1", "P1", "CNNS2", "VBP2"): 1.0,
       ("CNNS3", "P1", "CNNS1", "VBP2"): 1.0,
       ("CNNS2", "P1", "CNNS1", "VBP3"): 1.0,
       ("CNNS1", "P1", "CNNS3", "VBP2"): 1.0,
       ("CNNS1", "P1", "CNNS2", "VBP3"): 1.0,
       ("CNNS3", "P1", "CNNS1", "VBG2"): 1.0,  # present participle
       ("CNNS2", "P1", "CNNS1", "VBG3"): 1.0,  # present participle
       ("CNNS1", "P1", "CNNS3", "VBG2"): 1.0,  # present participle
       ("CNNS1", "P1", "CNNS2", "VBG3"): 1.0,  # present participle
       ("CADJ3", "CNNS1", "VBG3"): 1.0,  # present participle
       ("VADJ3", "CNNS1", "VBG3"): 1.0,  # present participle

       # vowels - singular
       ("VADV5", "VBD2"): 1.0,
       ("VADV6", "VBD1"): 1.0,
       ("VBD2", "VADV5"): 1.0,
       ("VBD1", "VADV6"): 1.0,
       ("D1", "VNN2", "VBD1", "P2", "VNNS1"): 1.0,  # past
       ("D1", "VNN2", "VBZ1", "P2", "VNNS1"): 1.0,
       ("D1", "VNN1", "VBD1", "P2", "VNNS2"): 1.0,  # past
       ("D1", "VNN1", "VBZ1", "P2", "VNNS2"): 1.0,
       ("D1", "VNN1", "VBD1", "VADV4"): 1.0,  # past
       ("D1", "VNN1", "VBZ1", "VADV4"): 1.0,  #
       ("D1", "VNN2", "VBD1", "VADV3"): 1.0,  # past
       ("D1", "VNN2", "VBZ1", "VADV3"): 1.0,  #
       ("D1", "VNN1", "VBD1", "CADV4"): 1.0,  # past

       ("D1", "VNN1", "VBZ1", "CADV4"): 1.0,  #
       ("VBG3", "P2", "D1", "VNN1"): 1.0,
       ("VBG2", "P1", "D1", "VNN3"): 1.0,
       ("VBG2", "P1", "D1", "VADJ2", "VNN1"): 1.0,
       ("D1", "VNN2", "P1", "VNNS1", "VBZ2"): 1.0,
       ("D1", "VNN1", "P1", "VNNS1", "VBZ3"): 1.0,
       ("D1", "VNN1", "P1", "VNNS2", "VBZ2"): 1.0,
       ("D1", "VNN1", "P1", "VNNS1", "VBG3"): 1.0,
       ("D1", "VNN1", "P1", "VNNS2", "VBG2"): 1.0,
       ("D1", "VADV3", "VBG3"): 1.0,  # present participle
       ("D1", "VADV2", "VBG4"): 1.0,  # present participle
       ("VADV3", "CADV3", "VBD1"): 1.0,

       # vowels - plural
       ("VNNS3", "VBD1", "CADV3"): 1.0,  # past
       ("VNNS3", "VBD1", "VADV3"): 1.0,  #
       ("DS1", "VNNS2", "VBD1", "P1", "D1", "VNN1"): 1.0,  # past
       ("DS1", "VNNS2", "VBD1", "P2", "VNNS1"): 1.0,  # past
       ("DS1", "VNNS2", "VBP1", "P1", "D1", "VNN1"): 1.0,
       ("DS1", "VNNS2", "VBP1", "P2", "VNNS1"): 1.0,
       ("DS1", "VNNS1", "VBD1", "P2", "VNN2"): 1.0,  # past
       ("DS1", "VNNS1", "VBD1", "P2", "VNNS2"): 1.0,  # past
       ("DS1", "VNNS1", "VBP1", "P2", "VNN2"): 1.0,
       ("DS1", "VNNS1", "VBP1", "P2", "VNNS2"): 1.0,
       ("VBG3", "P2", "DS1", "VNNS1"): 1.0,  # present participle
       ("VBG2", "P1", "DS1", "VNNS3"): 1.0,  # present participle
       ("VBG2", "P1", "DS1", "VADJ2", "VNNS1"): 1.0,
       ("DS1", "VNNS2", "P1", "VNNS1", "VBP2"): 1.0,
       ("DS1", "VNNS1", "P1", "VNNS2", "VBP2"): 1.0,
       ("VNNS3", "P1", "VNNS1", "VBP2"): 1.0,
       ("VNNS2", "P1", "VNNS1", "VBP3"): 1.0,
       ("VNNS1", "P1", "VNNS3", "VBP2"): 1.0,
       ("VNNS1", "P1", "VNNS2", "VBP3"): 1.0,
       ("VNNS3", "P1", "VNNS1", "VBG2"): 1.0,  # present participle
       ("VNNS2", "P1", "VNNS1", "VBG3"): 1.0,  # present participle
       ("VNNS1", "P1", "VNNS3", "VBG2"): 1.0,  # present participle
       ("VNNS1", "P1", "VNNS2", "VBG3"): 1.0,  # present participle
       ("CADJ3", "VNNS1", "VBG3"): 1.0,  # present participle
       ("VADJ3", "VNNS1", "VBG3"): 1.0  # present participle

       }

# def check_syllables(dictionary, desired):
#       for k, val in dictionary.iteritems():
#             count = 0
#             for word in k:
#                   count += int(word[-1])
#             if count != desired:
#                   print k

# if __name__ == '__main__':
#       check_syllables(NPs, 5)
#       check_syllables(TPs, 7)
#       check_syllables(PPs, 5)
