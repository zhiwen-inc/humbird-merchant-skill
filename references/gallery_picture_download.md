## 接口说明

批量获取图片原图的下载URL，可根据该URL直接下载原图。

## api_type

```
gallery.picture.download
```

## 请求方法

POST

## 请求参数

| 参数名 | 类型       | 是否必填 | 说明                           |
| ------ | ---------- | -------- | ------------------------------ |
| ids    | List<Long> | **是**   | 图片ID列表，最少1个，最多200个 |

## 执行脚本例示

```bash
python3 {baseDir}/scripts/humbird_api.py -m POST -p '{
	"api_type": "gallery.picture.download",
	"ids": [897837427337467904, 897837427337467905]
}'
```



## 响应参数

该接口返回JSON格式数据，`data`为图片原图URL信息数组：

| 参数名       | 类型   | 说明        |
| ------------ | ------ | ----------- |
| id           | Long   | 图片ID      |
| original_url | String | 图片原图URL |

## 脚本返回示例

**成功响应：**

```json
{
    "result_code": 200,
    "msg": "成功",
    "data": [
        {
            "id": "906473564184516608",
            "original_url": "http://obs-xxx.com/fat103/protect/2f35e8cca31e45259cba4c2405c39100/d828ae5978244b7c8d854e2eaeabda4e.jpg?AccessKeyId=84N9WxxxxMIUZMW1CDSG&Expires=1777020706&Signature=Hn6kh1adVhupIRKjidcxJ7q6WbI%3D"
        },
        {
            "id": "906431082923038720",
            "original_url": "http://obs-xxx.com/fat103/protect/d4105644f8744e42825970637696c398/51122e57fbb048d0a77e38c33a4490c9.jpeg?AccessKeyId=84N9WMCGxxxUZMW1CDSG&Expires=1777020706&Signature=%2F6J0rnsa45cR1%2FihtnrH68yf5ls%3D"
        }
    ]
}


```

**失败响应（图片不存在）：**

```json
{
  "result_code": 10050032,
  "message": "图片不存在",
  "data": null
}

```

## 异常码

| 异常码   | 异常信息        |
| -------- | --------------- |
| 1000     | 请求参数非法    |
| 10050032 | 图片不存在      |
| 10050006 | 数据权限异常    |
| 10050076 | 原图url获取失败 |