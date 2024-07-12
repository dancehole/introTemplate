# 项目文档攥写建议
> 适用场景：demo游戏，创意产品，和一些中小型项目的简介（公司简介也可）

优点：基于简单后端+对象存储服务实现存储
可以在线编辑，添加页面
含运维界面

使用json配置表单

## 快速开始
进入template目录，

## json表单配置及对应关系

#### 导航栏
建议配置：
- bug反馈（体验反馈）
- 捐赠者名单（没有写模板，但是有示例）
- 更新日志
- 网站地址/github/gitee/文档/快速开始/。。。


#### 简介

**使用方法**
1. 编辑config.json ：模板的名称，默认从/template读取html模板，/json读取json配置，请独立配置资源文件。config.json包含了所有需要渲染的模板。json文件名不要带后缀！！
2. 运行render.py


#### 说明

目前样式支持还不太完善，建议：
“项目说明”三个框文字建议字数相似，否则不好看

#### 额外说明

#### 图片展示

#### Q&A

#### 页脚





关于设置flex图片流布局时的心得：(还是chatgpt+图片nb)

从这样修改为这样：

![image-20240630221815740](https://cdn.jsdelivr.net/gh/dancehole/image@main/codelabs/image-20240630221815740.png)

![image-20240630221755260](https://cdn.jsdelivr.net/gh/dancehole/image@main/codelabs/image-20240630221755260.png)





需求：原本是一个图片50%宽度，我希望展示成图片流的形式



修改：

```css
.col-md-6 {
		-webkit-box-flex: 0;
		-ms-flex: 0 0 50%;
		flex: 0 0 50%;
		width:auto;
	}
```



为

```css
	.col-md-6 {
		-webkit-box-flex: 0;
		-ms-flex: 0 0 50%;
		flex: 0 0 auto;
		max-width:50%;
	}
```

真的找了我很久。。。
