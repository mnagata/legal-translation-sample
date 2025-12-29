import sys
import csv
import util
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    HTMLHeaderTextSplitter,
)
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI


def main():
    # 入力ファイル名
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} 翻訳対象テキストファイル")
        exit(1)
    input_filename = sys.argv[1]

    documents = load_source_document(input_filename)

    output = translation(documents)

    print(output)


def load_source_document(file_path):
    data = TextLoader(file_path)
    docs = data.load()
    return docs


def translation(documents):
    env = util.load_environ()

    system_template = """あなたは翻訳アシスタントです。日本語を英語に翻訳します。 下記のルールに注意してください:
- 元の文章構造を維持すること。
- 翻訳の精度は重要ですが、「翻訳っぽい」結果にならないよう気をつけてください。
- 単語ごとの対応に気を配りすぎず、自然さや伝わりやすさを優先させてください

ドメイン特化した単語の翻訳辞書を書きに示しますので、使い分け基準を考慮して適宜使用すること：
<Dictionary start>
日本語: 英語: 使い分け基準
{legal_dictionary}
<End of Dictionary>"""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

    human_template = """Here is a chunk text to translate"
Return the translated text only, without adding anything else.
Text: {source}"""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chat = ChatOpenAI(model_name=env["GPT_MODEL"], temperature=0.5)
    chain = LLMChain(llm=chat, prompt=chat_prompt, output_key="output")

    translated_docs = ""
    for chunk in documents:
        result = chain.invoke(
            {"legal_dictionary": get_dictionary(env), "source": chunk.page_content}
        )
        translated_docs += result["output"]

    return translated_docs


def get_dictionary(env):
    # 出力CSVファイル名
    input_filename = env["DICTIONARY_FILE"]
    # 出力テキストの内容を保持する変数
    dictionary_text = ""

    # CSVファイルを開いてテキストに変換
    with open(input_filename, mode="r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        next(reader)  # ヘッダーをスキップ

        # 各行をテキストに変換
        for row in reader:
            term, translation, criteria = row
            # フォーマットに従ってテキストを追加
            dictionary_text += f"{term}: {translation}: {criteria}\n"

    return dictionary_text


if __name__ == "__main__":
    main()
