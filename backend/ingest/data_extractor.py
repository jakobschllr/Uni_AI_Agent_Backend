import fitz
import re


class DataExtractor():
    def __init__(self):
        pass

    def is_noise(self, sentence):
        if (len(sentence) < 3):
            return True
        if all(char.isdigit() or char in '/=+*.,- ' for char in sentence):
            return True
        return False

    def get_pdf_data(self, path):
        doc = fitz.open(path)
        text_lines = []
        for page in doc:
            page_lines = page.get_text().splitlines()
            for line in page_lines:
                text_lines.append(line)
        
        return text_lines

    
    # receives a String containing raw text data from file
    def clean_data(self, data):
        temp_text = re.sub('[!@#$]', '', data)
        temp_text = re.sub(r'\\n', ' ', temp_text)
        temp_text = re.sub(r'\n', ' ', temp_text)
        temp_text = re.sub(r'\\n{2,}', '\\n\\n', temp_text)
        temp_text = re.sub(r'[^\w\säöüÄÖÜß()"\']+', '', temp_text) # ungewöhnliche Zeichen entfernen
        temp_text = re.sub(r'-\n', '', temp_text)
        temp_text = re.sub(r'\s+', ' ', temp_text) # mehrmalige Leerzeichen entfernen
        temp_text = re.sub(r"-\s+", "", temp_text)
        temp_text.strip()

        #data = [sent for sent in data if not self.is_noise(sent)]
        return data