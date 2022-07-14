import unittest
import app

class TestCompareItems(unittest.TestCase):
    def test_item1_calculated(self):
        player_class = "Druid"
        specialization = "Feral DPS"
        item1 = {
            "strength": 12,
            "agility": 12,
            "attack power": 12,
            "crit": 12,
            "hit": 12,
            "haste": 12,
            "expertise": 12,
            "armor penetration": 12,
        }
        self.assertNotEqual(item1, app._calculate_stats(player_class, specialization, item1))

    def test_item_comparison(self):
        player_class = "Druid"
        specialization = "Feral DPS"
        item1 = {
            "strength": 12,
            "agility": 12,
            "attack power": 12,
            "crit": 12,
            "hit": 12,
            "haste": 12,
            "expertise": 12,
            "armor penetration": 12,
        }
        item2 = {
            "strength": 10,
            "agility": 10,
            "attack power": 10,
            "crit": 10,
            "hit": 10,
            "haste": 10,
            "expertise": 10,
            "armor penetration": 10,
        }
        item1_calc = app._calculate_stats(player_class, specialization, item1)
        item2_calc = app._calculate_stats(player_class, specialization, item2)

        self.assertEqual("item1", app._compare_items(item1_calc, item2_calc))
  
if __name__ == "__main__":
    unittest.main()