# 图片详情

## 接口说明

根据图片ID查询图片详细信息，返回图片的完整信息。

## api_type

```
gallery.picture.detail
```

## 请求方法

GET

## 请求参数

| 参数名 | 类型 | 是否必填 | 说明   |
| ------ | ---- | -------- | ------ |
| id     | Long | **是**   | 图片ID |

## 执行脚本例示

```bash
python3 {baseDir}/scripts/humbird_api.py -m POST -p '{
	"api_type": "gallery.picture.detail",
	"id": 111
}'
```



## 响应参数

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

### names/keywords 数组元素说明

| 参数名      | 类型   | 说明                                    |
| ----------- | ------ | --------------------------------------- |
| lang        | String | 语言编码（包含：zh、zh_TW、en、th、ja） |
| description | String | 名称/关键字内容                         |

## 脚本返回示例

**成功响应：**

```json
{
    "result_code": 200,
    "msg": "成功",
    "data": {
        "id": "906473564184516608",
        "gallery_id": "660",
        "gallery_name": "Snow",
        "category_id": "540288072479152128",
        "file_name": "906387644076857344",
        "file_ext": "jpg",
        "file_url": "https://obs-xxx.com/fat103/protect/2f35e8cca31e45259cba4c2405c39100/d828ae5978244b7c8d854e2eaeabda4e.jpg?x-image-process=style/s500",
        "width": 375,
        "height": 500,
        "size": "38645.0",
        "created": 1776758650000,
        "modified": 1776758655000,
        "code": "906387644076857344",
        "names": [
            {
                "lang": "zh",
                "description": "906387644076857344"
            },
            {
                "lang": "zh_TW",
                "description": "906387644076857344"
            },
            {
                "lang": "en",
                "description": "906387644076857344"
            },
            {
                "lang": "th",
                "description": null
            },
            {
                "lang": "ja",
                "description": null
            }
        ],
        "keywords": [
            {
                "lang": "zh",
                "description": null
            },
            {
                "lang": "zh_TW",
                "description": null
            },
            {
                "lang": "en",
                "description": null
            },
            {
                "lang": "th",
                "description": null
            },
            {
                "lang": "ja",
                "description": null
            }
        ],
        "created_user_id": null
    }
}

```

**失败响应：**

```json
{
  "result_code": 10050032,
  "msg": "图片不存在",
  "data": null
}

{
  "result_code": 10050006,
  "msg": "数据权限异常",
  "data": null
}

```

## 异常码

| 异常码   | 异常信息     |
| -------- | ------------ |
| 10050032 | 图片不存在   |
| 10050006 | 数据权限异常 |