# 辞書を利用した翻訳サンプル

## .env

```
DICTIONARY_FILE="legal_dictionary.csv"  # 辞書ファイル
OPENAI_API_KEY=<API KEY>                # OpenAI API Key
GPT_MODEL="gpt-4-0125-preview"          # GPTモデル
```

## 辞書ファイル作成

サイトからダウンロードした「法令用語日英標準対訳辞書」を変換する

```
$ python dic_conv.py utf8_law.je.dic.16.0.a.csv
'legal_dictionary.csv'にデータを出力しました。
```

## 翻訳

翻訳するテキストファイルを指定して実行

```
$ python legal_translation.py sample.txt
```
