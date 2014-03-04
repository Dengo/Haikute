import unittest
import haiku
from our_dict import naomis_dict


class testHaiku(unittest.TestCase):
    def setUp(self):
        self.hk = haiku.Haiku()
        self.word_list = str(self.hk).split('\n')
        first_word_possibilities = ['NN5', 'NNS5', 'D1', 'D2', 'P1', 'P2']
        last_word_possibilities = ['NN5', 'NNS5', 'NN4', 'NNS4', 'NN1', 'NNS1']
        mid_first_word_possibilities = ['V3', 'D1', 'NN2']
        mid_last_word_possibilities = ['NN1', 'NNS1']
        self.first_word, self.last_word, self.mf_word, self.ml_word = [], [], [], []
        for poss in first_word_possibilities:
            for w in naomis_dict[poss]:
                self.first_word.append(w)
        for poss in last_word_possibilities:
            for w in naomis_dict[poss]:
                self.last_word.append(w)
        for poss in mid_first_word_possibilities:
            for w in naomis_dict[poss]:
                self.mf_word.append(w)
        for poss in mid_last_word_possibilities:
            for w in naomis_dict[poss]:
                self.ml_word.append(w)

    def testLength(self):
        self.assertIn(len(self.word_list[0].split()), range(1, 4))
        self.assertIn(len(self.word_list[1].split()), range(4, 6))
        self.assertIn(len(self.word_list[2].split()), range(1, 4))

    def testWords(self):
        self.assertIn(self.word_list[0].split()[0], self.first_word)
        self.assertIn(self.word_list[2].split()[-1], self.last_word)
        self.assertIn(self.word_list[1].split()[0], self.mf_word)
        self.assertIn(self.word_list[1].split()[-1], self.ml_word)


if __name__ == '__main__':
    unittest.main()
