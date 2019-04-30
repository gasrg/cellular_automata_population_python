import unittest

import Model


class TestModel(unittest.TestCase):
    def setUp(self):
        """Set up a model"""
        self.model = Model.Model()
        self.model.run()

    def test_model(self):
        """Test that the model is not null"""
        self.assertIsNotNone(self.model)

    def test_cells(self):
        """Test that the cells exist"""
        self.assertIsNotNone(self.model.cells)

    def test_count(self):
        """Test that the count is not negative"""
        model = Model.Model()
        model.run()
        for step, c in enumerate(model.count_alive):
            with self.subTest(step=step):
                self.assertGreater(c, 0, "Count is less that zero at step = {}".format(step))


if __name__ == "__main__":
    unittest.main()
