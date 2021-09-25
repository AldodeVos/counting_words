import csv
import string

text_file = 'books.txt'
the_text = ''
different_words = []
individual_word_counts = []
total_word_count = 0
delete_list = []

#load file 
f = open(text_file, 'r', encoding='utf8')
the_text = f.read().translate(str.maketrans('', '', string.punctuation)).lower().split()
f.close()


#Reduce text to unique words only, and count how many times each word existed
for count1, value1 in enumerate(the_text):
    delete_list = []
    try:
        individual_word_counts[count1] += 1
    except:
        individual_word_counts.append(1)
    for count2, value2 in enumerate(the_text[count1+1:]):
        if value2 == value1:
            delete_list.append(count2+count1+1)
            try:
                individual_word_counts[count1] += 1
            except:
                individual_word_counts.append(1)
    for count3, value3 in enumerate(delete_list):
        try:
            del the_text[value3-count3]
        except:
            print('something went wrong at {0}. The text is only {1} words long'.format(count3,len(the_text)))

#export data to a .csv file

data_file = open('word data for {0}.csv'.format(text_file), 'a', newline='')
writer = csv.writer(data_file)

for count4, value4 in enumerate(the_text):
    writer.writerow([the_text[count4], individual_word_counts[count4]])





quit()


