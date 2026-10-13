# 实际案例：只读取自己的订单

这个小案例展示如何把安全规则落实为查询代码和可重复的检查。实现与测试只用 Python 标准库，数据库存在于内存，不需要凭据或外部服务。

## 请求与边界

> 为 Python 服务实现订单查询：沿用已有登录态，用户只能读取自己的订单；检查输入、SQL 查询和权限边界，并完成相关测试。

本案例实现其中的数据读取函数。调用方必须先完成认证与操作权限检查，并从**服务端已验证的身份**传入 `authenticated_user_id`；不能把请求中的 `user_id` 当作登录身份。函数对身份数值的校验本身不构成认证。

示例约定订单 ID 是 1–64 字符的不透明字符串，用户 ID 是正的 SQLite 64 位整数。这是本案例的数据契约，不是适用于所有项目的通用规则。

## 从规则到实现

先读 [共性入口](../../skills/secure-coding/references/common.md) 和 [Python 索引](../../skills/secure-coding/references/python.md)，再读相关正文。以下行号对应随包原文快照，可用 `guide.py show` 定位：

| 规则 | 原文位置 | 本案例的落实方式 |
|---|---|---|
| `PY-BACKEND-1.1.1` 按类型进行数据校验 | [Python 指南](../../skills/secure-coding/sources/Python安全指南.md)，153–173 行 | 校验订单 ID 的类型/长度，以及用户 ID 的类型/范围 |
| `PY-BACKEND-1.2.1` 使用参数化查询 | 同上，177–262 行 | 使用 `?` 占位符与独立参数元组 |
| `PY-BACKEND-1.8.1` 默认鉴权 | 同上，479–481 行 | 调用方负责认证与操作权限；函数拒绝缺失/无效身份 |
| `PY-BACKEND-1.8.3` 避免越权访问 | 同上，489–498 行 | 查询同时匹配订单 ID 和服务端传入的用户 ID |

在本仓库根目录读取正文：

```sh
python skills/secure-coding/scripts/guide.py show PY-BACKEND-1.1.1 PY-BACKEND-1.2.1 PY-BACKEND-1.8.1 PY-BACKEND-1.8.3
```

例如，下面的**问题代码示意**同时存在直接拼接输入与缺少订单归属条件的问题；它不是一次无技能模型的实测输出：

```python
# 仅用于说明问题，不作为可执行示例。
connection.execute(f"SELECT id, note FROM orders WHERE id = '{order_id}'")
```

[orders.py](orders.py) 中的完整实现为：

```python
import sqlite3


def get_order(
    connection: sqlite3.Connection,
    order_id: str,
    *,
    authenticated_user_id: int | None,
) -> tuple[str, str] | None:
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
```

此处省略了源码的说明性 docstring。SQL 结构固定，参数通过驱动绑定。合法 ID 中的单引号保留为数据，无需手工转义；不属于当前用户和不存在的订单都返回 `None`。参数绑定方式依据 [Python sqlite3 官方文档](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders)。

## 可重复验证

需 Python 3.10+ 且包含标准库 `sqlite3`。在本仓库根目录运行：

```sh
python -B -m unittest discover -s examples/order-query -p test_orders.py -v
```

[test_orders.py](test_orders.py) 建立一次性内存数据库，验证六项行为：

1. 用户可以读取自己的订单。
2. 查询其他用户的订单返回 `None`。
3. 查询不存在的订单返回 `None`。
4. 注入形态的输入不扩大查询范围，含单引号的合法 ID 仍可读取。
5. 缺失身份，以及零、负数、布尔值、字符串或溢出的用户 ID 均被拒绝。
6. 非字符串、空字符串和过长的订单 ID 均被拒绝。

**实际结果：2026-10-13，Windows / Python 3.14.2，6 项测试通过，退出状态 0。** 工作流也已加入此测试命令，其他平台以实际 CI 结果为准。

这验证了上述数据契约和查询行为。HTTP 登录、会话、操作级授权、真实数据库集成及项目安全扫描不在本案例内；它也不能证明使用技能比不使用技能更可靠。业务项目应接入已有认证链路并运行自己的相关检查。
