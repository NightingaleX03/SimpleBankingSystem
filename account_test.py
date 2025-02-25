import unittest
import os
from account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        if os.path.exists('accounts.json'): # Backup the original accounts.json file if it exists
            os.rename('accounts.json', 'accounts_backup.json')

    def tearDown(self):
        if os.path.exists('accounts.json'): # Remove the accounts.json file after each test
            os.remove('accounts.json')
        if os.path.exists('accounts_backup.json'): # Restore the original accounts.json file if it was backed up
            os.rename('accounts_backup.json', 'accounts.json')

    def test_generate_unique_id(self):
        account = Account()
        unique_id = account.generate_unique_id()
        self.assertIsInstance(unique_id, int)
        self.assertGreaterEqual(unique_id, 0)
        self.assertLessEqual(unique_id, 1000000000)

    def test_account_creation_with_new_id(self):
        account = Account()
        self.assertIsNotNone(account.id)
        self.assertEqual(account.balance, 0)
        self.assertEqual(account.transactions, {})

    def test_account_creation_with_existing_id(self):
        account = Account(id=12345)
        self.assertEqual(account.id, 12345)

    def test_deposit(self):
        account = Account()
        account.deposit(100)
        self.assertEqual(account.balance, 100)

    def test_withdraw(self):
        account = Account()
        account.deposit(100)
        account.withdraw(50)
        self.assertEqual(account.balance, 50)

    def test_view_account(self):
        account = Account()
        account.deposit(100)
        account.view_account()

if __name__ == '__main__':
    unittest.main()
