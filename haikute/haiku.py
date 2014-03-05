import random
from Haikute_Dictionary import naomis_dict
from Paradigms_Phrases import paradigms, NPs, PPs, TPs


class Haiku(object):
    def __init__(self):
        try:
            phrase_dict = {'NP': NPs, 'PP': PPs, 'TP': TPs}
            self.result = ''
            phrases = random.choice(paradigms)
            for p in phrases:
                line = random.choice(phrase_dict[p])
                print line
                self.string_line = ''
                prev = ''
                for w in line:
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
