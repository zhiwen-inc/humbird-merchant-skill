---
name: humbird-merchant-skill
display_name: "Humbird POD assistant - Product Selection, Image Library & Batch Design Products"
version: 1.0.0
author: hicustom.com
description: 基于厦门指纹科技(HICUSTOM)的蜂鸟数智平台(wwww.hihumbird.com)的公共API接口封装的SKILL，提供商品查询,商品详情，图库管理,图片上传、下载，创建定制商品等能力
homepage: https://www.hicustom.com/?utm_source=AgentSKILL&utm_medium=default&utm_campaign=default&utm_term=default&utm_content=
capabilities: ["POD (Print On Demain) Design"]
keywords:
  - 蜂鸟
  - 选品
  - 定制
  - humbird
metadata:
  version: 0.8.0
  openclaw:
    primaryEnv: HUMBIRD_API_KEY
    requiredMcp:
      - humbird-mcp-server
    requiresNetwork: true
---

# 蜂鸟POD助手 - POD: Product Selection, Image Library & Batch Design Products

本技能通过厦门指纹科技(HICUSTOM)的蜂鸟数智平台的公共API接口来进行选品、图库管理、定制商品等操作。


## 前置条件

### 如何获取API Key

1. 已经有蜂鸟数智平台商户账号
   - 登入账号，进入控制台
   - 点击右上角的用户名 → 账号管理 → API Keys 

2. 还没有账号的
   - 请到 [HICUSTOM](https://www.hicustom.com/?utm_source=AgentSKILL&utm_medium=default&utm_campaign=default&utm_term=default&utm_content=) 进行注册或登录
   - 登录后，点击顶部导航切换全球发货中心，然后点击右上角的用户名 → 账号管理 → API Keys

3. 创建一个新的API Key，并按您所使用的AI Agent的要求设置 API Key



### 安装MCP Server

**必需 MCP Server**: `humbird-mcp-server`

优先使用名为 `humbird-mcp-server` 的 MCP server。

**MCP 配置**:
以下的MCP Server的声明，需要根据不同的 AI Agent的要求进行配置，读取HUMBIRD_API_KEY，发起MCP请求

```json
{
  "mcpServers": {
    "humbird-mcp-server": {
      "transport": "streamable-http",
      "url": "https://mcp-server.hihumbird.com/mcp",
      "headers": {
        "x-api-key": "${HUMBIRD_API_KEY}"
      }
    }
  }
}
```

**安全说明**:

- `HUMBIRD_API_KEY` MCP Client通常应该读取环境变量 `HUMBIRD_API_KEY`, 如果无法正确读取，请查询所使用的Agent的读取规则进行设置



## 脚本执行例示

```bash
python3 {baseDir}/scripts/humbird_api.py -m POST -p '{"api_type": "xxx"}'
```

humbird_api.py参数说明

| 参数 | 完整参数 | 说明                                                         |
| ---- | -------- | ------------------------------------------------------------ |
| -m   | --method | 请求方式，值为[POST、GET]，例：POST                          |
| -p   | --params | 请求参数，json格式，例：<br />'{<br/>	"api_type": "gallery.picture.upload",<br/>	"gallery_id": 660,<br/>	"category_id": 20<br/>}' |



## References

详细API文档存在**`references/`**里（一个文件一个API）：

| 类型     | Doc                                    |
| -------- | -------------------------------------- |
| 图片上传 | `references/gallery_picture_upload.md` |





## 执行优先级

以下为强约束，优先级高于其余章节；如有重复描述，以本节为准：

1. **能力约束**：mcp tool有的能力优先使用（除了图片上传外），只有在mcp tool调用失败后，才使用`humbird_api.py`
2. **脚本约束**：不可自己生成脚本，只能使用`humbird_api.py`



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
- 到控制台 `创作`→`创作管理`→`定制商品` 查看定制商品
- 批量刊登到销售平台店铺



## 友好的展示要求

- **通用原则**：输出内容必须为有效的 `markdown` 格式，并采用富文本 + 图片的呈现方式。
- **图片展示**：输出 `![{picTitle}]({picUrl})`，其中 `{picTitle}` 和 `{picUrl}` 来自返回数据，若picTitle则取名称。
- **id展示**：数据有id字段优先展示出来

