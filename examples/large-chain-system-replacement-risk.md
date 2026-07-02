# Example: Large Chain System Replacement Risk

Use this for high-complexity chains considering a fast system replacement.

## User Input

```text
我们是 100 多家店，直营和加盟混合，加盟占大多数。
不同区域 POS 不统一，也用了库存、财务、会员、外卖、排班和 BI。
现在老板要求 3 个月内换系统解决库存和对账问题。
```

## Expected Advisor Response

```text
当前判断：
不建议直接把 3 个月目标定成“全量换系统上线”。
更合理的目标是：完成断点诊断、数据口径统一、试点门店验证和供应商异常场景评估。

问题归因：
- 系统：POS 碎片化，多系统并存，接口和字段口径可能不一致。
- 流程：直营和加盟门店的收货、盘点、报损、调拨执行标准不同。
- 数据衔接：库存、支付、退款、财务入账和 BI 报表之间没有统一追溯链。
- 责任：加盟场景下，总部、门店、加盟商、财务、仓配之间的审核和纠偏边界可能不清。

主要风险：
- 3 个月全量上线容易变成数据迁移和门店执行双重事故。
- 新系统如果不解决加盟店为什么不用、怎么用、谁审核，数据质量仍然会差。
- 如果没有统一 POS 输出标准和主数据规则，新系统接入后仍然需要人工导表。

更可信的 3 个月目标：

第 1-2 周：锁定断点
- 抽 10 个高频 SKU，追进货、配送、收货、销售、报损、盘点。
- 抽 20 笔对账异常，追订单、支付、退款、库存扣减、财务入账。
- 找 2 家直营店和 2 家加盟店蹲点，看哪些动作绕过系统。

第 3-6 周：定口径和责任
- 统一销售额、退款、库存、会员余额、加盟结算的最终口径。
- 定义谁录入、谁审核、谁改错、谁解释最终数字。
- 输出系统需求边界：哪些必须换系统，哪些只是流程和责任问题。

第 7-12 周：试点和供应商评估
- 用真实异常场景考供应商，不看标准演示。
- 先在少量直营和加盟门店试点。
- 用试点结果决定是否进入分批上线。

如果老板要一个结论：
现在不是“能不能换系统”的问题，而是“能不能先把数据和责任链路理清，再分批换系统”。
```

## Notes

- Do not make every dimension score identical.
- Use risk levels when the input is not structured enough for precise scoring.
- Avoid saying "all dimensions hit bottom" unless every dimension has explicit evidence.
