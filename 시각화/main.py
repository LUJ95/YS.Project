# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:51:39 2024

@author: jcp
"""

# 1. 데이터 수집
selected = []
selected += list(range(1309257,1309263)) # 연평해전 : 1309257~1309262
selected += [1310208, 1310209] # 금강산 관광객 피살 : 1310208~1310209
selected += [1330395, 1330298] # 천안함 피격 : 1330395, 1330298
selected += [1330411] # 연평도 포격 : 1330411
selected += [1400325,1400326,1400327] # 목함지뢰 : 1400325,1400326,1400327
selected += [1400332] # 서부전선 포격사건 : 1400332
selected += list(range(1401215, 1401218))+[1401939, 1401940] # 연락망 폭파 사건 : 1401939, 1401216, 1401215, 1401940, 1401217
selected += [1401955] + list(range(1401258, 1401264)) # 공무원 피살 사건 : 1401955, 1401258~1401263

# %%
# 대통령별 게시물id [시작, 끝]
kim = [1308526, 1309346]
roh = [1309348, 1310126]
lee = [1330066, 1331000]
lee2 = [1310127, 1310336]
park = [1400001, 1400493]
moon = [1400600, 1402000]
all_president = [kim, roh, lee, lee2, park, moon]
# %%
# 전처리 불가 특수첨자 사용된 게시물id
error = [1330443, 1330504]
# %%
lst = list(range(moon[0],moon[1]+1))
lst[-1]
# %%
import sps

selected_speeches = []
speeches = []
speeches_list = []
speeches_all = []
k = 0

for president in all_president:
    
    for idn in range(president[0], president[1] + 1):
        
        speech = sps.scrape_presidential_speech(idn)
        
        if len(speech) > 0:   
            if idn in selected:
                selected_speeches.append(speech)
            else:
                speeches.append(speech)
                speeches_all.append(speech)
                k += 1
            if (k > 0 and k % 100 == 0):
                speeches_list.append(speeches)
                speeches = []
                
        if idn == all_president[-1][-1]:
            speeches_list.append(speeches)
            print('크롤링이 종료되었습니다.')
            print('마지막 artid: ')
            print(idn)
            
            
# %%

import pandas as pd
df_selected = pd.DataFrame({"연설문": selected_speeches})

df_list = []
# 연설문 전체를 데이터프레임 리스트로 변환, excel파일로 저장
i = 1
for speeches in speeches_list:
    df_speeches = pd.DataFrame({'연설문':speeches})
    df_list.append(df_speeches)
    df_speeches.to_excel('speeches{}.xlsx'.format(i), index=False)
    i += 1
    
df_selected.to_excel('selected_speeches.xlsx', index=False)

#%%
# 2. 데이터 정제
import pp
selected_pp = pp.preprocess(df_selected)

# %%
pp_list = []

# %%
for speeches in df_list:
    pp_list.append(pp.preprocess(speeches))


# %%
# 연설문 전체 합치는 부분(미완)
# pp_sum = pd.DataFrame()
# for pp_speeches in pp_list:
#     if pp_speeches == pp_list[0]:
#         pp_sum = pp_speeches
#     else:
#         pp_sum.groupby('word')


# %%
# 3. 데이터 시각화
import wc
import bar_wc as bw

# 
bw.bar_wordcount(selected_pp, 'selected')
bw.barh_wordcount(selected_pp, 'selected')

wc.make_wordcloud(selected_pp, 'selected')
wc.make_img_wordcloud(selected_pp, 'selected', 'bird.png')

bw.bar_wordcount(speeches_pp, 'speeches')
bw.barh_wordcount(speeches_pp, 'speeches')

wc.make_wordcloud(speeches_pp, 'speeches')
wc.make_img_wordcloud(speeches_pp, 'speeches', 'bird.png')

# %%