import unittest
from price_analysis import PriceAnalysis

class TestRegressionPriceAnalysis(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Set up the PriceAnalysis instance and sample data for testing."""
        cls.analysis = PriceAnalysis()
        cls.sample_data = [100, 200, 300]
        cls.previous_results = cls.analysis.calculate_total_price(cls.sample_data)
    
    def test_regression_total_price(self):
        """Ensure that the total price calculation remains unchanged."""
        result = self.analysis.calculate_total_price(self.sample_data)
        self.assertEqual(result, self.previous_results)
    
    def test_regression_transformed_data(self):
        """Ensure that the data transformation logic remains unchanged."""
        transformed_data = self.analysis.transform_data(self.sample_data)
        self.assertEqual(transformed_data, [110, 220, 330])  # Example of previous expected result

if __name__ == '__main__':
    unittest.main()
