from sys import argv


def replace_hex_in_exe(file_path, old_hex_str, new_hex_str):
    """
    替换EXE文件中的十六进制序列。

    Args:
        file_path (str): EXE文件的路径。
        old_hex_str (str): 要查找的旧十六进制字符串
        new_hex_str (str): 用于替换的新十六进制字符串
    """
    try:
        # 将十六进制字符串转换为字节序列
        old_bytes = bytes.fromhex(old_hex_str)
        new_bytes = bytes.fromhex(new_hex_str)

        if len(old_bytes) != len(new_bytes):
            print(f"错误: 旧十六进制序列和新十六进制序列的长度不一致。")
            return

        # 以二进制读写模式打开文件
        with open(file_path, "rb+") as f:
            content = f.read()  # 读取整个文件内容

            # 查找旧字节序列
            offset = content.find(old_bytes)

            if offset != -1:
                print(f"找到旧十六进制序列 '{old_hex_str}'，位于偏移量: {hex(offset)}")

                # 将文件指针移到找到的位置
                f.seek(offset)
                # 写入新的字节序列
                f.write(new_bytes)
                print(f"成功将 '{old_hex_str}' 替换为 '{new_hex_str}'。")
                return True
            else:
                print(f"未在文件中找到旧十六进制序列 '{old_hex_str}'。")

    except FileNotFoundError:
        print(f"错误: 文件未找到 - {file_path}")
    except Exception as e:
        print(f"发生错误: {e}")


def portsum(port):
    return str(f"{int(port):04x}"[::-1])


if __name__ == "__main__":
    if len(argv) < 4:
        print("changeport exe路径 原端口 修改后的端口")
        print("魔方世界默认联机端口为12345")
        print("不建议使用过小的端口号以防止替换字符串唯一性错误")
        print("请务必先备份对应exe !!!")
        exit()
    else:
        exe_file = argv[1]  # 替换为你的EXE文件路径
        oldport = argv[2]
        newport = argv[3]
        old_hex = "68" + portsum(oldport) + "0000"
        new_hex = "68" + portsum(newport) + "0000"

        if replace_hex_in_exe(exe_file, old_hex, new_hex):
            print(f"已将 {exe_file} 的连接端口 {oldport} 改为 {newport}")
