# introTemplate 项目文档

> 适用场景：demo游戏、创意产品、中小型项目的简介页面（公司简介也可）

## 简介

基于 Jinja2 模板引擎 + JSON 配置实现的可动态配置项目介绍页面模板。

**优点：**
- 轻量级，只需修改 JSON 即可生成多套页面
- 响应式布局，适配移动端和 PC 端
- 支持在线编辑配置
- 含运维界面扩展能力

---

## 目录结构

```
introTemplate/
├── index.html              # 首页（主入口，根目录保留）
├── static/                 # 静态页面目录（除首页外的输出）
│   ├── chess.html          # 五子棋页面
│   ├── chessLog.html       # 五子棋更新日志
│   ├── library.html        # 图书管理系统页面
│   └── log.html            # 主项目更新日志
├── template/               # HTML 模板目录
│   ├── index.html          # 主页面模板
│   ├── log.html            # 日志页面模板
│   ├── AndroidDownload.html
│   ├── CountPlayer.html
│   ├── donate.html
│   ├── LICENSE.html
│   └── PCDownload.html
├── json/                   # JSON 配置目录
│   ├── index.json          # 首页配置
│   ├── chess.json          # 五子棋页面配置
│   ├── library.json        # 图书管理系统配置
│   ├── log.json            # 主日志配置
│   └── chessLog.json       # 五子棋日志配置
├── assets/                 # 静态资源
│   ├── css/                # 样式文件
│   └── images/             # 图片/视频资源
├── config.json             # 渲染配置（指定模板、数据源、输出路径）
├── render.py               # 渲染脚本
└── readme.md               # 本文档
```

---

## 快速开始

### 1. 环境准备

确保已安装 Python 和 Jinja2：

```bash
pip install jinja2
```

### 2. 编辑配置

1. 在 `json/` 目录下编辑或创建 JSON 配置文件
2. 在 `config.json` 中添加渲染条目（详见下文）
3. 运行渲染脚本

### 3. 运行渲染

```bash
python render.py
```

脚本会读取 `config.json` 中的所有配置，批量渲染生成 HTML 文件。

---

## config.json 配置说明

`config.json` 是渲染入口配置，定义了需要渲染的所有页面。格式为数组，每个元素包含三个字段：

| 字段 | 说明 | 示例 |
|------|------|------|
| `useTemplate` | 使用的模板文件路径 | `"template/index.html"` |
| `useSource` | 使用的 JSON 数据源路径 | `"json/index.json"` |
| `outputSource` | 输出的 HTML 文件路径 | `"index.html"` 或 `"static/xxx.html"` |

**示例：**
```json
[
  {
    "useTemplate": "template/index.html",
    "useSource": "json/index.json",
    "outputSource": "index.html"
  },
  {
    "useTemplate": "template/log.html",
    "useSource": "json/log.json",
    "outputSource": "static/log.html"
  }
]
```

> **注意：** JSON 文件名不要带后缀！路径相对于项目根目录。

---

## 模板类型

目前提供两种模板：

### 1. index.html（主页面模板）

包含完整的导航栏、简介、项目说明、图片展示、Q&A、页脚等模块。

### 2. log.html（日志页面模板）

简洁的更新日志页面，按时间倒序展示版本更新内容。

---

## index.json 配置详解（主页面模板）

以下是主页面模板 `template/index.html` 对应的所有可配置参数。

### 全局配置

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `websiteTitle` | string | 是 | 网站标题（显示在浏览器标签） |
| `websiteIco` | string | 是 | 网站图标路径 |
| `assetsPath` | string | 否 | 资源路径前缀。**根目录页面留空或不填，static 目录下页面填 `"../"`** |

### header（导航栏）

- **类型：** 数组
- **数量限制：** 无硬性限制，建议 3-6 个（过多会挤压导航栏）
- **每个元素字段：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `text` | string | 是 | 导航文字 |
| `href` | string | 是 | 跳转链接 |
| `target` | string | 否 | 打开方式，如 `"_blank"` 新窗口打开 |
| `style` | string | 否 | 自定义内联样式，如 `"color:red"` |
| `extraClass` | string | 否 | 额外 CSS 类名，如 `"font-weight-bold"` |

