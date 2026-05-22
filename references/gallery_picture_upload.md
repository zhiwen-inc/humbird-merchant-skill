# 图片上传

## 接口说明

上传单张图片到指定图库、分类，返回图片ID和文件路径。

上传图片成功后，必须告知用户：**可在后台: `AI工作流`→`图片素材`→`我的图库` 中查看。或者通过图片详情、图片列表API查看**

## api_type

```
gallery.picture.upload
```

## 请求方法

POST

## 请求参数

| 参数名      | 类型   | 是否必填 | 说明                                                         |
| ----------- | ------ | -------- | ------------------------------------------------------------ |
| gallery_id  | Long   | 否       | 图库Id,未指定则上传到默认图库                                |
| category_id | Long   | 否       | 图片分类Id                                                   |
| code        | String | 否       | 图片编码，最多300个字符                                      |
| names       | Array  | 否       | 多语言图片名称列表，最多100个                                |
| keywords    | Array  | 否       | 多语言图片关键字列表                                         |
| image_path  | String | **是**   | 图片文件路径，可以是本地图片路径，也可以是网络图片地址，图片最大不超25M，总像数不超2.5亿 |
| image_name  | String | **是**   | 原始文件名（包含扩展名）                                     |

### names/keywords 数组元素说明

| 参数名      | 类型   | 是否必填 | 说明                                    |
| ----------- | ------ | -------- | --------------------------------------- |
| lang        | String | **是**   | 语言编码（包含：zh、zh_TW、en、th、ja） |
| description | String | **是**   | 名称/关键字内容                         |

## 响应参数

| 参数名       | 类型       | 说明                                  |
| ------------ | ---------- | ------------------------------------- |
| picture_id   | Long       | 图片ID                                |
| gallery_id   | Long       | 图库ID                                |
| gallery_name | String     | 图库名称                              |
| category_id  | Long       | 分类ID                                |
| file_name    | String     | 图片名称（不带后缀）                  |
| file_ext     | String     | 图片后缀                              |
| file_url     | String     | 图片URL                               |
| width        | Integer    | 图片宽度                              |
| height       | Integer    | 图片高度                              |
| size         | BigDecimal | 图片大小（字节）                      |
| created      | String     | 创建时间（格式：yyyy-MM-dd HH:mm:ss） |
| modified     | String     | 更新时间（格式：yyyy-MM-dd HH:mm:ss） |
| code         | String     | 图片编码                              |
| names        | Array      | 多语言图片名称列表                    |
| keywords     | Array      | 多语言图片关键字列表                  |

### names/keywords 响应元素说明

| 参数名      | 类型   | 说明                                    |
| ----------- | ------ | --------------------------------------- |
| lang        | String | 语言编码（包含：zh、zh_TW、en、th、ja） |
| description | String | 名称/关键字内容                         |

## 执行脚本例示

```bash
python3 {baseDir}/scripts/humbird_api.py -m POST -p '{
  "api_type": "gallery.picture.upload",
  "gallery_id": 660,
  "category_id": 540288072479152128,
  "code": "PIC_001",
  "image_path": "D:\\img\\example.png",
  "image_name": "example.png",
  "names": [
    {
      "lang": "zh",
      "description": "示例图片"
    },
    {
      "lang": "en",
      "description": "Example Image"
    }
  ],
  "keywords": [
    {
      "lang": "zh",
      "description": "风景,自然"
    }
  ]
}'
```



## 脚本返回示例

**成功响应：**

```json
{
  "result_code": 200,
  "msg": "成功",
  "data": {
    "picture_id": "897837427337467904",
    "file_url": "https://obs-fat103.zhiwendiy.com/fat103/protect/20260409/6dd56e6e358942.png?x-image-process=style/s500",
    "gallery_id ": 123,
    "gallery_name": "默认图库",
    "category_id": 456,
    "file_name": "example",
    "file_ext": "png",
    "width": 1920,
    "height": 1080,
    "size": 524288,
    "created": "2026-04-09 10:30:00",
    "modified": "2026-04-09 10:30:00",
    "code": "PIC_001",
    "names": [
      {
        "lang": "zh",
        "description": "示例图片"
      },
      {
        "lang": "en",
        "description": "Example Image"
      }
    ],
    "keywords": [
      {
        "lang": "zh",
        "description": "风景,自然"
      }
    ]
  }
}

```

**失败响应：**

```json
{
    "result_code": 1000,
    "msg": "请求参数非法: [imageData], 图片文件数据不能为空!",
    "data": null
}

```

## 异常码

| 异常码   | 异常信息                              |
| -------- | ------------------------------------- |
| 10050073 | 图片上传失败                          |
| 10050074 | 图片文件大小超过限制，最大支持25MB    |
| 10050075 | 图片总像素超过限制，最大支持2.5亿像素 |





