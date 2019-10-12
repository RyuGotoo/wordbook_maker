import csv
import requests


BASE_ARTICLE_PATH = "articles/"
TEST = "test_article01.txt"
ARTICLE1 = "article001.txt"
ARTICLE2 = "article002.txt"
# ARTICLE_PATH = BASE_ARTICLE_PATH + TEST
ARTICLE_PATH = BASE_ARTICLE_PATH + ARTICLE2
MAX_WORDS = 5


def main():
    article_txt = get_article_txt(ARTICLE_PATH)
    word_list = split_by_symbols(article_txt)
    export_csv(word_list)
    print('Export complete!')


def get_article_txt(article_path):
    article_txt = open(article_path).read()
    return article_txt


def split_by_symbols(txt):
    word = ''
    word_list = []
    for s in txt:
        if s.isalpha():
            word += s
        else:
            if 3 < len(word) < 16:
                word_list.append(word.lower())
            word = ''
    word_list = list(set(word_list))  # 要素の重複を削除
    word_list.sort(key=len, reverse=True)  # 文字の長さ順にソート
    return word_list


def export_csv(word_list):
    with open('wordbook.csv', 'w') as csv_file:
        fieldnames = ['Word', 'inJapanese']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for word in word_list[:MAX_WORDS]:
            writer.writerow({'Word': word, 'inJapanese': translate(word)})


def translate(en_word):
    BASE_URL = 'https://script.google.com/macros/s/AKfycbxHqrRlPFP54ArkxyMVa-oiz7-miKQltWmAQ94pOcFLYsTk6fWd/exec?source=en&target=ja&text='
    # BASE_URL + $翻訳したい単語 みたいに使う
    ja_word = requests.get(BASE_URL + en_word).text
    return ja_word


if __name__ == '__main__':
    main()
