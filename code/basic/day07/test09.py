"""
使用字典
"""


def main():
    score = {'小明':99, '小莉莉':100, '小黑':78}
    print(score['小明'])
    print(score['小黑'])
    for key in score:
        print('name:%s,score:%d'% (key, score[key]))
    score = {'小帅':78}
    score.update(小美=100,肖帅=19)
    score.popitem()
    print(score)


if __name__ == '__main__':
    main()

