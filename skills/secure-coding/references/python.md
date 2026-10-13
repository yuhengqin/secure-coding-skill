# python 规则索引

共 45 条。由 scripts/guide.py 生成。

先读适用的完整规则正文和解释；标题及原文级别不等于已验证的当前实现。
使用 `python scripts/guide.py show <ID>` 取得带行号正文及本技能解释。
脚本路径以技能目录为基准；没有 Python 时，按下表行号直接读取 sources 文件。


## 通用类 / I. 代码实现 / 1.1 加密算法

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-COMMON-1.1.1 | 必须 | 避免使用不安全的对称加密算法 | [75–77](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | [INT-AEAD](interpretations.md#int-aead) |

## 通用类 / I. 代码实现 / 1.2 程序日志

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-COMMON-1.2.1 | 建议 | 对每个重要行为都记录日志 | [81–83](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-COMMON-1.2.2 | 建议 | 禁止将未经验证的用户输入直接记录日志 | [86–88](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-COMMON-1.2.3 | 建议 | 避免在日志中保存敏感信息 | [91–93](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 通用类 / I. 代码实现 / 1.3 系统口令

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-COMMON-1.3.1 | 必须 | 禁止使用空口令、弱口令、已泄露口令 | [98–98](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-COMMON-1.3.2 | 必须 | 口令强度要求 | [100–107](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | [INT-PASSWORD-POLICY](interpretations.md#int-password-policy) |
| PY-COMMON-1.3.3 | 必须 | 口令存储安全 | [109–113](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | [INT-PASSWORD-STORAGE](interpretations.md#int-password-storage) |
| PY-COMMON-1.3.4 | 必须 | 禁止传递明文口令 | [115–115](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-COMMON-1.3.5 | 必须 | 禁止在不安全的信道中传输口令 | [117–117](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 通用类 / II. 配置&环境 / 2.1 Python版本选择

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-COMMON-2.1.1 | 建议 | 使用Python 3.6+的版本 | [123–129](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | [INT-RUNTIME](interpretations.md#int-runtime) |

## 通用类 / II. 配置&环境 / 2.2 第三方包安全

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-COMMON-2.2.2 | 必须 | 禁止使用不安全的组件 | [133–133](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 通用类 / II. 配置&环境 / 2.3 配置信息

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-COMMON-2.3.1 | 必须 | 密钥存储安全 | [137–139](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-COMMON-2.3.2 | 必须 | 禁止硬编码敏感配置 | [142–144](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.1 输入验证

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-BACKEND-1.1.1 | 必须 | 按类型进行数据校验 | [153–173](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.2 SQL操作

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-BACKEND-1.2.1 | 必须 | 使用参数化查询 | [177–262](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.2.2 | 必须 | 对参数进行过滤 | [264–275](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.3 执行命令

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-BACKEND-1.3.1 | 建议 | 避免直接调用函数执行系统命令 | [279–282](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.3.2 | 必须 | 过滤传入命令执行函数的字符 | [284–300](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | [INT-COMMAND](interpretations.md#int-command) |
| PY-BACKEND-1.3.3 | 必须 | 禁止不安全的代码执行 | [302–304](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.4 文件操作

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-BACKEND-1.4.1 | 必须 | 文件类型限制 | [308–324](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | [INT-UPLOAD-EXT](interpretations.md#int-upload-ext) |
| PY-BACKEND-1.4.2 | 必须 | 禁止外部文件存储于可执行目录 | [326–328](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.4.3 | 必须 | 避免路径穿越 | [331–344](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.4.4 | 必须 | 禁用XML外部实体的方法 | [346–354](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.4.5 | 必须 | 禁用不安全的反序列化函数 | [356–358](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.4.6 | 建议 | 避免路径拼接 | [360–362](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.4.7 | 建议 | 文件名hash化处理 | [365–376](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.5 网络请求

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-BACKEND-1.5.1 | 必须 | 限定访问网络资源地址范围 | [382–404](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.6 响应输出

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-BACKEND-1.6.1 | 必须 | 设置正确的HTTP响应包类型 | [408–409](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.6.2 | 必须 | 设置安全的HTTP响应头 | [411–422](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | [INT-FRAME](interpretations.md#int-frame) |
| PY-BACKEND-1.6.3 | 必须 | 对外输出页面包含第三方数据时须进行编码处理 | [424–433](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | [INT-XSS-CONTEXT](interpretations.md#int-xss-context) |

## 后台类 / I. 代码实现 / 1.7 数据输出

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-BACKEND-1.7.1 | 必须 | 敏感数据加密存储 | [437–441](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.7.2 | 必须 | 敏感信息必须由后台进行脱敏处理 | [443–445](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.7.3 | 必须 | 高敏感信息禁止存储、展示 | [448–451](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.7.4 | 必须 | 个人敏感信息脱敏展示 | [453–460](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.7.5 | 必须 | 隐藏后台地址 | [462–474](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.8 权限管理

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-BACKEND-1.8.1 | 必须 | 默认鉴权 | [479–481](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.8.2 | 必须 | 授权遵循最小权限原则 | [484–486](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.8.3 | 必须 | 避免越权访问 | [489–498](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.8.4 | 建议 | 及时清理不需要的权限 | [500–502](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.9 异常处理

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-BACKEND-1.9.1 | 必须 | 不向对外错误提示 | [507–510](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.9.2 | 必须 | 禁止异常抛出敏感信息 | [512–512](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.10 Flask安全

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-BACKEND-1.10.1 | 必须 | 生产环境关闭调试模式 | [516–516](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.10.2 | 建议 | 遵循Flask安全规范 | [518–520](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.11 Django安全

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| PY-BACKEND-1.11.1 | 必须 | 生产环境关闭调试模式 | [525–525](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| PY-BACKEND-1.11.2 | 建议 | 保持Django自带的安全特性开启 | [527–531](../sources/Python%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
