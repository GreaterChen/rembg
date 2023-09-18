# REMBG 项目接口

### 项目结构

rembg

└─router

​	└─fastapi_rembg.py	基于fastapi的rembg接口

​	└─utils.py		若干工具函数

└─until		

​	└─image_type.py		各种图片格式转换函数

└─weights		

​	└─u2net.onnx	权重文件

└─main.py	基于gradio的图形化界面

### fastapi接口		

1. 方法：POST

2. url：localhost:8001/upload

3. 请求参数

    | 字段 |     说明     |  类型  |        备注         | 是否必填 |
    | :--: | :----------: | :----: | :-----------------: | :------: |
    | img  |  输入的图像  | string | 支持base64和url格式 |    是    |
    | size | 输出图片尺寸 |  int   |                     |    是    |
    
4. 请求示例

```json
{
    "size":500,
    "img":"https://img.evlook.com/evlook/ueeditor/autocoty/131829222851861715.jpg",
}
```

5. 返回参数

    接口返回头图的base64格式信息

```json
"code": 1,
"message": "success",
"data":
{
    "return_image": img,
}
```
