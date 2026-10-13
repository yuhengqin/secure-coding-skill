"""Exercise real queries against disposable, in-memory data."""

import sqlite3
import unittest

from orders import get_order


class OrderQueryTests(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.addCleanup(self.connection.close)
        self.connection.execute(
            "CREATE TABLE orders (id TEXT PRIMARY KEY, user_id INTEGER, note TEXT)"
        )
        self.connection.executemany(
            "INSERT INTO orders VALUES (?, ?, ?)",
            [
                ("order-a", 7, "your order"),
                ("order-b", 8, "someone else's order"),
                ("owner's-order", 7, "a literal quote in the identifier"),
            ],
        )

    def query(self, order_id, user_id=7):
        return get_order(
            self.connection, order_id, authenticated_user_id=user_id
        )

    def test_owner_can_read_order(self):
        self.assertEqual(self.query("order-a"), ("order-a", "your order"))

    def test_other_users_order_is_not_returned(self):
        self.assertIsNone(self.query("order-b"))

    def test_missing_order_is_not_returned(self):
        self.assertIsNone(self.query("missing-order"))

    def test_sql_syntax_remains_data(self):
        self.assertIsNone(self.query("order-b' OR 1=1 --"))
        self.assertEqual(
            self.query("owner's-order"),
            ("owner's-order", "a literal quote in the identifier"),
        )

    def test_missing_or_invalid_identity_is_rejected(self):
        for identity in (None, 0, -1, True, "7", 2**63):
            with self.subTest(identity=identity), self.assertRaises(PermissionError):
                self.query("order-a", identity)

    def test_invalid_identifier_is_rejected(self):
        for identifier in (None, 42, "", "x" * 65):
            with self.subTest(identifier=identifier), self.assertRaises(ValueError):
                self.query(identifier)


if __name__ == "__main__":
    unittest.main()
