## 接口说明

查询商品列表

## api_type

```
spu.selection.spu.list.query
```

## 请求方式

POST

## 请求参数

| 参数名称           | 类型      | 是否必须 | 说明                 |
| ------------------ | --------- | -------- | -------------------- |
| page               | integer   | 非必须   | 当前页数             |
| page_size          | integer   | 非必须   | 每页数量             |
| sort               | object[]  | 非必须   | 排序字段             |
| ids                | integer[] | 非必须   | 商品id列表           |
| category_id        | integer   | 非必须   | 分类id               |
| group_id           | integer   | 非必须   | 商品组id             |
| name               | string    | 非必须   | 商品名称             |
| name_filter_type   | integer   | 非必须   | 查询类型 1模糊 2精确 |
| blank_product_code | string    | 非必须   | 空白商品编码         |
| modify_time_filter | object    | 非必须   | 更新时间范围         |
| - from             | string    | 非必须   | 起始时间             |
| - to               | string    | 非必须   | 终止时间             |

Sort

| 参数名称  | 类型   | 是否必须 | 说明                                                    |
| --------- | ------ | -------- | ------------------------------------------------------- |
| sort_by   | string | 非必须   | 排序字段，当前支持position：排序值，sale_time：上新时间 |
| sort_type | string | 非必须   | 排序方法：1：ASC 2：DESC                                |

## 返回参数

| 参数名称        | 类型    | 是否必须 | 说明                          |
| --------------- | ------- | -------- | ----------------------------- |
| id              | integer | 非必须   | 商品id                        |
| name            | string  | 非必须   | 商品名称                      |
| detail          | integer | 非必须   | 商品详情                      |
| sale_time       | string  | 非必须   | 上新时间                      |
| position        | integer | 非必须   | 排序值                        |
| category_id     | integer | 非必须   | 分类id                        |
| category_name   | string  | 非必须   | 分类名称                      |
| delivery_period | integer | 非必须   | 处理时效，单位:小时           |
| urgent_period   | integer | 非必须   | 加速时效，单位:小时           |
| urgent_status   | integer | 非必须   | 是否支持加速 1:支持 -1:不支持 |
| view_price      | number  | 非必须   | 设计面价格,精确到小数点后2位  |
| currency_id     | integer | 非必须   | 币别id                        |
| group_id        | integer | 非必须   | 商品组id                      |
| image           | object  | 非必须   | 效果图                        |

Image

| 参数名称  | 类型   | 是否必须 | 说明             |
| --------- | ------ | -------- | ---------------- |
| file_path | string | 非必须   | 图片文件相对路径 |

## 执行脚本例示

