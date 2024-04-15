# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:13:40 2024

@author: jcp
"""
# 3. 데이터 시각화
def visualize():
    import pandas as pd
    # 엑셀 파일 읽어오기
    selected_pp = pd.read_excel('./data/selected_pp.xlsx')
    pp_all = pd.read_excel('./data/pp_all.xlsx')

    selected_d = pd.read_excel('./data/selected_d.xlsx')
    d_all = pd.read_excel('./data/d_all.xlsx')
    
    # 상위 20개
    top20_selected = selected_d[:20]
    top20 = d_all[:20]
    
    from module import wc
    from module import bar_wc as bw

    # 불용어 제거 후
    bw.bar_wordcount(top20_selected, './img/selected_d')
    bw.barh_wordcount(top20_selected, './img/selected_d')

    wc.make_wordcloud(top20_selected, './img/selected_d')
    wc.make_img_wordcloud(top20_selected, './img/selected_d', './module/bird.png')

    bw.bar_wordcount(top20, './img/speeches_d')
    bw.barh_wordcount(top20, './img/speeches_d')

    wc.make_wordcloud(top20, './img/speeches_d')
    wc.make_img_wordcloud(top20, './img/speeches_d', './module/bird.png')
    
    # 불용어 제거 안한 것
    bw.bar_wordcount(selected_pp[:20], './img/selected')
    bw.barh_wordcount(selected_pp[:20], './img/selected')

    wc.make_wordcloud(selected_pp[:20], './img/selected')
    wc.make_img_wordcloud(selected_pp[:20], './img/selected', './module/bird.png')

    bw.bar_wordcount(pp_all[:20], './img/speeches')
    bw.barh_wordcount(pp_all[:20], './img/speeches')

    wc.make_wordcloud(pp_all[:20], './img/speeches')
    wc.make_img_wordcloud(pp_all[:20], './img/speeches', './module/bird.png')

# %%
