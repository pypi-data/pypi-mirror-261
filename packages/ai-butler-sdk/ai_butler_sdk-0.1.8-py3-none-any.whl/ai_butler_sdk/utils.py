import zipfile
import chardet
import os
import shutil
import socket


def is_port_open(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)  # 设置超时时间
    try:
        sock.connect((ip, int(port)))
        return True
    except (socket.timeout, ConnectionRefusedError):  # 端口不可达或连接被拒绝
        return False
    finally:
        sock.close()


def support_gbk(zip_file: zipfile.ZipFile):
    """
    用于支持解码中文路径，避免乱码
    """
    name_to_info = zip_file.NameToInfo
    for name, info in name_to_info.copy().items():
        name_list = os.path.split(name)
        real_name = ""
        for n in name_list:
            try:
                encoding = chardet.detect(n.encode("cp437")).get("encoding")
            except UnicodeEncodeError:
                real_name = "/" + n
            else:
                if encoding:
                    real_name += "/" + n.encode("cp437").decode(encoding)
                else:
                    real_name += "/" + n

        if real_name != name:
            info.filename = real_name
            del name_to_info[name]
            name_to_info[real_name] = info
    return zip_file


def unzip_file(zip_path, target_dir):
    with support_gbk(zipfile.ZipFile(zip_path, "r")) as zip_ref:
        zip_ref.extractall(target_dir)

    # 删除解压目录中的__MACOSX .DS_Store
    for root, dirs, files in os.walk(target_dir):
        if "__MACOSX" in dirs:
            macosx_dir = os.path.join(root, "__MACOSX")
            shutil.rmtree(macosx_dir)
        if ".DS_Store" in dirs:
            macosx_dir = os.path.join(root, ".DS_Store")
            shutil.rmtree(macosx_dir)
