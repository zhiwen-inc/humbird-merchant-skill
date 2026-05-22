# 查询批量设计

## 接口说明

根据批量设计id查询批量设计信息。

## api_type

```
batch.design.get
```

## 请求方法

GET

## 请求参数

| 参数名          | 类型 | 是否必填 | 说明       |
| --------------- | ---- | -------- | ---------- |
| batch_design_id | Long | **是**   | 批量设计Id |

## 响应参数

| 参数名      | 类型    | 说明                                             |
| ----------- | ------- | ------------------------------------------------ |
| id          | Long    | 批量设计id                                       |
| qty         | Integer | 总数量                                           |
| success_qty | Integer | 成功数量                                         |
| fail_qty    | Integer | 失败数量                                         |
| filter_qty  | Integer | 过滤数量                                         |
| status      | Integer | 状态：1 待处理，2 处理完成，3 处理失败，5 处理中 |
| fail_msg    | String  | 失败信息                                         |
| det_list    | Array   | 明细集合                                         |

### 明细

当status返回2或3的时候，才会返回明细。

| 参数名              | 类型    | 说明                                               |
| ------------------- | ------- | -------------------------------------------------- |
| id                  | Long    | 批量设计详情id                                     |
| product_id          | Long    | 定制产品id                                         |
| small_product_image | String  | 定制产品主图，小尺寸： 500*500                     |
| large_product_image | String  | 定制产品主图，大尺寸： 2000*2000                   |
| status              | Integer | 状态：1 设计中，2 设计成功，3 设计失败，4 重复设计 |
| fail_msg            | String  | 失败原因                                           |

定制产品主图生成有延迟，如果返回的图片地址显示不了，请实现重试逻辑（建议间隔 2s/4s）。

## 脚本执行示例

```bash
python3 {baseDir}/scripts/humbird_api.py -m GET -p '{
	"api_type": "batch.design.get",
	"batch_design_id": 897725398475926016
}'
```

## 脚本返回示例

**成功响应：**

```json
{
    "code": 200,
    "msg": "Success",
    "result": {
        "result_code": 200,
        "msg": "Success",
        "data": {
            "id": "897725398475926016",
            "qty": 1,
            "success_qty": 1,
            "fail_qty": 0,
            "filter_qty": 0,
            "status": 2,
            "fail_msg": "",
            "det_list": [
                {
                    "id": "897725398962465280",
                    "product_id": "897725398962465281",
                    "status": 2,
                    "fail_msg": null
                }
            ]
        }
    },
    "request_id": "6d3f4acda5e144ec91ab1990652af57c.92.17758059480773027"
}

```

## 异常码

| 异常码 | 异常信息   |
| ------ | ---------- |
| 1004   | 数据不存在 |
| 1000   | 参数非法   |