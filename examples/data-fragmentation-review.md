# Example: Data Fragmentation Review

Use this when the user says each platform has separate data, such as POS, delivery, loyalty, inventory, accounting, or reporting systems all producing different numbers.

## User Input

```text
我们主要问题是数据割裂。收银、外卖、会员、库存、财务每个平台数据独立，
老板每天看报表都对不上。应该先整合，还是直接换系统？
```

## Expected Advisor Response

```text
这个不是单纯“缺系统”，而是典型的数据衔接问题。

当前判断：
先不要从“整合还是换系统”开始。
先确认每个关键数字的最终来源，也就是谁是 source of truth。

问题归因：
- 系统：各平台都有自己的数据口径，但没有统一主数据源。
- 流程：订单取消、退款、报损、调拨这些异常动作可能没有统一回写路径。
- 数据衔接：订单、支付、库存、会员、财务之间缺少可追溯链路。
- 责任：当两个系统数字不一致时，没人定义以哪个为准、谁来修正。

先做一张主数据表：

| 指标 | 当前来源 | 最终口径 | 冲突时以谁为准 | 负责人 |
|---|---|---|---|---|
| 销售额 | 收银 / 外卖 / 财务 | 待确认 | 待确认 | 待确认 |
| 库存数 | 库存系统 / 门店实盘 / 央厨配送 | 待确认 | 待确认 | 待确认 |
| 会员余额 | 会员系统 / 收银 / 小程序 | 待确认 | 待确认 | 待确认 |
| 退款金额 | 支付 / 外卖 / 财务 | 待确认 | 待确认 | 待确认 |

再追一条真实交易链路：

订单 -> 支付 -> 优惠/退款 -> 库存扣减 -> 报损/调拨 -> 会员余额 -> 财务入账 -> 经营报表

下一步动作：
1. 抽最近 20 笔有退款、优惠、外卖取消或库存异常的订单。
2. 对每一笔订单标出数据从哪个平台产生、什么时候同步、同步到哪里。
3. 找出第一个数字分叉点。
4. 先定义主数据和冲突规则，再谈接口、数据中台或换系统。

如果只是平台之间没有接口，系统整合可能有效；
如果连最终口径和责任人都没有定义，直接换系统也会继续对不上。
```

## Notes

- Do not name specific vendors.
- Start from source-of-truth decisions, not vendor categories.
- The answer should make the user feel the problem is diagnosable, not mysterious.
