n=int(input())
word_list=[]
word_dict={}
for 1 in range(n):
    word=input()
    if word not in word_dict:
        word_list.append(word)
    word_dict[word]=word_dict.get(word,0)
print(len(word_list))
for word in word_list:
    print(word_dict[word],end=' ')
