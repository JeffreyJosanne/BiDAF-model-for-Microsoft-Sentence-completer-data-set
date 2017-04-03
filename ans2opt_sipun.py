import json
import os
import sys

from difflib import SequenceMatcher


filepath = 'out/basic/00/answer/test-018000_10pm.json'
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
    idx = 0
    for d in data:
        found = False
        true_q = d['question']
        #words = true_q.split()
        key = str(idx)
        ans_idx = select_ans(answer[key], d['answer_list'])
        yield ans_idx
        idx += 1
    print (idx)


res = 0
with open('answer.txt', 'w+') as f:
    for x in run():
        #print ('for')
        #print (x)
        f.write('{:d}\n'.format(x))


#print('acc: {:f}'.format(res / len(answer.keys())))

#sys.stdout.close()
