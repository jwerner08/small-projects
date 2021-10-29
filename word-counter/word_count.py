import sys
import string

def Word_count():
    words = {}
    strip = string.whitespace + string.punctuation + string.digits + "\"'"
    stopwords = []
    stopwordsrep = []
    
    with open('stopwords.txt', 'r') as f:
        for stopwordi in f:
            stopwords.append(stopwordi)
    f.close()
    for stopwordrep in stopwords:
        stopwordsrep.append(stopwordrep.replace("\n", ""))

    try:
        text_file = sys.argv[1]
        while text_file[-4:] != '.txt':
            text_file = input('Copy/paste the name of the text file within this directory. \nPlease include the extension ".txt": ')
    except IndexError:
        text_file = ''
        while text_file[-4:] != '.txt':
            text_file = input('Copy/paste the name of the text file within this directory. \nPlease include the extension ".txt": ')
    with open(text_file, 'r') as f:
        for line in f:
            for word in line.lower().split():
                word = word.strip(strip)
            if len(word) > 2 and word not in stopwordsrep:
                words[word] = words.get(word, 0) + 1
    f.close()
    sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
    for i in range(10):
        print('"' + sorted_words[i][0] + '"', 'occured', sorted_words[i][1], "times.")


if __name__ == '__main__':
    Word_count()
