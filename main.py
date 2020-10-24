#!/usr/bin/python3
#coding=utf-8

"""
main
"""

try:
    import click as cli
    import sys
except ModuleNotFoundError:
    print("未安装click模块，请使用pip install click安装")
    print("程序终止")
    sys.exit(1)
except InterruptedError:
    print("用户退出")
    sys.exit(0)

try:
    import core
    @cli.command(help="加密解密")
    @cli.option("-k", help="密钥", type=str)
    @cli.option("-a", help="加密一个字符串", type=str, default=None)
    @cli.option("-b", help="解密一个字符串", type=str, default=None)
    def en(k: str,a: str,b: str):
        if not (a or b):
            print("请填写要加密的字符或要解密的！")
            sys.exit(1)
        if a and b:
            print("-a 和 -b 选项不能同时使用！")
        cha = core.check(a)
        chb = core.check(b)
        chk = core.check(k)
        if cha:
            print(f"-a 选项里不支持'{cha[0]}'字符")
            sys.exit(1)
        if chb:
            print(f"-b 选项里不支持'{chb[0]}'字符")
            sys.exit(1)
        if chk:
            print(f"-k 选项里不支持'{chk[0]}'字符")
            sys.exit(1)

        if a:
            print(core.encrypt(k, a), end="")
        if b:
            print(core.decrypt(k, b), end="")



    en()

except InterruptedError:
    print("用户退出")
    sys.exit(0)
except Exception as e:
    print(f"主程序运行时发生错误：{e}")
    print("你可以提issue哦！")
    print("gitee.com/gitkunkun/caesar")
    sys.exit(1)

try:
    from ext import *
except ModuleNotFoundError:
    print("警告：当前目录下没有ext目录(扩展目录)，只能提供基础操作！")
except InterruptedError:
    print("用户退出")
    sys.exit(0)
except Exception as e:
    print(f"加载扩展时发生错误：{e}")
