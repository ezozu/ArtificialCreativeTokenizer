# test_artificialcreativetokenizer.py
"""
Tests for ArtificialCreativeTokenizer module.
"""

import unittest
from artificialcreativetokenizer import ArtificialCreativeTokenizer

class TestArtificialCreativeTokenizer(unittest.TestCase):
    """Test cases for ArtificialCreativeTokenizer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtificialCreativeTokenizer()
        self.assertIsInstance(instance, ArtificialCreativeTokenizer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtificialCreativeTokenizer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
