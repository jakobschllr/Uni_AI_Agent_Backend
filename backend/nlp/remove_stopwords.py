

def remove_stopwords(data):
    stopwords_set = set()
    words = data.split(" ")
    with open("/Users/jakobschiller/Desktop/Projekte/AI_Uni_Quiz/nlp/stopwords_de.txt", "r") as stopwords:
        stopwords_set = set(line.strip().lower() for line in stopwords)

    words = data.split(" ")
    print(words)
    return [word for word in words if word.lower() not in stopwords_set]