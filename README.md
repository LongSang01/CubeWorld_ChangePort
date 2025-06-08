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

修改服务端端口在使用 `汉化版客户端` 或 `Mod` 时可能会报错 `版本不匹配`，非必要不建议修改服务端端口，使用[`frp`](https://github.com/fatedier/frp/)等工具或端口转发即可  
推荐主机端使用原版客户端，联机端使用修改端口的客户端
