# pokemonの分散表現   

単語ではないものの分散表現を取得する（今回の題材：ポケモンgoで実装されているポケモン251体）    
ポケモンの図鑑ナンバーをIDとして割り振り、以下の内容をdata.txtに記述   

1. 図鑑ナンバー   
2. タイプ毎の評価点順(火タイプで1行など)   
3. 進化関係(1行に001 002 003など)   
4. ポケモンgoにおける出現頻度の評価点順(Sランクで1行など)   
5. 画像の類似度(1ポケモンにつき1行、他250体のランキング)   

## 0. 事前準備   
gensimパッケージのダウンロード   

## 1. 画像の類似度を考慮しない場合   
word2vecの学習＆あるポケモンに似ているポケモンを出力  

`$ python test.py pokemon_nosim.txt`   

(デフォルトは"246", 変えたい場合は34行目の数字を図鑑IDに書き換え)   

## 2. 画像の類似度を考慮する場合   
word2vecの学習＆あるポケモンに似ているポケモンを出力   

`$ python test.py pokemon.txt`   

(デフォルトは"246", 変えたい場合は34行目の数字を図鑑IDに書き換え)   

## 3. 図鑑ID→ポケモン名に書き換えた場合（画像類似度あり）   
word2vecの学習＆あるポケモンに似ているポケモンを出力   

`$ python test.py pokemon_word.txt`   

(34行目の数字を名前に書き換え。例、246→ヨーギラス)   
