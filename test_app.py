import unittest
import app

#Tests to make sure the user inputs for items are being modified by the _calculate_stats function
class TestCompareItems(unittest.TestCase):
    def test_item1_calculated(self):
        player_class = "Druid"
        specialization = "Feral Dps"
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

#Test to make sure the user inputs for items being compared properly.
    def test_item_comparison(self):
        player_class = "Druid"
        specialization = "Feral Dps"
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

#Test to make sure output is a string
    def test_comparison_type(self):
        player_class = "Druid"
        specialization = "Feral Dps"
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


        self.assertTrue(app._compare_items(item1_calc, item2_calc).isalpha)
  
if __name__ == "__main__":
    unittest.main()