```bash
python3 {baseDir}/scripts/humbird_api.py -m POST -p '{
	"api_type": "spu.selection.spu.list.query",
	"page": 1,
	"page_size": 20
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
            "total": 158,
            "page": 1,
            "page_size": 10,
            "list": [
                {
                    "id": "753649807867841664",
                    "name": "无框画30*40-7.28HIC上架选品池无敌犀牛",
                    "category_id": "722905604888236569",
                    "category_name": "箱包皮具>便当包>手提便当包",
                    "min_price": "29.31",
                    "max_price": "33.18",
                    "sale_time": "2025-09-22 20:07:47",
                    "position": 0,
                    "delivery_period": 48,
                    "urgent_period": 24,
                    "urgent_status": 1,
                    "view_price": "0.00",
                    "currency_id": 1,
                    "app_id": 2483993,
                    "image": {
                        "file_path": "lpt104/protect/effect_image/head/753649805686770816/0d34c95e0e9797be70db101a4dae3e88/545553409000914688/color/100001.jpeg"
                    },
                    "group_id": null
                },
                {
                    "id": "723809775019658368",
                    "name": "bmw330li-level2",
                    "category_id": "688312364868585346",
                    "category_name": "测试分类",
                    "min_price": "12.00",
                    "max_price": "12.00",
                    "sale_time": "2025-09-04 18:02:13",
                    "position": 0,
                    "delivery_period": 39,
                    "urgent_period": 39,
                    "urgent_status": -1,
                    "view_price": "0.00",
                    "currency_id": 1,
                    "app_id": 2483993,
                    "image": {
                        "file_path": "lpt104/protect/effect_image/head/723809526565899392/d751713988987e9331980363e24189ce/723058903721545344/color/100011.jpeg"
                    },
                    "group_id": null
                },
                {
                    "id": "740444047973354624",
                    "name": "男款双面短袖T恤",
                    "category_id": "604",
                    "category_name": "男装>男士T恤>男式短袖T恤",
                    "min_price": "25.81",
                    "max_price": "29.21",
                    "sale_time": "2025-09-04 15:19:47",
                    "position": 0,
                    "delivery_period": 1,
                    "urgent_period": 12,
                    "urgent_status": 1,
                    "view_price": "5.00",
                    "currency_id": 1,
                    "app_id": 2483993,
                    "image": {
                        "file_path": "lpt104/protect/effect_image/head/740444046169803904/d751713988987e9331980363e24189ce/737518330956516992/color/100001.jpeg"
                    },
                    "group_id": null
                },
                {
                    "id": "739006530069793920",
                    "name": "190g针织拼色印花套装-wu",
                    "category_id": "568573218651179267",
                    "category_name": "男装>上衣>衬衫",
                    "min_price": "23.46",
                    "max_price": "26.56",
                    "sale_time": "2025-09-02 15:14:57",
                    "position": 0,
                    "delivery_period": 20,
                    "urgent_period": 20,
                    "urgent_status": -1,
                    "view_price": "0.00",
                    "currency_id": 1,
                    "app_id": 2483993,
                    "image": {
                        "file_path": "lpt104/protect/effect_image/head/739006529155435648/62ffc255bcbe5ab4f6757f99de752a5e/738237449846689408/color/100000.jpeg"
                    },
                    "group_id": null
                },
                {
                    "id": "730391711670373504",
                    "name": "小腿压力袜（按尺码建模）",
                    "category_id": "568573218651179267",
                    "category_name": "男装>上衣>衬衫",
                    "min_price": "99.00",
                    "max_price": "550.00",
                    "sale_time": "2025-08-21 17:58:09",
                    "position": 0,
                    "delivery_period": 89,
                    "urgent_period": 89,
                    "urgent_status": -1,
                    "view_price": "0.00",
                    "currency_id": 1,
                    "app_id": 2483993,
                    "image": {
                        "file_path": "lpt104/protect/effect_image/head/730391711024417920/d751713988987e9331980363e24189ce/593889792857475328/516538516679690496/100001.jpeg"
                    },
                    "group_id": null
                },
                {
                    "id": "730351600442346624",
                    "name": "小腿压力袜（3D打印）-R建",
                    "category_id": "652877396185255040",
                    "category_name": "未设置费率分类",
                    "min_price": "111.36",
                    "max_price": "126.06",
                    "sale_time": "2025-08-21 16:38:25",
                    "position": 0,
                    "delivery_period": 481,
                    "urgent_period": 24,
                    "urgent_status": 1,
                    "view_price": "0.00",
                    "currency_id": 1,
                    "app_id": 2483993,
                    "image": {
                        "file_path": "lpt104/protect/effect_image/head/730351599553088640/d751713988987e9331980363e24189ce/728693379772190336/567824830154477184/100001.jpeg"
                    },
                    "group_id": null
                },
                {
                    "id": "728925342550461568",
                    "name": "小腿压力袜（3D打印）-自建",
                    "category_id": "688312364868585346",
                    "category_name": "测试分类",
                    "min_price": "2.00",
                    "max_price": "12.00",
                    "sale_time": "2025-08-19 17:23:52",
                    "position": 0,
                    "delivery_period": 12,
                    "urgent_period": 12,
                    "urgent_status": -1,
                    "view_price": "0.00",
                    "currency_id": 1,
                    "app_id": 2483993,
                    "image": {
                        "file_path": "lpt104/protect/effect_image/head/728924997216668800/d751713988987e9331980363e24189ce/728693379772190336/567824830154477184/100001.jpeg"
                    },
                    "group_id": null
                },
                {
                    "id": "723159322699271296",
                    "name": "bmw330li-问题定位勿动",
                    "category_id": "688312364868585346",
                    "category_name": "测试分类",
                    "min_price": "1.00",
                    "max_price": "1.00",
                    "sale_time": "2025-08-11 18:28:01",
                    "position": 0,
                    "delivery_period": 12,
                    "urgent_period": 12,
                    "urgent_status": -1,
                    "view_price": "0.00",
                    "currency_id": 1,
                    "app_id": 2483993,
                    "image": {
                        "file_path": null
                    },
                    "group_id": null
                },
                {
                    "id": "723153392809053312",
                    "name": "A20250811-1-384new",
                    "category_id": "652877396185255040",
                    "category_name": "未设置费率分类",
                    "min_price": "33.99",
                    "max_price": "38.48",
                    "sale_time": "2025-08-11 18:16:52",
                    "position": 0,
                    "delivery_period": 1,
                    "urgent_period": 1,
                    "urgent_status": -1,
                    "view_price": "0.00",
                    "currency_id": 1,
                    "app_id": 2483993,
                    "image": {
                        "file_path": "lpt104/protect/effect_image/head/723153391961836672/d751713988987e9331980363e24189ce/722896958481534592/color/100001.jpeg"
                    },
                    "group_id": null
                },
                {
                    "id": "723131457756761216",
                    "name": "bmw330li",
                    "category_id": "688312364868585346",
                    "category_name": "测试分类",
                    "min_price": "12.00",
                    "max_price": "12.00",
                    "sale_time": "2025-08-11 17:32:25",
                    "position": 0,
                    "delivery_period": 12,
                    "urgent_period": 12,
                    "urgent_status": -1,
                    "view_price": "0.00",
                    "currency_id": 1,
                    "app_id": 2483993,
                    "image": {
                        "file_path": null
                    },
                    "group_id": null
                }
            ]
        }
    },
    "request_id": "7278dd74ce2d4643bb768a590847e8bd.92.17585962830902587"
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