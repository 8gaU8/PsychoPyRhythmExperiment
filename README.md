# PsychoPyリズム実験

## 実行

```bash
pyrun ./rhythm_trial_exp_lastrun.py
```

## TODO
- こしてんはずっと出しておく
- 回答してくださいのメッセージを視覚でつくる
- 輝度が同じ
  - パステルカラーみたいな
  - 色変えない
  - 被験者にたいして、視覚メッセージの影響がないことをじっけんで示す
- 体動かす、動かさない、レスト（音無し）
- タッピングを取得できるようにする
  - キーボードORボタン
- フォントはちゃんと出せるようにする
- かくtrial前に3秒くらいの時間あける
- インストラクション→3秒→trial→2秒
- https://pressrelease.brainproducts.com/triggerbox2/
- コントロール実験大事に


## メモ

- リズムのパターンは [The sensation of groove engages motor and reward networks, Fig1](https://doi.org/10.1016/j.neuroimage.2020.116768)から

## 実験bnm01 反省点
- 教示の問題
  - 音がない区間もタッピングしていい？　していい
  - タッピングのパターンは？　一定のテンポで
- 実装の問題
  - テンポが速い時、ブレが大きくなる
    - play_noneを適用して修正
  - 明らかに120%テンポより速いのがあった
    - exp_paramsを修正する
- 実験全体の問題
  - 利き手テスト
  - 強制的に数分の休憩をいれる