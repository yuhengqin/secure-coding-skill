"""Small SQLite example; not a web endpoint or authentication implementation."""

import sqlite3


def get_order(
    connection: sqlite3.Connection,
    order_id: str,
    *,
    authenticated_user_id: int | None,
) -> tuple[str, str] | None:
    """Read an owned order. The caller must supply a server-verified identity.

    This demo uses a 1-64 character opaque identifier and a positive SQLite
    INTEGER user ID. A request parameter is not an authenticated identity.
    """
    if (
        type(authenticated_user_id) is not int
        or not 0 < authenticated_user_id <= 2**63 - 1
    ):
        raise PermissionError("A verified user identity is required")
    if not isinstance(order_id, str) or not 1 <= len(order_id) <= 64:
        raise ValueError("Order ID must contain 1-64 characters")

    return connection.execute(
        "SELECT id, note FROM orders WHERE id = ? AND user_id = ?",
        (order_id, authenticated_user_id),
    ).fetchone()
