# 意味粒度解析機

## 形態素解析とは別の発想

## 頻出の最低単位である群を考える
もともと、英語圏では、単語と単語のつなぎに余白を使うので、余白が最小の粒度だと定義するのに違和感がない
しかし、日本語を文化とする場合、果たして品詞という枠組みによる当てはめは最適なのかという疑問が生じる

今回、意味粒度を取り出す別のアプローチを提案するので参考にしてほしい

## ひとまとまりの粒度の構築
RNNでもヒエラルキカルベイズでもいいともうのだが、連続の確率遷移分布を計算し、その確率が太い場所を探索する
言葉では通じないと思うので図示するとイメージとしてはこのようになる

<p align="center">
  <img width="400" src="https://cloud.githubusercontent.com/assets/4949982/25890061/2280afd8-35a7-11e7-8633-8b0e317a267d.png">
</p>
<div align="center">図1. このような連鎖系のイメージする</div>

マルコフチェーンと少し違うのが、以前の状態を記憶していないわけでなく、同時に2gram以上を考える。
探索的に1 ~ 10gram程度のcharactorの連なりを背景事象として、次に来るcharctorのダイバーシティ*1を計算する

ダイバーシティとは、次に来る単語がどの程度の確率で確定的(P1)なのか、どの程度の単語を分散をもつか(p2)の２パラメータからなるヒューリスティックである。
この2変数が取りうる分布で意味粒度を構築する

## 実践
MeCabのような形態素解析エンジンから分布を取り出し、これに近似させることで、MeCabに近い出力を得たり、任意の粒度で切り取ることが可能である。

## 具体的な利用シーン
Bag Of Wordsを構築する際、もっとも適切な単語分割粒度が不明な祭、精度を得るために、利用可能である。
探索域が増えるので、より高精度が期待できる。

## 例
コントロールコードが入っているが、このような出力になる
```
何 /<2>409という /<18>412綺麗 /<5>415な、 /<10>417立派に /<2>419なった /<2>422ことであ /<2>425ろう /<4>429』 /<15>431掃除の行届 /<2>432いた /<17>437劇場 /<11>439前の /<3>441人 /<49>443道 /<9>444は /<287>445水に /<2>446洗 /<3>448われて、 
```
エンピリカルな視点においてうまくいっている

## 実行
入力に使う文章の長さに依存するが、小説一冊ぐらいならほぼ一瞬である
```python
$ python3 processor.py
```