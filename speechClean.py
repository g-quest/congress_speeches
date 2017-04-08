f = open('responses.txt','r')
file = f.read()
f.close()

# convert text file into list of dicts similar to JSON format
responseList = eval(file)
type(responseList[0])

# get number of responses
len(responseList)

# get last names of each speaker
last_names = ['Response #{0}: {1}'.format(i + 1, response['speaker_last']) for i, response in enumerate(responseList)]
last_names

# show political affiliation of each name
for response in responseList:
    if response['speaker_last'] != None:
        if response['speaker_party'] == 'D':
            party = response['speaker_party'].replace('D','Democrat')
            print('Response #{0}: {1}, {2}'.format((int(responseList.index(response))+1), response['speaker_last'], party ))
        elif response['speaker_party'] == 'R':
            party = response['speaker_party'].replace('R','Republican')
            print('Response #{0}: {1}, {2}'.format((int(responseList.index(response))+1), response['speaker_last'], party ))
        else:
            print('Response #{0}: {1}, {2}'.format((int(responseList.index(response))+1), response['speaker_last'], response['speaker_party'] ))

# lengthy speeches are broken down into a list. clean up broken speeches for all responses and place in a 
# separate list
i = 0
speechList = [] #make a list of all the speeches cleaned
for response in responseList:
    newSpeech = " ".join(responseList[i]['speaking'])
    i = i + 1
    speechList.append('Speech from Response #{0}: {1}'.format(i, newSpeech,))

# show the list of speeches
speechList 

# get the number of words for each speech
wordCountList = ['Speech from response #{0}: {1} words'.format(i + 1, len(response.split())) for i, response in enumerate(speechList)]
wordCountList 

# use regular expressions to show responses whose title includes the word "ACT", i.e. a response that involves
# the introduction of a bill
import re
for response in responseList:
    found = re.search(r'\bACT\b',response['title'])
    if found:
        print('Response #{0}: {1}'.format((int(responseList.index(response))+1), response['title']))

