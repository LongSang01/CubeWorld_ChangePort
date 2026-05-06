# 魔方世界Alpha 端口修改器

`Cube World Alpha`默认连接端口为 `12345`, 使用起来较为不便

逆向游戏文件后, 通过替换`汇编`对应的`hex`来修改端口

新版本应该可以避免之前的修改后报错`客户端版本不匹配`

将匹配的特征改为上下`4`条汇编

- 客户端汇编为

  ```c
  movq(name) + mov eax,2 + push (端口2字节) 0000 + movq(var_1ch)
  ```

- 服务端汇编为

  ```c
  mov eax,2 + movq(name) + push (端口2字节) 0000 + movq(var_1ch)
  ```

## 务必事先备份对应 EXE 文件

```
python changeport.py Cube.exe/Server.exe 自定义端口
```
