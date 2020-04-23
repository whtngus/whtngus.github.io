import re
import collections


def file_load(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        # for line in f:
        #     yield line
        lines = f.readlines()
        f.close()
        return lines


def file_write(line,file_stream, file_path=None):
    if file_path != None:
        return open(file_path, "w", encoding="utf-8")
    file_stream.write(line)

# q1
write_file_path = "./q1.txt"
load_file_path = "./4300-0.txt"
file_stream = file_write(None, None, write_file_path)
for line in file_load(load_file_path):
    line = line.strip()
    if line == "" or line == '﻿':
        continue
    file_write(line + "\n", file_stream)
file_stream.close()
# q2
write_file_path = "./q2.txt"
load_file_path = "./q1.txt"

file_stream = file_write(None, None, write_file_path)
for line in file_load(load_file_path):
    text = re.sub('[—‘.,?]', '', line)
    text = re.sub('[ ]{2,}', ' ', text)
    if text == "\n":
        continue
    file_write(text,file_stream)

# q3

write_file_path = "./q3.txt"
load_file_path = "./q2.txt"
file_stream.close()
file_stream = file_write(None, None,write_file_path)
for line in file_load(load_file_path):
    file_write(line.replace("Mooney", "Simon."),file_stream)
file_stream.close()
# q4 and 5
load_file_path = "./q3.txt"
unigram_count = collections.Counter()
Egypt_count = 0
text_history = []
for line in file_load(load_file_path):
    Egypt_count += line.count("Egypt")
    text_history += line.split()
unigram_count = collections.Counter(text_history)
print("q4 - How many times does “Egypt” occur ? : {}\n".format(Egypt_count))
print("q5.1 - What are the top 20 most frequently occurred words? Provide eachword with its count? : {}\n".format(
    unigram_count.most_common(20)))
print("q5.2 -  Provide 5 words with frequency =2")
frequncy_2_word = 5
for k,v in unigram_count.items():
    if v != 2:
        continue
    frequncy_2_word-=1
    print("{} - {}".format(k,v))
    if frequncy_2_word == 0:
        break

# Ex6. Build a bigram model.
def input_bigram(keyword_1, keyword_2):
    if keyword_1 in bigram:
        kv_dict = bigram[keyword_1]
        if keyword_2 in kv_dict:
            kv_dict[keyword_2] += 1
        else:
            kv_dict[keyword_2] = 1
    else:
        bigram[keyword_1] = {keyword_2: 1}

    token = keyword_1 + " " + keyword_2
    if token in bigram_count:
        bigram_count[token] += 1
    else:
        bigram_count[token] = 1

bigram = {}
bigram_count = {}
for line in file_load(load_file_path):
    tokens = line.strip().split()
    input_bigram("-BOS-", tokens[0])
    input_bigram(tokens[-1], "-EOS-")
    for i, word in enumerate(tokens[:-1]):
        input_bigram(word, tokens[i + 1])

print("q6.1 - What are the top 20 most frequently occurred two-word sequence? \n Provide each three-word sequence with its count.")
print("result : {}\n".format(sorted(bigram_count.items(),key=lambda x:x[1],reverse=True)[:20]))

print('q6.2 - Compute Count(in the), Count(in)')
print("Compute Count(in the) : {}".format(bigram_count["in the"]))
print("Count(in) : {}\n".format(unigram_count["in"]))

print("q6.3 -  Calculate P( the | in)? ")
print(" Calculate P( the | in)? : {}\n".format(bigram_count["in the"]/unigram_count["in"]))

print("q6.4 - What is the mostly frequently occurred word “X” after the word“same”, argmax( X | same ) ?")
max_value = sorted(bigram["same"].items() , key=lambda x:x[1],reverse=True)[1] # 1 eq -EOS-
print(" X is  {}, p({}|same) = {}\n".format(max_value[0],max_value[0],max_value[1]/unigram_count["same"]))

# 7. Build a trigram model.
def input_total_count(dict):
    total_name = "total count"
    if total_name in dict:
        dict[total_name] += 1
    else:
        dict[total_name] = 1

def input_trigram(keyword_1, keyword_2, keyword_3):
    if keyword_1 in trigram:
        kv_dict = trigram[keyword_1]
        if keyword_2 in kv_dict:
            kv_dict = kv_dict[keyword_2]
            if keyword_3 in kv_dict:
                kv_dict[keyword_3] += 1
            else:
                kv_dict[keyword_3] = 1
        else:
            kv_dict[keyword_2] = {keyword_3 : 1}
    else:
        trigram[keyword_1] = {keyword_2: {keyword_3: 1}}
    input_total_count(trigram[keyword_1])
    input_total_count(trigram[keyword_1][keyword_2])

    token = keyword_1 + " " + keyword_2 + " " + keyword_3
    if token in trigram_count:
        trigram_count[token] += 1
    else:
        trigram_count[token] = 1



trigram = {}
trigram_count = {}
for line in file_load(load_file_path):
    line = line.strip().split()
    if len(line) < 3:
        continue
    input_trigram("-BOS-", line[0],line[1])
    input_trigram(line[-2], line[-1], "-EOS-")
    for i, word in enumerate(line[:-2]):
        input_trigram(word, line[i + 1],line[i+2])

print("7.1 -  What are the top 20 most frequently occurred two-word sequence?")
print("Provide each three-word sequence with its count.")
print("\n".join([word + "\t" + str(count) for word, count in sorted(trigram_count.items(), key = lambda x : x[1],reverse=True)[:20]]))

print("7.2 - Compute P(morning | in the) ? ")
print("P(morning | in the) = {}".format(trigram_count["in the morning"]/trigram["in"]["the"]["total count"]))
