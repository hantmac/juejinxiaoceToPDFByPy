
<p align="center">
<img src="https://img.shields.io/badge/language-python-green.svg">
<img src="https://img.shields.io/badge/dependencies-pdfkit-yellow.svg">
<img src="https://img.shields.io/badge/dependencies-requests-green.svg">
</p>

# juejinxiaoceToPDFByPy
将掘金小册制作成一整本PDF
## 由来
之前写过一个[Golang的版本](https://github.com/hantmac/juejinxiaoceToMobi)，但是阅读效果不是特别好，这个Python版本可以将所有章节制作成单个PDF文件。看起来会更加方便，转mobi格式的正在开发，遇到一点小问题，使用的`kindle_maker`库报错。如果想要在kindle上观看小册，可以使用[这个工具](https://pdf2mobi.com/zh/)将PDF转为mobi。
## 使用方法
- 参照 https://github.com/hantmac/juejinxiaoceToMobi 的README，获取你想要转换的小册的`id`、`client_id`、`uid`、`token`、等信息，按照`ini`文件的格式填入`conf.ini`；
- pip3 install -r requirements.txt (环境为Python3)
- python run.py 
- 等待片刻，即可出炉 🍺

## 注意事项
- conf.ini中的`bookName`千万不能含有中文，不然PDF会乱码
- 使用的pdfkit，可能会比较慢
- 如果中间报错，很可能是没有安装 wkhtmltopdf，按照[官方教程](https://github.com/JazzCore/python-pdfkit)进行安装
- Mac OS在安装过程中遇到一个错误 `Error: Permission denied @ dir_s_mkdir - /usr/local/Caskroom/wkhtmltopdf`，查了一下，解决方案是：`sudo chown -R $(whoami):staff ~/Library/Caches/Homebrew /usr/local/Caskroom/`

## 效果预览
![](https://ws2.sinaimg.cn/large/006tKfTcly1g1fi2d1z6dj31hf0u0b2a.jpg)
![](https://ws3.sinaimg.cn/large/006tKfTcly1g1fi3wlpjrj31mq0u0b29.jpg)
