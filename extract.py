import os
from nltk.tokenize import sent_tokenize
import re

path_to_text_files = r"C:\Users\LENOVO\Desktop\projects\it_workshop\PY-PY\TXT"
for filename in os.listdir(path_to_text_files):

    absolute_text_path = os.path.join(path_to_text_files, filename)
    with open(absolute_text_path, 'r', encoding='utf-8') as f, open(r"C:\Users\LENOVO\Desktop\projects\it_workshop\PY-PY\outputrough.txt",'a', encoding='utf-8') as fw:
        fw.write(filename)
        fw.write("\n")
        fw.write("\n")
        text = f.read()
        result_string_table_caption = []
        result_string_sentence = []
        text2 = sent_tokenize(text)

        captionPattern = re.compile(r"Table \d:")
        abstractPattern = re.compile(r"Table \d ")
        for token in text2:
            a = captionPattern.search(token)
            b = abstractPattern.search(token)
            if a:
                result_string_table_caption.append(token)
            if b:
                result_string_sentence.append(token)

        for tableNos in range(len(result_string_table_caption)):
            fw.write(f"Table {tableNos+1}\n")
            fw.write(result_string_table_caption[tableNos] + "\n")
            fw.write("Abstractive Summary: \n")
            for abstracts in result_string_sentence:
                t = f"Table {tableNos+1} "
                if re.search(t, abstracts):
                    fw.write(abstracts + "\n")