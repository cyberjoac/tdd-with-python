from unittest.case import skip
from functional_tests.base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.fail("Write me!")
