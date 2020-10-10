"""
凯撒加密
"""

from random import randint
import sys
import random

# 加密依据的字符串
s = """ !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def ch(x: int)->str:
    """
    替代内置函数chr实现更灵活的控制。
    """
    return s[x%len(s)]  # 防止越界

def od(c: str)->int:
    """
    替代内置函数ord实现更灵活的控制。
    """
    return s.find(c)

def check(x: str)->bool:
    """检查字符串x的值是否合法"""
    for i in x:
        if i not in s:
            print(f"输入不合法：{i}")
            sys.exit(0)

def encrypt(key: str, m: str):
    """
    加密函数
    传入密钥和明文，转换成密文
    """
    # 延长密钥，方便操作
    random.seed(key)
    tmp = key
    while len(key) < len(m):
        key += tmp
    
    # 加密功能核心
    ans = ""
    for i in range(0, len(m)):  # 遍历明文
        ans += ch(od(m[i])+od(key[i])+i+random.randint(1, 1024))    # 最后再加i增加破解难度
    
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
    random.seed(key)
    
    # 加密功能核心
    ans = ""
    for i in range(0, len(m)):  # 遍历密文
        ans += ch(od(m[i])-od(key[i])-i-randint(1, 1024))
    
    return ans

if __name__ == "__main__":
    key = input("请输入密钥：")
    m = input("请输入明文：")
    check(key)
    check(m)
    print("加密结果:\n", encrypt(key, m))
    print("解密结果:\n", decrypt(key, m))
