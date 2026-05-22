# 商品详情

## 接口说明

获取商品信息

## api_type

```
spu.selection.spu.get
```

## 请求方法

GET

## 请求参数

| 参数名称        | 类型    | 是否必须 | 说明        |
| --------------- | ------- | -------- | ----------- |
| id              | integer | 必须     | 商品id      |
| accept_sku_info | boolean | 非必须   | 返回sku信息 |

## 返回参数

| 参数名称        | 类型      | 是否必须 | 说明                          |
| --------------- | --------- | -------- | ----------------------------- |
| id              | integer   | 非必须   | 商品id                        |
| name            | string    | 非必须   | 商品名称                      |
| detail          | integer   | 非必须   | 商品详情                      |
| sale_time       | string    | 非必须   | 上新时间                      |
| position        | integer   | 非必须   | 排序值                        |
| category_id     | integer   | 非必须   | 分类id                        |
| category_name   | string    | 非必须   | 分类名称                      |
| delivery_period | integer   | 非必须   | 处理时效，单位:小时           |
| urgent_period   | integer   | 非必须   | 加速时效，单位:小时           |
| urgent_status   | integer   | 非必须   | 是否支持加速 1:支持 -1:不支持 |
| view_price      | number    | 非必须   | 设计面价格,精确到小数点后2位  |
| currency_id     | integer   | 非必须   | 币别id                        |
| group_id        | integer   | 非必须   | 商品组id                      |
| skus            | object [] | 非必须   | SKU列表                       |
| attribute_items | object [] | 非必须   | 商品属性项列表                |
| images          | object [] | 非必须   | 效果图列表                    |

SKU

| 参数名称           | 类型      | 是否必须 | 说明        |
| ------------------ | --------- | -------- | ----------- |
| id                 | integer   | 非必须   | skuId       |
| sales_price        | number    | 非必须   | 销售价格    |
| attribute_items    | object [] | 非必须   | 属性列表    |
| sku_price_template | object    | 非必须   | sku价格模板 |

AttributeItem

| 参数名称     | 类型    | 是否必须 | 说明                  |
| ------------ | ------- | -------- | --------------------- |
| id           | integer | 非必须   | ID                    |
| name         | string  | 非必须   | 属性项名称            |
| value        | string  | 非必须   | 属性值                |
| reference_id | integer | 非必须   | 关联的属性id          |
| type         | integer | 非必须   | 类型：1：颜色 2：尺码 |

SkuPriceTemplate

| 参数名称            | 类型     | 是否必须 | 说明         |
| ------------------- | -------- | -------- | ------------ |
| currency_id         | integer  | 非必须   | 币别id       |
| price_level_factors | object[] | 非必须   | 价格等级因子 |

PriceLevelFactor

| 参数名称          | 类型    | 是否必须 | 说明                   |
| ----------------- | ------- | -------- | ---------------------- |
| id                | integer | 非必须   | 价格等级ID, 编辑需要传 |
| name              | string  | 必须     | 价格等级名称           |
| min_num           | integer | 非必须   | 最小值                 |
| max_num           | integer | 非必须   | 最大值                 |
| member_level_id   | integer | 非必须   | 会员等级               |
| member_level_name | string  | 非必须   | 会员等级名称           |
| calculate_value   | number  | 非必须   | 计算值                 |

Image

| 参数名称  | 类型    | 是否必须 | 说明             |
| --------- | ------- | -------- | ---------------- |
| color_id  | integer | 非必须   | 颜色id           |
| size_id   | integer | 非必须   | 尺码id           |
| file_path | string  | 非必须   | 图片文件相对路径 |

## 脚本请求示例

```Bash
python3 {baseDir}/scripts/humbird_api.py -m GET -p '{
	"api_type": "spu.selection.spu.get",
	"id": 753649807867841664,
	"accept_sku_info": false
}'
```

## 脚本返回示例

```Bash
{
    "code": 200,
    "msg": "Success",
    "result": {
        "result_code": 200,
        "msg": "成功",
        "data": {
            "id": "753649807867841664",
            "name": "无框画30*40-7.28HIC上架选品池无敌犀牛",
            "detail": "<p>无框画无敌犀牛</p>",
            "sale_time": "2025-09-22 20:07:47",
            "position": 0,
            "category_id": "722905604888236569",
            "category_name": "箱包皮具>便当包>手提便当包",
            "delivery_period": 48,
            "urgent_period": 24,
            "urgent_status": 1,
            "app_id": 2483993,
            "view_price": "0.00",
            "currency_id": 1,
            "group_id": null,
            "skus": [
                {
                    "id": "753649807943339136",
                    "sales_price": null,
                    "attribute_items": [
                        {
                            "id": "2",
                            "name": "白色",
                            "value": "{\"tone\":\"#FFFFFF\"}",
                            "reference_id": "100001",
                            "type": 1
                        },
                        {
                            "id": "32",
                            "name": "One Size",
                            "value": "",
                            "reference_id": "120015",
                            "type": 2
                        }
                    ],
                    "sku_price_template": {
                        "currency_id": 1,
                        "price_level_factors": [
                            {
                                "id": "85",
                                "name": "C",
                                "min_num": 1,
                                "max_num": 10,
                                "member_level_id": "0",
                                "member_level_name": "普通",
                                "calculate_value": "38.16"
                            },
                            {
                                "id": "86",
                                "name": "V1",
                                "min_num": 11,
                                "max_num": 20,
                                "member_level_id": "101693",
                                "member_level_name": "黄金",
                                "calculate_value": "36.57"
                            },
                            {
                                "id": "87",
                                "name": "V2",
                                "min_num": 21,
                                "max_num": 30,
                                "member_level_id": "101694",
                                "member_level_name": "铂金",
                                "calculate_value": "35.62"
                            },
                            {
                                "id": "88",
                                "name": "V3",
                                "min_num": 31,
                                "max_num": 40,
                                "member_level_id": "101695",
                                "member_level_name": "钻石",
                                "calculate_value": "34.36"
                            },
                            {
                                "id": "89",
                                "name": "V4",
                                "min_num": 41,
                                "max_num": 50,
                                "member_level_id": "101696",
                                "member_level_name": "星耀",
                                "calculate_value": "34.03"
                            },
                            {
                                "id": "90",
                                "name": "V5",
                                "min_num": 51,
                                "max_num": null,
                                "member_level_id": null,
                                "member_level_name": null,
                                "calculate_value": "33.71"
                            }
                        ]
                    }
                }
            ],
            "attribute_items": [
                {
                    "id": "2",
                    "name": "白色",
                    "value": "{\"tone\":\"#FFFFFF\"}",
                    "reference_id": "100001",
                    "type": 1
                },
                {
                    "id": "32",
                    "name": "One Size",
                    "value": "",
                    "reference_id": "120015",
                    "type": 2
                }
            ],
            "images": [
                {
                    "color_id": "100001",
                    "size_id": "120015",
                    "file_path": "lpt104/protect/effect_image/head/753649805686770816/0d34c95e0e9797be70db101a4dae3e88/545553409000914688/color/100001.jpeg"
                }
            ]
        }
    },
    "request_id": "7278dd74ce2d4643bb768a590847e8bd.97.17585970292933067"
}

```

## 币别说明

| 币别ID | 币别编码 | 币别编码 |
| ------ | -------- | -------- |
| 1      | 人民币   | CNY      |
| 2      | 美元     | USD      |
| 3      | 英镑     | GBP      |
| 4      | 加元     | CAD      |
| 5      | 日元     | JPY      |
| 6      | 欧元     | EUR      |