import matplotlib.pyplot as plt

word_count = {}
with open("C:/Users/88692/Downloads/hw2_data.txt", "r", encoding="utf-8") as file:
    for line in file:
        word = line.strip()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

unique_word_count = len(word_count)
print(f"不重複的英文字數量: {unique_word_count}")
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print("\n各單字出現次數（由多到少）：")
for word, count in sorted_word_count:
    print(f"{word}: {count}")

words, counts = zip(*sorted_word_count)

# 使用 matplotlib 繪製直方圖
plt.figure(figsize=(12, 6))
plt.bar(words, counts, color='skyblue')
plt.xlabel("word", fontsize=12)
plt.ylabel("count", fontsize=12)
plt.title("all word", fontsize=14)
plt.xticks(rotation=90, fontsize=8)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
