# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:19:15 2024

@author: YS702
"""

import streamlit as st


st.title("[분전팀], 대통령 연설문 분석, 2002~2020년 북한 주요도발 사건을 중심으로")

st.sidebar.title("메뉴")
selected_page = st.sidebar.radio("페이지 선택", ["홈으로", "대통령", "지도", "날짜","사건명"])

if selected_page == "홈으로":
    st.write("이곳은 홈입니다.")
    st.subheader("- 홈으로: 홈으로 이동합니다.")
    st.subheader("- 대통령: 대통령을 기준으로 정보를 나눕니다.")
    st.subheader("- 지도: 지도를 기준으로 사건을 나눕니다.")
    st.subheader("- 날짜: 날짜를 기준으로 사건을 나눕니다")
    st.subheader("- 사건명: 사건명을 기준으로 사건을 나눕니다")
elif selected_page == "대통령":
    st.write("이곳은 대통령 페이지입니다.")
    st.sidebar.subheader("대통령 하위 페이지")
    selected_subpage = st.sidebar.radio("하위 페이지 선택", ["서브페이지1", "서브페이지2","서브페이지3", "서브페이지4", "서브페이지5"])
    if selected_subpage == "서브페이지1":
        st.write("대통령의 서브페이지1입니다.")
    elif selected_subpage == "서브페이지2":
        st.write("대통령의 서브페이지2입니다.")
    elif selected_subpage == "서브페이지3":
        st.write("대통령의 서브페이지3입니다.")
    elif selected_subpage == "서브페이지4":
        st.write("대통령의 서브페이지4입니다.")
    elif selected_subpage == "서브페이지5":
        st.write("대통령의 서브페이지5입니다.")

elif selected_page == "지도":
    st.write("이곳은 지도 페이지입니다.")
elif selected_page == "날짜":
    st.write("이곳은 날짜 페이지입니다.")
elif selected_page == "사건명":
    st.write("이곳은 사건명 페이지입니다.")
    

