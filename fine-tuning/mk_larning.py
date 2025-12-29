import csv
import json

## ファインチューニングJSONファイル作成

# CSVファイルのパス
csv_file_path = "legal_dictionary.csv"
# JSONファイルのパス
json_file_path = "output.json"


# CSVからJSONに変換する関数
def convert_csv_to_json(csv_file_path, json_file_path):
    # 結果を格納するリスト
    json_list = []

    # CSVファイルを開く
    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        # CSVリーダーを作成
        csv_reader = csv.reader(csvfile)

        # 各行を処理
        for row in csv_reader:
            json_list = multiply_text(json_list, row)

    # JSONファイルに書き込む
    with open(json_file_path, mode="w", encoding="utf-8") as jsonfile:
        jsonfile.write(json.dumps(json_list, ensure_ascii=False) + "\n")


def multiply_text(json_list, row):
    prompts = []
    if not row[2]:
        prompts.append(f"法律の文書に現れる用語、「{row[0]}」の英語訳")
        prompts.append(f"法令に記載されている言葉、「{row[0]}」の英訳")
        prompts.append(f"法律文書に使用される語句、「{row[0]}」の英語による翻訳")
        prompts.append(f"法的文書で使われる用語、「{row[0]}」の英語での対応語")
        prompts.append(f"法規において使われる言葉、「{row[0]}」の英語での表現")
        prompts.append(f"法令における専門用語、「{row[0]}」の英語翻訳")
        prompts.append(f"法的な文章における用語、「{row[0]}」の英語における同等語")
        prompts.append(f"法律上の文書に記される専門語、「{row[0]}」の英語による同義語")
        prompts.append(f"法律関連の文章にある単語、「{row[0]}」の英文での訳語")
        prompts.append(f"法律用語として文中に出現する、「{row[0]}」の英語での意味")
    else:
        prompts.append(
            f"法律の条文に{row[2]}というフレーズが含まれている場合、「{row[0]}」の英訳"
        )
        prompts.append(
            f"法的文書で{row[2]}という言葉が使用された際、「{row[0]}」の英訳"
        )
        prompts.append(
            f"法規のテキストに{row[2]}という表現が見られる時、「{row[0]}」の英訳"
        )
        prompts.append(f"法的な記述で{row[2]}という部分がある場合、「{row[0]}」の英訳")
        prompts.append(
            f"法律に関する文章において{row[2]}という節がある場合、「{row[0]}」の英訳"
        )
        prompts.append(
            f"法的な文脈で{row[2]}という語句が登場する際、「{row[0]}」の英訳"
        )
        prompts.append(
            f"法規定に{row[2]}というセクションが含まれている時、「{row[0]}」の英訳"
        )
        prompts.append(
            f"法的ドキュメントに{row[2]}という句が挿入されている場合、「{row[0]}」の英訳"
        )
        prompts.append(
            f"法令の記載で{row[2]}という部分が見受けられる際、「{row[0]}」の英訳"
        )
        prompts.append(
            f"法的記録に{row[2]}という表記が確認される時、「{row[0]}」の英訳"
        )

    for prompt in prompts:
        json_data = {
            "prompt": prompt,
            "completion": row[1],
        }
        json_list.append(json_data)
        print(f"{prompt}{row[1]}")

    return json_list


# スクリプトを実行
convert_csv_to_json(csv_file_path, json_file_path)
