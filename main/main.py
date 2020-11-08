#!/usr/bin/python3
#coding=utf-8

"""
main
"""

try:
    # 导入库
    import sys
    import argparse
    try:
        import core
    except ModuleNotFoundError:
        print("加密模块丢失！")
        sys.exit(1)
    try:
        from load import extdict, extarg
    except ModuleNotFoundError:
        print("没有扩展模块！")
        sys.exit(1)
    
    # 基本选项与扩展选项
    parser = argparse.ArgumentParser(description="加密解密")
    parser.add_argument("-k",help="密钥",type=str)
    parser.add_argument("-s",help="待操作的字符串",type=str)
    parser.add_argument("--ext",help="使用的扩展",type=str)
    parser.add_argument("--enc",help="表示需要加密(否则就是解密)",action="store_true")
    for i in extarg.keys():
        parser.add_argument(i,help=extarg[i])
    args = parser.parse_args()

    # 获取必要信息
    key = args.k
    s = args.s
    if key == None:
        from getpass import getpass
        key = getpass("请输入key（已隐藏输入内容）: ")
    if s == None:
        try:
            s = ""
            while 1:
                s = s + "\n" + input()
        except EOFError:
            pass
    
    # 基本加密解密
    if args.ext != None:
        if core.check(s) or core.check(key):
            print("有输入不合法！")
        if args.enc:
            print(core.encrypt(key,s))
        else:
            print(core.decrypt(key,s))

    # 调用扩展
    pass

except InterruptedError:
    print("用户退出")
    sys.exit(0)