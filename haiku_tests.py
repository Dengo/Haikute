import unittest
import haiku
from our_dict import naomis_dict


class testHaiku(unittest.TestCase):
    def setUp(self):
        self.hk = haiku.Haiku()
        self.word_list = str(self.hk).split('\n')
        first_word_possibilities = ['NN5', 'NNS5', 'D1', 'D2', 'P1', 'P2']
        last_word_possibilities = ['NN5', 'NNS5', 'NN4', 'NNS4', 'NN1', 'NNS1']
        self.first_word = []
        self.last_word = []
        for poss in first_word_possibilities:
            for w in naomis_dict[poss]:
                self.first_word.append(w)
        for poss in last_word_possibilities:
            for w in naomis_dict[poss]:
                self.last_word.append(w)

        # self.NPs = [
        #     ["NN5"],  # noun, common, singular or mass is NN
        #     ["NNS5"],  # noun, common, plural is NNS
        #     ["D1", "NN4"],
        #     ["D1", "NNS4"],
        #     ["D2", "Adj2", "NN1"],
        #     ["D2", "Adj2", "NNS1"],
        # ]

        # self.PPs = [
        #     ["P2", "D1", "NN2"],
        #     ["P1", "D1", "NNS3"],
        # ]

        # self.TPs = [
        #     ["V3", "P2", "D1", "NN1"],
        #     ["V3", "P2", "D1", "NNS1"],
        #     ["D1", "NNS1", "V1", "D1", "NN1"],
        # ]

        # self.TTPs = [
        #     ["D1", "D1", "NN2", "NNS1"],
        #     ["Adj2", "D2", "NN1", "NNS1"],
        # ]

    def testLength(self):
        self.assertIn(len(self.word_list[0].split()), range(1, 4))
        self.assertIn(len(self.word_list[1].split()), range(4, 6))
        self.assertIn(len(self.word_list[2].split()), range(1, 4))

    def testWords(self):
        self.assertIn(self.word_list[0].split()[0], self.first_word)
        self.assertIn(self.word_list[2].split()[-1], self.last_word)


if __name__ == '__main__':
    unittest.main()
