# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:58:05 2024

@author: jcp
"""


from wordcloud import WordCloud # 워드클라우드 제작 라이브러리
import pandas as pd # 데이터 프레임 라이브러리
import numpy as np # 행렬 라이브러리
import matplotlib.pyplot as plt # 워드클라우드 시각화 라이브러리

df = pd.read_csv('한산_댓글모음.csv')
df

# %%
df['Review'] = df['Review'].str.replace('[^가-힣]', ' ', regex = True)
df['Review']

# %%
import konlpy
kkma = konlpy.tag.Kkma() #형태소 분석기 꼬꼬마(Kkma)

nouns = df['Review'].apply(kkma.nouns)
nouns

# %%
# 5. 단어 데이터프레임 만들기
nouns = nouns.explode()
nouns

# %%
# 두 글자 이상만
df_word = pd.DataFrame({'word' : nouns})
df_word['count'] = df_word['word'].str.len()
df_word = df_word.query('count >= 2')
df_word

# %%
df_word = df_word.groupby('word', as_index = False).count().sort_values('count', ascending = False)
df_word

# %%

# 영화처럼 불필요한 단어 제거
df_word = df_word.iloc[1:, :]
df_word.head(5)

# %%
# 6.  워드클라우드 만들기
#  - 전처리 과정이 귀찮았습니다. 또한, 워드클라우드는 Java 등 갖가지 문제점이 발생합니다. 버전 등을 잘 확인해주셔야 합니다.
#  - 데이터 프레임을 딕셔너리 형태로 변환해주셔야 합니다.


# %%
def make_wordcloud(df):
    # df를 dict로 변환
    dic_word = df_word.set_index('word').to_dict()['count']
    dic_word
    # 워드클라우드 객체 생성
    wc = WordCloud(random_state = 123, font_path = './NanumBarunGothic.ttf', width = 400,
                   height = 400, background_color = 'white')

    img_wordcloud = wc.generate_from_frequencies(dic_word)

    plt.figure(figsize = (10, 10)) # 크기 지정하기
    plt.axis('off') # 축 없애기
    plt.imshow(img_wordcloud) # 결과 보여주기
    plt.savefig('워드클라우드') # 파일 저장
    
# %%
make_wordcloud(df_word)

# %%
import PIL
icon = PIL.Image.open('cloud2.png')

img = PIL.Image.new('RGB', icon.size, (255,255,255))
img.paste(icon, icon)
img = np.array(img)