**示例：**
```json
"header": [
  {
    "text": "首页",
    "href": "index.html",
    "target": "",
    "style": "",
    "extraClass": "font-weight-bold"
  }
]
```

### intro（简介区域）

- **类型：** 对象
- **字段：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `title` | string | 是 | 主标题，支持 HTML 标签（如 `<br>`） |
| `subTitle` | string | 是 | 副标题 |
| `text` | string | 是 | 介绍文字，支持 HTML |
| `image` | string | 是 | 右侧展示图片路径 |
| `btn` | array | 是 | 按钮数组，建议 2-3 个 |

**intro.btn 每个元素：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ico` | string | 是 | 按钮图标图片路径 |
| `text` | string | 是 | 按钮文字 |
| `href` | string | 是 | 按钮跳转链接 |

> **图片支持：** `intro.image` 和 `intro.btn[].ico` 都支持图片。

### desc（项目说明）

- **类型：** 对象
- **字段：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `title` | string | 是 | 区域标题 |
| `content` | array | 是 | 说明内容数组，**最多 3 个**（3 列布局，超过会换行） |

> **限制：** `desc.content` 建议 3 个，文字长度尽量相近，否则布局不美观。
> 每个元素支持 HTML 标签（如 `<a>`、`<ul>`、`<li>`、`<br>` 等）。

### exDesc（额外说明 / 最低配置）

- **类型：** 对象
- **字段：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `disable` | boolean | 是 | 是否禁用该模块，`true` 为隐藏，`false` 为显示 |
| `title` | string | 是 | 区域标题 |
| `content` | array | 否 | 预留字段，当前模板中未使用（内容写死在模板里） |

> **注意：** 此模块的具体内容（三列配置信息）目前硬编码在模板中，如需修改需编辑 `template/index.html`。

### displaySession（图片/视频展示区）

- **类型：** 对象
- **字段：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `title` | string | 是 | 区域标题 |
| `imageList` | array | 是 | 展示项数组，支持图片和视频 |

**imageList 每个元素：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `type` | string | 是 | 类型：`"image"` 图片 或 `"video"` 视频 |
| `src` | string | 是 | 图片/视频资源路径 |
| `url` | string | 否 | 点击跳转链接，不填则不可点击 |
| `title` | string | 是 | 展示标题 |
| `subTitle` | string | 否 | 副标题 |
| `description` | string | 否 | 描述文字 |
| `width` | string | 否 | 视频宽度（type=video 时） |
| `height` | string | 否 | 视频高度（type=video 时） |

> **图片/视频支持：** 此区域是主要的多媒体展示区，支持图片（jpg/png/gif）和视频（mp4）。
> **布局：** 两列流式布局（col-md-6），数量不限，自动换行。

### QA（常见问题）

- **类型：** 数组
- **数量限制：** 无限制
- **每个元素字段：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `question` | string | 是 | 问题/解答内容 |

> **注意：** 目前仅支持纯文字，不支持图文混排。

### footer（页脚）

- **类型：** 对象
- **字段：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `content` | array | 是 | 页脚列数组，**最多 4 个**（4 列布局，col-md-3） |
| `author` | string | 是 | 版权信息文字，支持 HTML |

**footer.content 每个元素（每一列）：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `title` | string | 是 | 列标题（大写显示） |
| `content` | array | 是 | 该列的链接/图片列表 |

**footer.content[].content 每个元素：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `title` | string | 否 | 链接文字（普通链接模式） |
| `url` | string | 否 | 链接地址 |
| `imageSrc` | string | 否 | 图片路径（图片模式，如二维码）。**填了此项则显示图片，忽略 title/url** |
| `description` | string | 否 | 链接描述（可选） |

> **限制：** `footer.content` 最多 4 列。每列内部的链接/图片数量无限制。
> **图片支持：** 页脚支持通过 `imageSrc` 字段显示图片（如二维码）。

---

## log.json 配置详解（日志模板）

以下是日志页面模板 `template/log.html` 对应的所有可配置参数。

### 全局配置

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `websiteTitle` | string | 是 | 网站标题 |
| `websiteIco` | string | 是 | 网站图标路径 |
| `assetsPath` | string | 否 | 资源路径前缀，static 目录下填 `"../"` |
| `updates` | array | 是 | 更新日志数组，按时间倒序排列（最新在前） |

### updates 每个元素

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `date` | string | 是 | 更新日期，如 `"2024年8月30日"` |
| `version` | string | 是 | 版本号，如 `"1.0.0"` |
| `isImp` | boolean | 否 | 是否重要版本，`true` 时高亮显示 |
| `changes` | array | 是 | 更新内容字符串数组 |

**示例：**
```json
"updates": [
  {
    "date": "2024年8月30日",
    "version": "1.0.0",
    "changes": [
      "【feature】完成备案，正式发布",
      "【feature】完成图书管理系统页面"
    ]
  },
  {
    "date": "2024年06月23日",
    "isImp": true,
    "version": "0.1.0",
    "changes": [
      "【feature】重构原项目",
      "【feature】使用 jinja2+json 表单配置"
    ]
  }
]
```

> **显示规则：**
> - 第一条（数组第一个）自动标记为「最新版本」，青色显示
> - 设置 `isImp: true` 的版本标记为「重要版本」，橙色显示
> - 普通版本橙色显示

---

## 限制与注意事项汇总

### 数量限制

| 模块 | 限制数量 | 原因 |
|------|----------|------|
| `desc.content` | 最多 3 个 | 三列布局（col-lg-4），超过会换行 |
| `footer.content` | 最多 4 个 | 四列布局（col-md-3），超过会换行 |
| `intro.btn` | 建议 2-3 个 | 过多会挤压布局 |
| `header` | 建议 3-6 个 | 导航栏空间有限 |

### 图片支持位置

| 位置 | 字段 | 说明 |
|------|------|------|
| 网站图标 | `websiteIco` | favicon |
| 简介区主图 | `intro.image` | 右侧大图片 |
| 按钮图标 | `intro.btn[].ico` | 按钮前小图标 |
| 展示区 | `displaySession.imageList[].src` | type=image 时是图片，type=video 时是视频 |
| 页脚二维码 | `footer.content[].content[].imageSrc` | 填了则显示图片 |

### HTML 支持

以下字段支持内嵌 HTML 标签：
- `intro.title`
- `intro.text`
- `desc.content[]`
- `footer.author`
- `log.changes[]`

支持的常用标签：`<a>`、`<br>`、`<ul>`、`<li>`、`<strong>` 等。

### 可修改 / 不可修改

| 类别 | 内容 | 修改方式 |
|------|------|----------|
| ✅ 可通过 JSON 修改 | 所有文字内容、链接、图片路径、按钮、导航项、颜色样式（style） | 编辑对应 JSON 文件 |
| ✅ 可通过 CSS 修改 | 页面样式、颜色、布局 | 编辑 `assets/css/` 下的样式文件 |
| ⚠️ 需改模板 | 模块顺序、模块增减、布局结构 | 编辑 `template/` 下的 HTML 模板 |
| ❌ exDesc 内容 | 最低配置三列的具体内容 | 当前硬编码在模板中，需改 `template/index.html` |

---

## assetsPath 说明

由于部分页面输出在根目录（`index.html`），部分在 `static/` 目录下，资源引用路径需要调整：

- **根目录页面**（如 `index.html`）：`assetsPath` 留空或不填，资源路径为 `assets/...`
- **static 目录页面**（如 `static/chess.html`）：`assetsPath` 设为 `"../"`，资源路径为 `../assets/...`

> 所有 JSON 配置中引用的资源路径（图片、视频、图标）都按「相对于 HTML 文件所在位置」来写，模板会自动加上 `assetsPath` 前缀。

---

## 样式说明

目前样式支持还在完善中，建议：
- 「项目说明」（desc.content）三个框的文字字数尽量相近，否则布局不美观
- 图片建议使用相近尺寸的横图，展示效果最佳
- 展示区（displaySession）为两列瀑布流布局，图片数量随意

---

## 部署

项目支持 GitHub Pages 部署，配置文件见 `.github/workflows/static.yml`。

推送到 main 分支后会自动部署。
