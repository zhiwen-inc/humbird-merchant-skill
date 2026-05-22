# merchant-skill

## 简介

基于厦门指纹科技(HICUSTOM)的蜂鸟数智平台的公共API接口封装的SKILL，针对POD(Print On Demand)市场提供商品查询,商品详情，图库管理、图片上传、下载，批量创建定制商品等能力


## 如何获取API Key

1. 已经有蜂鸟数智平台商户账号
   - 登入账号，进入控制台
   - 点击右上角的用户名 → 账号管理 → API Keys

2. 还没有账号的
   - 请到 [HICUSTOM](https://www.hicustom.com/?utm_source=AgentSKILL&utm_medium=default&utm_campaign=default&utm_term=default&utm_content=) 进行注册或登录
   - 登录后，点击顶部导航切换全球发货中心，然后点击右上角的用户名 → 账号管理 → API Keys

3. 创建一个新的API Key，并按您所使用的AI Agent的要求设置 API Key


## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

```bash
python3 {baseDir}/scripts/humbird_api.py -m POST -p '{"api_type": "xxx"}'
```

humbird_api.py参数说明

| 参数 | 完整参数 | 说明                                                         |
| ---- | -------- | ------------------------------------------------------------ |
| -m   | --method | 请求方式，值为[POST、GET]，例：POST                          |
| -p   | --params | 请求参数，json格式，例：<br />'{<br/>	"api_type": "spu.selection.spu.list.query",<br/>	"page": 1,<br/>	"page_size": 20<br/>}' |

## 核心能力

### 选品管理

- 商品类目：查询商品类目
- 商品列表：查询商品列表
- 商品详情：获取商品信息

### 图库管理

- 图片列表：搜索图库中的图片，支持多维度筛选条件，返回分页的图片列表。
- 图片详情：根据图片ID查询图片详细信息，返回图片的完整信息。
- 图片上传：上传单张图片到指定图库、分类，返回图片ID和文件路径。
- 原图下载：批量获取图片原图的下载URL，可根据该URL直接下载原图。

### 定制商品

- 创建批量设计：调用接口创建批量设计，返回批量设计Id。后续可通过该Id查询批量设计信息。
- 查询批量设计：根据批量设计id查询批量设计信息。


## 典型使用路径

- 通过大模型生成热卖素材图片
- 搜索平台商品，了解商品详细信息
- 上传图片到图库
- 使用上传的图片，批量设计定制商品
- 到控制台查看定制商品，批量刊登到销售平台店铺
