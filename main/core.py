#!/usr/bin/python3
#coding=utf-8

"""
凯撒加密
"""

import sys

# 加密依据的字符串
s = """ !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\n"""

def ch(x: int)->str:
    return s[x%len(s)]  # 防止越界

def od(c: str)->int:
    return s.find(c)

def check(x: str)->bool:
    """检查字符串x的值是否合法，合法返回None"""
    if x == None:
        return None
    for i in x:
        if i not in s:
            return (i, x.index(i))
    return None

def encrypt(key: str, m: str):
    """
    加密函数
    传入密钥和明文，转换成密文
    """
    # 延长密钥，方便操作
    tmp = key
    while len(key) < len(m):
        key += tmp
    
    # 加密功能核心
    ans = ""
    for i in range(0, len(m)):  # 遍历明文
        ans += ch(od(m[i])+od(key[i])+i)    # 最后再加i增加破解难度
    
    return ans

def decrypt(key: str, m: str)->str:
    """
    解密函数
    传入密钥和密文，转换成明文。
    """
    # 延长密钥，方便操作
    tmp = key
    while len(key) < len(m):
        key += tmp
    
    # 加密功能核心
    ans = ""
    for i in range(0, len(m)):  # 遍历密文
        ans += ch(od(m[i])-od(key[i])-i)
    
    return ans

if __name__ == "__main__":
    key = input("请输入密钥：")
    m = input("请输入明文：")
    if check(key) or check(m):
        print("有不支持加密的字符")
        sys.exit(1)
    print("加密结果:\n", encrypt(key, m))
    print("解密结果:\n", decrypt(key, m))
