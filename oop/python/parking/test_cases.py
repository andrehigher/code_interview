import unittest
from user import User

class UserTests(unittest.TestCase):
	
	def test_users_init(self):
		""" User should be initialized properly.
        """
		user_obj = User('Andre', 25)
		self.assertIsInstance(user_obj, User)

	def test_users_properties(self):
		""" User should have properties defined.
        """
		user_obj = User('Andre', 25)
		self.assertEqual(user_obj.name, 'Andre')
		self.assertEqual(user_obj.age, 25)
		self.assertEqual(user_obj.active, False)
		self.assertEqual(user_obj.warning, 0)

	def test_users_status(self):
		""" User should have 2 states: active and inactive.
        """
		user_obj = User('Andre', 25)
		user_obj.set_active()
		self.assertTrue(user_obj.active)
		user_obj.set_inactive()
		self.assertFalse(user_obj.active)
	
	def test_users_warning(self):
		""" User should be able to receive warning.
        """
		user_obj = User('Andre', 25)
		user_obj.set_warning()
		self.assertEqual(user_obj.warning, 1)
		user_obj.set_warning()
		self.assertEqual(user_obj.warning, 2)

	def test_users_inactive_by_warnings(self):
		""" User should be inactive if have 3 warnings.
        """
		user_obj = User('Andre', 25)
		user_obj.set_active()
		user_obj.set_warning()
		user_obj.set_warning()
		user_obj.set_warning()
		self.assertFalse(user_obj.active)

	def test_users_clean_warning(self):
		""" User should be cleaned of warnings.
        """
		user_obj = User('Andre', 25)
		user_obj.set_active()
		user_obj.set_warning()
		user_obj.set_warning()
		user_obj.set_warning()
		user_obj.clean_warning()
		self.assertEqual(user_obj.warning, 0)
		self.assertTrue(user_obj.active)
	
class CarTests(unittest.TestCase):
    	
    def test_car_init(self):
    	pass

if __name__ == '__main__':
    unittest.main()