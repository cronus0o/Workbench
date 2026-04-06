import pandas as pd
import sqlite3
import streamlit as st
import folium
from streamlit_folium import st_folium
import re
import csv

# pip install openai 
# oenai migrate
from openai import OpenAI

# -------------------------------
# 팝업 챗봇용 스타일
# -------------------------------
st.markdown("""
    <style>
    .chat-popup {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 320px;
        background-color: #ffffff;
        border: 2px solid #ccc;
        border-radius: 12px;
        padding: 15px;
        z-index: 1000;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .chat-message {
        margin: 8px 0;
        padding: 8px 12px;
        border-radius: 10px;
        max-width: 100%;
    }
    .user-msg {
        background-color: #dbeafe;
        text-align: left;
    }
    .bot-msg {
        background-color: #fef3c7;
        text-align: left;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# DB 연결
# -------------------------------
conn = sqlite3.connect("reviews.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    restaurant TEXT,
    user TEXT,
    rating INTEGER,
    comment TEXT
)
""")
conn.commit()


# -------------------------------
# CSV 불러오기
# -------------------------------
df = pd.read_csv("ansung_restaurants_geocoded.csv")

# -------------------------------
# 상태 초기화
# -------------------------------
if "page_mode" not in st.session_state:
    st.session_state.page_mode = "지도"
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "전체"
if "selected_restaurant" not in st.session_state:
    st.session_state.selected_restaurant = None
if "show_chat" not in st.session_state:
    st.session_state.show_chat = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "add_shop" not in st.session_state:
    st.session_state.add_shop = "가게추가"

# -------------------------------
# 챗봇 로직
# -------------------------------
client = OpenAI(api_key="")
specific_data = pd.read_csv("ansung_restaurants_geocoded.csv")
def ai_reply(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"""
            너는 안성시의 맛집을 알려주는 인공지능 챗봇이야 {specific_data}
            """},
            {"role": "user", "content": text}
        ],
        max_tokens=200, # 데이터가 길어질 수 있는 경우 token 수 늘리기
        temperature=0.7
    )
    answer = response.choices[0].message.content.strip()
    return answer

# -------------------------------
# 챗봇 토글 버튼
# -------------------------------
if st.button("🤖 챗봇 열기/닫기"):
    st.session_state.show_chat = not st.session_state.show_chat

