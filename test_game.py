import unittest
from game import Game
from main import calculate_player_score, calculate_suit_score

game_obj = Game(6, 5)


class TestCalculatePlayerScore(unittest.TestCase):
    def test_calculate_player_score(self):
        player_cards1 = [
            "10_of_clubs",
            "13_of_clubs",
            "5_of_clubs",
            "3_of_hearts",
            "12_of_hearts",
        ]
        player_cards2 = [
            "4_of_diamonds",
            "6_of_diamonds",
            "6_of_hearts",
            "4_of_hearts",
            "13_of_diamonds",
        ]
        player_cards3 = [
            "10_of_hearts",
            "9_of_hearts",
            "13_of_spades",
            "7_of_diamonds",
            "8_of_spades",
        ]
        player_cards4 = [
            "8_of_diamonds",
            "3_of_diamonds",
            "11_of_hearts",
            "2_of_spades",
            "13_of_clubs",
        ]
        player_cards5 = [
            "12_of_diamonds",
            "14_of_diamonds",
            "3_of_clubs",
            "5_of_diamonds",
            "4_of_spades",
        ]
        self.assertEqual(calculate_player_score(player_cards1), 43, "Should be 43")
        self.assertEqual(calculate_player_score(player_cards2), 33, "Should be 33")
        self.assertEqual(calculate_player_score(player_cards3), 47, "Should be 47")
        self.assertEqual(calculate_player_score(player_cards4), 37, "Should be 37")
        self.assertEqual(calculate_player_score(player_cards5), 35, "Should be 35")

    def test_calculate_suit_score(self):
        player_cards1 = [
            "10_of_clubs",
            "13_of_clubs",
            "5_of_clubs",
            "3_of_hearts",
            "12_of_hearts",
        ]
        player_cards2 = [
            "4_of_diamonds",
            "6_of_diamonds",
            "6_of_hearts",
            "4_of_hearts",
            "13_of_diamonds",
        ]
        self.assertEqual(calculate_suit_score(player_cards1), 256, "Should be 256")
        self.assertEqual(calculate_suit_score(player_cards2), 4, "Should be 4")

    def test_deal_cards(self):
        dealt_cards = game_obj.deal_cards()
        self.assertEqual(len(dealt_cards), 6, "Should be 6")
        self.assertEqual(len(dealt_cards[0]), 5, "Should be 5")
        self.assertEqual(len(dealt_cards[1]), 5, "Should be 5")
        self.assertEqual(len(dealt_cards[2]), 5, "Should be 5")
        self.assertEqual(len(dealt_cards[3]), 5, "Should be 5")
        self.assertEqual(len(dealt_cards[4]), 5, "Should be 5")
        self.assertEqual(len(dealt_cards[5]), 5, "Should be 5")


if __name__ == "__main__":
    unittest.main()
