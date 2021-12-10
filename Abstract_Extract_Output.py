import os
from nltk.tokenize import sent_tokenize
import re

path_to_text_files = r"C:\Users\LENOVO\Desktop\projects\it_workshop\PY-PY\TXT"
for filename in os.listdir(path_to_text_files):

    absolute_text_path = os.path.join(path_to_text_files, filename)
    with open(absolute_text_path, 'r', encoding='utf-8') as f, open(r"C:\Users\LENOVO\Desktop\projects\it_workshop\PY-PY\Foutputrough.txt",'a', encoding='utf-8') as fw:
        text = f.read()
        result_string_table_caption = []
        result_string_sentence = []
        text2 = sent_tokenize(text)

        captionPattern = re.compile(r"Table \d+:")
        abstractPattern = re.compile(r"Table \d+ ")
        for token in text2:
            a = captionPattern.search(token)
            b = abstractPattern.search(token)
            if a:
                result_string_table_caption.append(token)
            if b:
                result_string_sentence.append(token)

        PaperID = re.findall(r"\d+", filename)

        for tableNos in range(len(result_string_table_caption)):
            fw.write(f"<Paper ID = {PaperID[0]}> ")
            fw.write(f"<Table {tableNos}> <Abstractive Summary> =")

            fw.write(result_string_table_caption[tableNos] + " </Abstractive Summary>")
            fw.write(" <Extractive Summary> ")

            for extracts in result_string_sentence:
                t = f"Table {tableNos} "
                if re.search(t, extracts):
                    fw.write(extracts + " ")
            fw.write(" </Extractive Summary> ")
            fw.write(f" </Table {tableNos}> ")
            fw.write(f" </Paper ID = {PaperID[0]}>\n\n\n")