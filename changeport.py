import struct
from sys import argv
import re


def replace_hex_in_exe(file, offset: int, new_bytes: bytes) -> None:
    """在指定偏移量写入新的hex"""
    file.seek(offset)
    file.write(new_bytes)
    print(f"成功替换数据，偏移量: {offset}")


def port_to_hex(port: int) -> str:
    """端口转 2 字节小端 hex"""
    port = int(port)

    if port < 1024 or port > 65535:
        print("端口需在 1024-65535 之间")
        exit()

    return struct.pack("<I", port)[:2]


def find_sig(file, new_port: int):
    """正则查找特征码, 返回偏移量和需要替换的新特征码"""

    movq_name = b"\x66\x0f\xd6\x45\xe0"
    mov_eax_2 = b"\xb8\x02\x00\x00\x00"
    push_port = b"\x68" b".{2}\x00\x00"  # 正则匹配 2 字节旧端口
    movq_var = b"\x66\x0f\xd6\x45\xe8"

    # 客户端特征码：movq(name) + mov eax,2 + push (2字节) 0000 + movq(var_1ch)
    client_pattern = movq_name + mov_eax_2 + push_port + movq_var
    # 服务端特征码：mov eax,2 + movq(name) + push (2字节) 0000 + movq(var_1ch)
    server_pattern = mov_eax_2 + movq_name + push_port + movq_var

    content = file.read()

    # 搜索匹配的特征码
    for pattern in (client_pattern, server_pattern):
        match = re.search(pattern, content, re.DOTALL)
        if match:
            old_sig = match.group()
            offset = match.start()

            # 解析旧端口
            old_port = struct.unpack("<H", old_sig[11:13])[0]
            print(f"检测到原端口为: {old_port}")

            # 直接切片拼接
            new_sig = old_sig[:11] + port_to_hex(new_port) + old_sig[13:]
            print(f"修改端口为: {new_port}")

            return offset, new_sig

    print("未查找到特征码")
    exit()


if __name__ == "__main__":

    if len(argv) < 3:
        print("changeport exe路径 原端口 修改后的端口")
        print("魔方世界默认联机端口为12345")
        print("请务必先备份对应exe !!!")
        exit()

    exe_file = argv[1]
    new_port = int(argv[2])

    with open(exe_file, "rb+") as file:
        offset, new_sig = find_sig(file, new_port)

        replace_hex_in_exe(file, offset, new_sig)
