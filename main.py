import matplotlib.pyplot as plt
import codecs
import re

def main(cipher_data):
    #計算するやつを用意
    char = [chr(i) for i in range(97, 97+26)]
    cnt = [0 for i in range(26)]

    #正規化
    cipher_data_norm = cipher_data.lower()
    cipher_data_norm = re.sub('\n', ' ', cipher_data_norm)

    #カウント
    for i in range(26):
        cnt[i] = cipher_data_norm.count(char[i])

    #表へプロット
    x = [i for i in range(1,27)]
    y = cnt
    plt.bar(x, y, align='center')
    plt.xticks(x, char)
    plt.show()


if __name__ == '__main__':

    #'sample.txt'から文章の読み込み
    f = open('sample.txt')
    text = f.read()
    f.close()

    #暗号化
    encrypt_data = codecs.encode(text, 'rot13')

    #実行
    main(encrypt_data)
