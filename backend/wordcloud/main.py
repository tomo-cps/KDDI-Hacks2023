import os
from langchain.document_loaders import PyPDFLoader
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

class PaperWordCloud():
    def __init__(self):
        os.environ["OPENAI_API_TYPE"] = "azure"
        os.environ["OPENAI_API_KEY"] = "b2caf052e14340aa94abe712a3cace53"
        os.environ["OPENAI_API_BASE"] = "https://gpt-eastus-ateam.openai.azure.com/"

    def replace_word_in_text(self, text, old_word, new_word):
        pattern = re.compile(r'\b{}\b'.format(re.escape(old_word)))
        new_text = re.sub(pattern, new_word, text)
        return new_text

    def extract_nouns(self, text):
        tokenizer = Tokenizer()
        nouns = []
        tokens = tokenizer.tokenize(text)
        for token in tokens:
            part_of_speech = token.part_of_speech.split(',')[0]
            if part_of_speech == '名詞':
                nouns.append(token.surface)
        return nouns

    def generate_wordcloud(self, words, font_path):
        wordcloud = WordCloud(width=800, height=400, font_path=font_path, background_color='white').generate(' '.join(words))
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig('./output/hoge.png')
        plt.show()

    def main(self):
        loader = PyPDFLoader("../data/twitter.pdf")
        input_list = loader.load_and_split()
        font_path = "./font/SourceHanSerifK-Light.otf"
        text=str(input_list[0])
        text = re.sub(r'\s+', '', text)
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'n', '', text)
        text = re.sub(r'page_cotet', '', text)

        nouns = self.extract_nouns(text)
        filtered_nouns = [word for word in nouns if len(word) < 10]
        filtered_nouns = [word for word in filtered_nouns if not word.isdigit()]
        self.generate_wordcloud(filtered_nouns, font_path)

if __name__ == "__main__":
    output = PaperWordCloud()
    output.main()