# -------------------------------
# 챗봇 팝업 렌더링
# -------------------------------
if st.session_state.show_chat:
    with st.container():
        st.markdown('<div class="chat-popup">', unsafe_allow_html=True)
        st.markdown("#### 🤖 기분 챗봇")
        with st.form("chat_form", clear_on_submit=True):
            msg = st.text_input("오늘 기분은?", key="chat_input_popup")
            submitted = st.form_submit_button("보내기")
            if submitted and msg:
                st.session_state.chat_history.append(("user", msg))
                ai_response = ai_reply(msg)
                st.session_state.chat_history.append(("bot", ai_response))
        for sender, text in st.session_state.chat_history[-6:]:
            role_class = "user-msg" if sender == "user" else "bot-msg"
            st.markdown(f'<div class="chat-message {role_class}">{text}</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# UI 시작
# -------------------------------
st.title("🍱 내리 맛집 안내 시스템")
search = st.text_input("🔍 맛집 검색", placeholder="가게명을 입력하세요")

# -------------------------------
# 카테고리 버튼
# -------------------------------
category_images = {
    "전체": "https://img.icons8.com/emoji/96/restaurant-emoji.png",
    "한식": "https://img.icons8.com/emoji/96/cooked-rice-emoji.png",
    "중식": "https://img.icons8.com/emoji/96/stuffed-flatbread-emoji.png",
    "양식": "https://img.icons8.com/emoji/96/pizza-emoji.png"
}
icon_map = {
    "한식": "🍚", "중식": "🍜", "양식": "🍕",
    "카페/디저트": "☕", "기타": "📍", "전체": "📍"
}
st.subheader("🍽️ 음식 종류 선택")
for cat, img in category_images.items():
    if st.button(f"{cat}", key=f"cat_{cat}"):
        st.session_state.selected_category = cat
        st.session_state.page_mode = "리스트"
        st.session_state.selected_restaurant = None
    st.markdown(f"<div style='text-align:center;'><img src='{img}' width='60'></div>", unsafe_allow_html=True)

# -------------------------------
# 지도 출력
# -------------------------------
if st.session_state.page_mode == "지도":
    st.subheader("📍 맛집 지도 보기")
    filtered_df = df.copy()
    if st.session_state.selected_category != "전체":
        filtered_df = filtered_df[filtered_df["category"] == st.session_state.selected_category]
    if search:
        filtered_df = filtered_df[filtered_df["name"].str.contains(search, case=False)]

    m = folium.Map(location=[36.99, 127.145], zoom_start=14)
    for _, row in filtered_df.iterrows():
        if pd.notnull(row["latitude"]) and pd.notnull(row["longitude"]):
            folium.Marker(
                [row["latitude"], row["longitude"]],
                tooltip=row["name"],
                popup=f"<b>{row['name']}</b><br>{row['road_address']}<br>{row['phone']}",
                icon=folium.DivIcon(html=f"<div style='font-size: 20px'>{icon_map.get(row['category'],'📍')}</div>")
            ).add_to(m)
    st_folium(m, width="100%", height=500)

# -------------------------------
# 리스트 페이지
# -------------------------------
elif st.session_state.page_mode == "리스트":
    st.subheader(f"📋 {st.session_state.selected_category} 맛집 리스트")
    filtered_df = df[df["category"] == st.session_state.selected_category]
    for name in filtered_df["name"]:
        if st.button(name, key=f"rest_{name}"):
            st.session_state.selected_restaurant = name

# -------------------------------
# 리뷰 보기
# -------------------------------
if st.session_state.page_mode == "리스트" and st.session_state.selected_restaurant:
    st.markdown(f"### ⭐ {st.session_state.selected_restaurant} 리뷰")
    cursor.execute("SELECT user, rating, comment FROM reviews WHERE restaurant = ?", 
                   (st.session_state.selected_restaurant,))
    rows = cursor.fetchall()
    if not rows:
        st.info("아직 리뷰가 없습니다.")
    for user, rating, comment in rows:
        st.markdown(f"- ⭐ {rating}점 by `{user}`: {comment}")
    if st.button("✍️ 리뷰 작성하기"):
        st.session_state.page_mode = "작성"

# -------------------------------
# 리뷰 작성
# -------------------------------
if st.session_state.page_mode == "작성":
    st.subheader(f"✍️ {st.session_state.selected_restaurant} 리뷰 작성")
    user = st.text_input("닉네임")
    rating = st.slider("별점", 1, 5)
    comment = st.text_area("리뷰")
    if st.button("저장"):
        cursor.execute("INSERT INTO reviews (restaurant, user, rating, comment) VALUES (?, ?, ?, ?)",
                       (st.session_state.selected_restaurant, user, rating, comment))
        conn.commit()
        st.success("리뷰가 저장되었습니다!")
        st.session_state.page_mode = "리스트"
    if st.button("⬅️ 돌아가기"):
        st.session_state.page_mode = "리스트"

# ———————————————
# 홈 버튼
# ———————————————
st.markdown("---")
if st.button("🏠 홈으로 돌아가기"):
    st.session_state.page_mode = "지도"
    st.session_state.selected_category = "전체"
    st.session_state.selected_restaurant = None
    st.session_state.chat_history = []
    st.session_state.show_chat = False


# -------------------------------
# 직접 장소 추가 기능
# -------------------------------

if st.session_state.add_shop :
    name = st.text_input("가게명")
    category = st.text_input("종류")
    address = st.text_input("주소")
    road_address = st.text_input("도로명주소")
    phone = st.text_input("전화번호")
    url = st.text_input("URL")
    latitude = st.text_input("위도")
    longitude = st.text_input("경도")
    menu = st.text_input("메뉴")


if st.button("가게추가"):
    # name,category,address,road_address,phone,url,latitude,longitude,menu
    csv_file = 'ansung_restaurants_geocoded.csv'
    with open(csv_file, 'a', newline = '') as csvfile :
        csv_writer = csv.writer(csvfile, delimiter = ',')
        new_restaurant = [name, category, address, road_address, phone, url, latitude, longitude, menu]
        csv_writer.writerow(new_restaurant)
