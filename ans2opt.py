import json
import os
import sys

from difflib import SequenceMatcher


filepath = 'out/basic/00/answer/test-010000.json'
datapath = '../data/squad/test.json'

with open(filepath) as f:
    answer = json.load(f)

with open(datapath) as f:
    data = json.load(f)

print('Answer: {:5d}'.format(len(answer)))
print('Data: {:7d}'.format(len(data)))

#sys.stdout = open("missing_qs.txt","w")

def select_ans(ans, opts):
    scores = [0, 0, 0, 0]
    ans = ans.lower()
    for i,opt in enumerate(opts):
        if ans == opt: return i
        words = [x.lower() for x in opt.split()]
        for w in words:
            if w in ans:
                scores[i] += 1
            else:
                scores[i] -= 1

    #print (scores)
    return scores.index(max(scores))

def run():
    count = 0
    for d in data:
        found = False
        true_q = d['question']
        #words = true_q.split()
        for q in answer.keys():
            """
            precessed_q = q.replace(' ?', '?')
            precessed_q = precessed_q.replace(' \'', '\'')
            precessed_q = precessed_q.replace(' ,', ',')
            precessed_q = precessed_q.replace(' & ', '&')
            """
            #q_words = q.split()
            #if words[0] == q_words[0]:
            #    score = SequenceMatcher(None, true_q, q).real_quick_ratio()
            if true_q == q:
                idx = select_ans(answer[q], d['answer_list'])
                count += 1
                found = True
                yield idx
                break
        if found is False:
            yield 0
    print (count)

res = 0
with open('answer.txt', 'w+') as f:
    #for x, y in run():
    for x in run():
        #if x == y:
        #    res += 1
        #print ('for')
        #print (x)
        f.write('{:d}\n'.format(x))


#for x in run():
#    print(x)

#print('acc: {:f}'.format(res / len(answer.keys())))

#sys.stdout.close()
