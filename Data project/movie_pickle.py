import pickle

a = {'hello': 'world'}

with open('av_runtim.pickle', 'rb') as g:
    av_runtim = pickle.load(g)

print (av_runtim)

import matplotlib.pyplot as plt 

data = []
bins = len(av_runtim)      
for item in av_runtim:
    data.append(item)

# data = tuple(data)

# fig, ax = plt.subplots()
# means_men = (20, 35, 30, 35, 27)
# bar1_index = [0, 1, 2, 3, 4]
# rects1 = ax.bar(bar1_index, data, 0.35, color='b',  label='Men')
# label_tick = [0.175, 1.18, 2.18, 3.18, 4.18]

# ax.set_xlabel('Group')
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.set_xticks(label_tick)
# ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
# ax.legend()

# fig.tight_layout()
# plt.show()

plt.hist(data, bins, facecolor='b')
plt.xlabel('Years')
plt.ylabel('Average runtime')
plt.title('Average movie runtime by year')

#         x:0-100 y:0, (samples/bins) * 2.5 
plt.axis([0, 100, 0, 150])
plt.grid(True)
plt.show()