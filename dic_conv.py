import csv
import sys
import prompt_ver.util as util


def main():
    env = util.load_environ()

    # 入力ファイル名
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} 対訳辞書ファイル")
        exit(1)
    input_filename = sys.argv[1]

    # 出力ファイル名
    output_filename = env["DICTIONARY_FILE"]

    # 入力ファイルを開いて処理
    with open(input_filename, mode="r", newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)

        # 出力ファイルを開いて処理
        with open(output_filename, mode="w", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile)
            # ヘッダーを書き込む
            writer.writerow(["用語", "訳語候補", "使い分け基準"])

            # 各行を処理
            for row in reader:
                term = row["用語"]
                criteria = row["使い分け基準"]
                translation_candidates = row["訳語候補"].split("/")[0]
                # 行を書き込む
                writer.writerow([term, translation_candidates, criteria])

    print(f"'{output_filename}'にデータを出力しました。")


if __name__ == "__main__":
    main()
