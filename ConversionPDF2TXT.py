import os
import pdfplumber

path_to_your_files = "C:\PDF"
path_to_text_files = "C:\TXT"
for filename in os.listdir(path_to_your_files):

    absolute_file_path = os.path.join(path_to_your_files, filename)
    absolute_text_path = os.path.join(path_to_text_files, filename)
    with pdfplumber.open(absolute_file_path) as pdf:
        print(absolute_file_path)
        for page in pdf.pages:
            text = page.extract_text()
            with open(
                    os.path.splitext(absolute_text_path)[0] + ".txt", encoding="utf-8", mode="a"
            ) as f:
                f.write(str(text))
    print("Operation Success!")