# 商品类目

## 接口说明

查询商品类目

## api_type

```
spu.selection.category.tree
```

## 请求方式

- POST

## 请求参数

```json
{"api_type": "spu.selection.category.tree"}
```



## 返回参数

- data

| 参数名称  | 类型    | 是否必须 | 说明                                |
| --------- | ------- | -------- | ----------------------------------- |
| id        | integer | 非必须   | 分类id                              |
| name      | string  | 非必须   | 分类名称                            |
| parent_id | integer | 非必须   | 父分类id，如果当前是根分类，该值为0 |
| position  | integer | 非必须   | 排序值                              |
| children  | []      | 非必须   | 子分类信息                          |



## 执行脚本例示

```bash
python3 {baseDir}/scripts/humbird_api.py -m POST -p "{\"api_type\": \"spu.selection.category.tree\"}"
```



## 脚本返回示例

```Bash
{
    "code": 200,
    "msg": "Success",
    "result": {
        "result_code": 200,
        "msg": "成功",
        "data": [
            {
                "id": "443",
                "name": "男装",
                "parent_id": "0",
                "position": 444,
                "children": [
                    {
                        "id": "90809321809321",
                        "name": "上衣",
                        "parent_id": "443",
                        "position": 444,
                        "children": [
                            {
                                "id": "90809321809323",
                                "name": "衬衫",
                                "parent_id": "90809321809321",
                                "position": 444,
                                "children": []
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "request_id": "7278dd74ce2d4643bb768a590847e8bd.92.17585338669400235"
}
```