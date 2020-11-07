from __future__ import division
import csv
from string import punctuation
# import matplotlib.pyplot as plt

positive_word = []
negative_word = []
netral_word = []
positive_counts = []
negative_counts = []
netral_counts = []
clean_tweets = []
header = [("Tweets", "Positive", "Negative", "Positive %", "Negative %", "Netral %")]

tweets = open("mercubuana.csv").read()
tweets_list = tweets.split('\n')

pos_sent = open("source/positive.txt").read()
positive_words = pos_sent.split('\n')

neg_sent = open("source/negative.txt").read()
negative_words = neg_sent.split('\n')

for tweet in tweets_list:
    text_positive = []
    text_negative = []
    text_netral = []
    positive_counter = 0
    negative_counter = 0
    netral_counter = 0
    tweet_procces_2 = tweet.replace('!', '').replace('.', '')
    tweet_processed = tweet_procces_2.lower()

    for p in list(punctuation):
        tweet_processed = tweet_processed.replace(p, '')

    clean_tweets.append(tweet_processed)

    words = tweet_processed.split(' ')
    word_count = len(words)
    for word in words:
        if word in positive_words:
            text_positive.append(word)
            positive_counter = positive_counter + 1
        elif word in negative_words:
            text_negative.append(word)
            negative_counter = negative_counter + 1
        else:
            text_netral.append(word)
            netral_counter = netral_counter + 1

    positive_counts.append((positive_counter / word_count) * 100)
    negative_counts.append((negative_counter / word_count) * 100)
    netral_counts.append(netral_counter)
    positive_word.append(text_positive)
    negative_word.append(text_negative)
    netral_word.append(text_netral)

output = zip(clean_tweets, positive_word, negative_word, positive_counts, negative_counts, netral_counts)
title = header
writer = csv.writer(open('source/result_sentiment.csv', 'w'))
writer.writerows(title)
writer.writerows(output)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Positive', 'Negative', 'Netral'
# sizes = [positive_counts, negative_counts, netral_counts]
# fig, ax = plt.subplots()
# ax.pie(sizes, labels=labels, autopct='%1.1f%%')
# ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
# ax.set_title('Engineering Diciplines')
#
# plt.show()
