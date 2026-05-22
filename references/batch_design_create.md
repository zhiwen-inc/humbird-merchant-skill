# 创建批量设计

## 接口说明

调用接口创建批量设计，返回批量设计Id。后续可通过该Id查询批量设计信息。

批量设计成功后，必须告知用户：**可在后台: `创作`→`创作管理`→`定制商品` 中查看结果,并进行后续的发布操作。**

## api_type

```
batch.design.create
```

## 请求方法

POST

## 请求参数

| 参数名           | 类型    | 是否必填 | 说明                     |
| ---------------- | ------- | -------- | ------------------------ |
| is_filter        | Integer | 是       | 是否过滤重复：1 是，0 否 |
| spu_id           | Long    | 是       | 商品id                   |
| default_color_id | Long    | 否       | 指定默认颜色             |
| design_img       | Object  | 否       | 设计图片                 |
| background       | Object  | 否       | 背景图                   |
| background_color | Array   | 否       | 背景色                   |

**设计图片、背景图、背景色必传一个，一次最多生成2000个定制产品**

### 设计图片

| 参数名  | 类型   | 是否必填 | 说明       |
| ------- | ------ | -------- | ---------- |
| ids     | Array  | 是       | 图片id集合 |
| setting | Object | 是       | 图片设置   |

### 背景图

| 参数名  | 类型   | 是否必填 | 说明       |
| ------- | ------ | -------- | ---------- |
| ids     | Array  | 是       | 图片id集合 |
| setting | Object | 是       | 图片设置   |

### 图片设置

| 参数名     | 类型    | 是否必填 | 说明                                       |
| ---------- | ------- | -------- | ------------------------------------------ |
| scale_type | Integer | 是       | 放大类型：1 最大化，2 铺满，3 适高，4 适宽 |
| flatten    | Object  | 否       | 平铺设置                                   |

### 平铺设置

| 参数名           | 类型    | 是否必填 | 说明                                                     |
| ---------------- | ------- | -------- | -------------------------------------------------------- |
| type             | Integer | 是       | 平铺类型：1 基础平铺，2 镜像平铺，3 横向平铺，4 纵向平铺 |
| lateral_spacing  | Integer | 是       | 横向间距                                                 |
| vertical_spacing | Integer | 是       | 纵向间距                                                 |

## 执行脚本例示

```bash
python3 {baseDir}/scripts/humbird_api.py -m POST -p '{
	"api_type": "batch.design.create",
    "is_filter": 1,
    "spu_id": 881100929036762880,
    "design_img": {
        "ids": [
            886887154972640768
        ],
        "setting": {
            "scale_type": 1
        }
    },
    "background": {
        "ids": [
            886887154972640768
        ],
        "setting": {
            "flatten": {
                "type": 1,
                "lateral_spacing":10,
                "vertical_spacing":10
            }
        }
    },
    "background_color":[
        "rgb(196, 49, 49)","rgb(209, 159, 159)"   
    ]
}'
```

## 脚本返回示例

```json
{
    "code": 200,
    "msg": "Success",
    "result": {
        "result_code": 200,
        "msg": "Success",
        "data": "791172060503119872"
    },
    "request_id": "6ee10fa521bc45d7b14a40d30d3232a9.93.17630158573794337"
}

```

## 脚本返回参数

| 参数名      | 类型    | 说明       |
| ----------- | ------- | ---------- |
| result_code | Integer | 响应状态码 |
| msg         | String  | 响应消息   |
| data        | String  | 订单ID     |

## 异常码

| 异常码 | 异常信息   |
| ------ | ---------- |
| 1004   | 数据不存在 |
| 1000   | 参数非法   |



