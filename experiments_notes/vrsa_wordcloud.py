
'''
# save mask to alice_mask
alice_mask = np.array(Image.open('alice_mask.png'))

alice_novel = open('alice_novel.txt', 'r').read()

stopwords = set(STOPWORDS)
print(stopwords)

stopwords.add('said') # add the words said to stopwords

# instantiate a word cloud object
alice_wc = WordCloud(
    background_color='white',
    max_words=2000,
    stopwords=stopwords,
    mask=alice_mask
)

# generate the word cloud
alice_wc.generate(alice_novel)

# display the word cloud
plt.imshow(alice_wc, interpolation='bilinear')
plt.axis('off')
plt.show()

fig = plt.figure()
fig.set_figwidth(14) # set width
fig.set_figheight(18) # set height

# display the cloud
plt.imshow(alice_wc, interpolation='bilinear')
plt.axis('off')
plt.show()

fig = plt.figure()
fig.set_figwidth(14) # set width
fig.set_figheight(18) # set height

plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()
alice_wc.to_file('alice.png')

'''

# just for collecting words of the text, not for word cloud
import collections
from wordcloud import WordCloud
#for English texts:
#from wordcloud import WordCloud, STOPWORDS
import matplotlib.pylab as plt
import numpy as np
from PIL import Image

# open the input file
vrsa = open('/home/csaba/indology/dharma_project/vrsa_edition/text_version_of_vrsa_split.txt', 'r', encoding="utf8").read()

# to produce an ordinary dictionary of each word:
vrsa_coll_list = collections.Counter(vrsa.replace("\n", " ").split(" "))
max_occurance = max(vrsa_coll_list.values())
m = max_occurance
while m > 0:
    for k in vrsa_coll_list:
        if vrsa_coll_list[k] == m:
            print(k, vrsa_coll_list[k])
    m = m - 1


#for English texts:
#stopwords = set(STOPWORDS)

# I want to exclude trivial words. It is a work in progress...
stopwords = ['ca', 'vā', 'eva', 'na', 'sa', 'vai', 'tatra', 'bhavet',
        'tasya', 'tathā', 'tu', 'tv', 'uvāca' 'tataḥ', 'tato', 'yasya', 'caiva', 'te', 'hi', 'ucyate',
        'taṃ', 'mama'] 


# generate WordCloud instance:
vrsa_wc = WordCloud(
    ## font for Roman: 
    font_path='/usr/share/fonts/opentype/linux-libertine/LinLibertine_R.otf',
    ## font for Devanāgarī:
    #font_path='/usr/share/fonts/truetype/Gargi/Gargi.ttf',
    background_color='white',
    ## to limit the number of words:
    #max_words=2000,
    ## list of words to exclude:
    stopwords=stopwords,
    ## image to fit the words into:
    #mask=alice_mask
    # dimensions of the output image:
    width=800, height=400
)

# generate image:
vrsa_wc.generate(vrsa)
# generate 'plot':
plt.imshow(vrsa_wc, interpolation='bilinear')
plt.axis('off')
plt.show()




