import brain
import brain_util as bu
import numpy as np
import pptree
import json
import copy
import jieba

from collections import namedtuple
from collections import defaultdict
from enum import Enum

import parser as p

def setup_jieba_for_lexemes():
    """
    目标：分词结果尽量只产生 CHINESE_LEXEME_DICT 里的词元。
    做法：
    1) 把所有词元加入 jieba 用户词典（高频），避免被拆开；
    2) 对少数需要“强制切开”的地方用 suggest_freq（如 踢+球）。
    """
    # 1) 加入用户词典：让这些词尽量“整体成词”
    for w in p.CHINESE_LEXEME_DICT.keys():
        # freq 给高一点，减少被拆分概率；tag 这里不强依赖
        jieba.add_word(w, freq=10_000)

    # 2) 强制切分/合并的关键点（与词元表对齐）
    # 我踢球 -> 我 / 踢 / 球（而不是 踢球）
    jieba.suggest_freq(("踢", "球"), True)

    # 红温了 / 愚蠢的 / 愤怒地 这些不要被拆
    jieba.suggest_freq("红温了", True)
    jieba.suggest_freq("愚蠢的", True)
    jieba.suggest_freq("聪明的", True)
    jieba.suggest_freq("硬邦邦的", True)
    jieba.suggest_freq("愤怒地", True)
    jieba.suggest_freq("无可奈何地", True)
    jieba.suggest_freq("一颗", True)

def tokenize(sentence: str):
    s = sentence.replace(" ", "").strip()
    tokens = [t.strip() for t in jieba.lcut(s, HMM=False) if t.strip()]
    return tokens

test_data=["我红温了",
           "我并非人类",
           "我踢球",
           "你真善良",
           "愚蠢的我踢球",
           "我踢硬邦邦的球",
           "愚蠢的我踢硬邦邦的球",
           "愚蠢的我愤怒地踢一颗硬邦邦的球",
           "你真温柔善良大度"
           ]

def run_tests():
    setup_jieba_for_lexemes()
    for sentence in test_data:
        tokens = tokenize(sentence)
        temp=" ".join(tokens)
        print(f"分词结果: {temp}")
        p.parse(temp, language="Chinese", verbose=False, debug=False)


if __name__ == "__main__":
    run_tests()