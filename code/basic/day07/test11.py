"""
设计一个函数长度生成指定的验证码,验证码大小写字母和数字组成
"""
import random


def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for x in range(code_len):
        code += all_chars[random.randint(0, len(all_chars) - 1)]
    return code

if __name__ == "__main__":
    code = generate_code(4)
    print(code)
