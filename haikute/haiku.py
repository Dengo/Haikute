import random
import lea
from Haikute_Dictionary import naomis_dict
from Paradigms_Phrases import paradigms, NPs, PPs, TPs


class Haiku(object):
    def __init__(self):
        try:
            phrase_dict = {'NP': NPs, 'PP': PPs, 'TP': TPs}
            self.result = ''
            para = lea.Lea.fromValFreqsDict(paradigms)
            phrases = para.random(1)[0]
            for p in phrases:
                phrase = lea.Lea.fromValFreqsDict(phrase_dict[p])
                line = phrase.random(1)[0]
                self.string_line = ''
                prev = ""
                for w in line:
                    if w == "D1":
                        dets = lea.Lea.fromValFreqsDict(naomis_dict[w])
                        word = dets.random(1)[0]
                    elif w == "P1":
                        prep = lea.Lea.fromValFreqsDict(naomis_dict[w])
                        word = prep.random(1)[0]
                    else:
                        word = random.choice(naomis_dict[w])
                    if w[0] == 'V' and prev == "a":
                        self.string_line += "n %s" % word
                    else:
                        self.string_line += " %s" % word
                    prev = word
                self.result += "%s\n" % self.string_line[1:]
        except IndexError:
            print "Error!"

    def __str__(self):
        return self.result  # [:-1]


if __name__ == '__main__':
    h = Haiku()
    print h
