# Example: Problem Diagnosis Before System Replacement

Use this example when a user asks whether a messy operating problem means they should replace systems.

## User Input

```text
我们现在 3 家店，用了收银、小程序、库存系统和财务软件，
但库存和月底对账总是不准。是不是该换系统？
```

## Expected Advisor Response

```text
先别急着换系统。

当前判断：
你这个问题更像是订单渠道、库存动作和财务口径之间没有闭环。
现在可以怀疑系统衔接，但还不能直接判断“该换系统”。

问题归因：
- 系统：可能有接口、字段或库存扣减规则不一致。
- 流程：门店收货、报损、调拨、盘点可能没有按当天动作完成。
- 数据衔接：订单、支付、退款、库存扣减、财务入账之间可能没有一条可追溯链路。
- 责任边界：库存差异和对账差异出现后，可能没人负责解释最终口径。

主要风险：
如果现在直接换系统，新系统可能只是把旧问题换成新界面。
真正要先确认的是：差异到底集中在系统交接处，还是集中在门店执行、仓库审核、财务补录这些动作上。

下一步动作：
1. 抽 10 个高频 SKU，连续 7 天核对系统库存、实盘、收货、销售扣减、报损、调拨和人工修改记录。
2. 找最近一笔月底对账差异，从订单、支付、退款、库存扣减、报损、调拨一路追到财务入账。
3. 标出每个断点：是系统没有传、流程没有做、数据口径不一致，还是没人审核。

检查清单：
- 门店当天收货是否当天入系统？
- 报损、报溢、调拨是否有审核人？
- 库存系统和财务软件之间是否自动同步，还是人工导表？
- 月底差异由谁确认，谁修正，谁负责解释？
- 同一笔订单能否从收银/线上订单一路追到库存和财务？

如果断点集中在系统交接处，再考虑集成或换系统；
如果断点在门店没录、仓库没审、财务月底补，
换系统只会把问题换个界面继续发生。
```

## Notes

- Do not name specific vendors.
- Do not provide a vendor ranking.
- Do not jump directly into a long readiness report unless the user asks for a full check.
- Keep the answer practical and easy for a restaurant owner to act on.
