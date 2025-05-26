# 魔方世界端口修改器

魔方世界默认连接端口为 12345, 使用起来较为不便

基于
[Cube-World-Alpha-Client-Port-Switcher](https://github.com/coremaze/Cube-World-Alpha-Client-Port-Switcher/) 使用 python 重写


```
python changeport.py Cube.exe 原端口 自定义端口
```
也可修改服务端端口

```
python changeport.py Server.exe 原端口 自定义端口
```

# 注意事项
**务必事先备份对应 EXE 文件**

尽量不要使用较小的端口，以防止替换十六进制字符串唯一性错误
