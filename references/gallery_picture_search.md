# 图片列表

## 接口说明

搜索图库中的图片，支持多维度筛选条件，返回分页的图片列表。

## api_type

```
gallery.picture.search
```

## 请求方法

POST

## 请求参数

| 参数名           | 类型    | 是否必填 | 说明                                                         |
| ---------------- | ------- | -------- | ------------------------------------------------------------ |
| gallery_ids      | Array   | 否       | 图库ID列表，为空时查询所有可用图库                           |
| category_id      | Long    | 否       | 图片分类ID                                                   |
| lang             | String  | 否       | 语言，影响picture_name、picture_label参数，默认中文（包含：zh、zh_TW、en、th、ja） |
| created_user_ids | Array   | 否       | 创建人/上传人ID列表                                          |
| picture_name     | String  | 否       | 图片名称                                                     |
| picture_label    | String  | 否       | 图片关键词                                                   |
| ids              | Array   | 否       | 图片ID列表，最多200个                                        |
| codes            | Array   | 否       | 图片编码列表，最多200个                                      |
| ai_workflow_ids  | Array   | 否       | 工作流任务ID列表，最多200个                                  |
| source           | Integer | 否       | 图片来源，1:普通; 2:AI                                       |
| drawing_type     | Integer | 否       | 绘图类型 1:图生图 2:文生图 3:擦除 5:替换 6:四方连续图 7:艺术字 12:高清放大 20:提取印花 |
| width_range      | Object  | 否       | 图片宽度范围                                                 |
| height_range     | Object  | 否       | 图片高度范围                                                 |
| created_range    | Object  | 否       | 创建时间范围                                                 |
| file_exts        | Array   | 否       | 图片格式列表                                                 |
| dimension_tags   | Array   | 否       | 维度标签集                                                   |
| sorts            | Array   | 否       | 排序规则                                                     |
| page             | Integer | 否       | 页码，默认1                                                  |
| page_size        | Integer | 否       | 每页数量，默认20                                             |

### width_range/height_range 对象说明

| 参数名 | 类型    | 是否必填 | 说明   |
| ------ | ------- | -------- | ------ |
| from   | Integer | 否       | 最小值 |
| to     | Integer | 否       | 最大值 |

### created_range 对象说明

| 参数名 | 类型   | 是否必填 | 说明                                |
| ------ | ------ | -------- | ----------------------------------- |
| from   | String | 否       | 开始时间，格式：yyyy-MM-dd HH:mm:ss |
| to     | String | 否       | 结束时间，格式：yyyy-MM-dd HH:mm:ss |

### dimension_tags 数组元素说明

| 参数名       | 类型   | 是否必填 | 说明     |
| ------------ | ------ | -------- | -------- |
| dimension_id | Long   | **是**   | 维度ID   |
| tag          | String | **是**   | 标签名称 |

### sorts 数组元素说明

| 参数名    | 类型    | 是否必填 | 说明                                |
| --------- | ------- | -------- | ----------------------------------- |
| sort_by   | String  | **是**   | 排序字段（如：created、modified等） |
| sort_type | Integer | **是**   | 排序类型，1:升序; 2:降序            |

## 脚本执行示例

```json
python3 {baseDir}/scripts/humbird_api.py -m POST -p '{
	"api_type": "gallery.picture.search",
    "gallery_ids": [660],
    "page": 1,
    "page_size": 20,
	"sorts": [
        "sort_by": "created",
        "sort_type": 2
    ]
}'
```

## 脚本执行结果示例

**成功响应：**

```json
{
    "result_code": 200,
    "msg": "成功",
    "data": {
        "total": 5915,
        "page": 1,
        "page_size": 2,
        "list": [
            {
                "id": "906473564184516608",
                "gallery_id": "660",
                "gallery_name": "Snow",
                "category_id": "540288072479152128",
                "file_name": "906387644076857344",
                "file_ext": "jpg",
                "file_url": "https://obs-xxx.com/fat103/protect/2f35e8cca31e45259cba4c2405c39100/d828ae5978244b7c8d854e2eaeabda4e.jpg",
                "width": 375,
                "height": 500,
                "size": "38645.00",
                "created": 1776760870000,
                "modified": 1776760875000,
                "code": "906387644076857344",
                "names": null,
                "keywords": null,
                "created_user_id": "207001"
            },
            {
                "id": "906431082923038720",
                "gallery_id": "660",
                "gallery_name": "Snow",
                "category_id": "540288072479152128",
                "file_name": "I8mketmppsd0ie",
                "file_ext": "jpeg",
                "file_url": "https://obs-xxx.com/fat103/protect/d4105644f8744e42825970637696c398/51122e57fbb048d0a77e38c33a4490c9.jpeg",
                "width": 2096,
                "height": 1414,
                "size": "2673557.00",
                "created": 1776755805000,
                "modified": 1776755809000,
                "code": "I8mketmppsd0ie",
                "names": null,
                "keywords": null,
                "created_user_id": "207001"
            }
        ]
    }
}

```

**失败响应：**

```json
{
    "result_code": 10050006,
    "msg": "数据权限异常",
    "data": null
}

```



## 返回参数

| 参数名    | 类型    | 说明     |
| --------- | ------- | -------- |
| total     | Long    | 总记录数 |
| page      | Integer | 当前页码 |
| page_size | Integer | 每页数量 |
| data      | Array   | 图片列表 |

### data 数组元素说明

| 参数名          | 类型       | 说明                                  |
| --------------- | ---------- | ------------------------------------- |
| id              | Long       | 图片ID                                |
| gallery_id      | Long       | 图库ID                                |
| gallery_name    | String     | 图库名称                              |
| category_id     | Long       | 分类ID                                |
| file_name       | String     | 图片名称（不带后缀）                  |
| file_ext        | String     | 图片后缀                              |
| file_url        | String     | 图片URL                               |
| width           | Integer    | 图片宽度                              |
| height          | Integer    | 图片高度                              |
| size            | BigDecimal | 图片大小（字节）                      |
| created         | String     | 创建时间（格式：yyyy-MM-dd HH:mm:ss） |
| modified        | String     | 更新时间（格式：yyyy-MM-dd HH:mm:ss） |
| code            | String     | 图片编码                              |
| names           | Array      | 多语言图片名称列表                    |
| keywords        | Array      | 多语言图片关键字列表                  |
| created_user_id | Long       | 创建用户ID                            |

### names/keywords 响应元素说明

| 参数名      | 类型   | 说明                                    |
| ----------- | ------ | --------------------------------------- |
| lang        | String | 语言编码（包含：zh、zh_TW、en、th、ja） |
| description | String | 名称/关键字内容                         |

## 异常码

| 异常码   | 异常信息     |
| -------- | ------------ |
| 10050001 | 数据权限错误 |