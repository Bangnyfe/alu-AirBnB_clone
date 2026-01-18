#!/usr/bin/python3
"""Unit tests for Review class."""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review class."""

    def test_review_inherits_from_base_model(self):
        """Test that Review inherits from BaseModel."""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_review_has_place_id_attribute(self):
        """Test that Review has place_id attribute."""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertEqual(review.place_id, "")

    def test_review_has_user_id_attribute(self):
        """Test that Review has user_id attribute."""
        review = Review()
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertEqual(review.user_id, "")

    def test_review_has_text_attribute(self):
        """Test that Review has text attribute."""
        review = Review()
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.text, "")

    def test_review_place_id_is_string(self):
        """Test that place_id is a string."""
        review = Review()
        self.assertIsInstance(review.place_id, str)

    def test_review_user_id_is_string(self):
        """Test that user_id is a string."""
        review = Review()
        self.assertIsInstance(review.user_id, str)

    def test_review_text_is_string(self):
        """Test that text is a string."""
        review = Review()
        self.assertIsInstance(review.text, str)

    def test_review_place_id_assignment(self):
        """Test that place_id can be assigned."""
        review = Review()
        review.place_id = "place-123"
        self.assertEqual(review.place_id, "place-123")

    def test_review_user_id_assignment(self):
        """Test that user_id can be assigned."""
        review = Review()
        review.user_id = "user-456"
        self.assertEqual(review.user_id, "user-456")

    def test_review_text_assignment(self):
        """Test that text can be assigned."""
        review = Review()
        review.text = "Great place to stay!"
        self.assertEqual(review.text, "Great place to stay!")

    def test_review_to_dict_contains_class(self):
        """Test that to_dict contains __class__ key."""
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')

    def test_review_instance_creation(self):
        """Test that a Review instance is created correctly."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))

    def test_review_str_representation(self):
        """Test the string representation of Review."""
        review = Review()
        string = str(review)
        self.assertIn('[Review]', string)
        self.assertIn(review.id, string)


if __name__ == '__main__':
    unittest.main()
