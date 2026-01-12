import streamlit as st

st.title("🎈요리왕통깨 앱!! ")

st.write(
    "야호, 오예"
)
st.write(
    "첫번째 앱을 만들어 봅시다"
)
st.markdown("---")

import streamlit as st
import pandas as pd

st.title("1️⃣ ✅ 공개 Google Sheet 읽기")
st.info("📘 누구나 볼 수 있도록 공개된 시트를 Pandas로 직접 불러오는 가장 간단한 방법입니다.\n📎 링크는 반드시 `export?format=csv` 형태로 설정하세요.")

csv_url1 = "https://docs.google.com/spreadsheets/d/1VC_q8HJfIufjGVR2zGRcJjBgkefIbp6Pv01rQ1uvoXI/export?format=csv"
df1 = pd.read_csv(csv_url1)
st.dataframe(df1['choice'])

# choice 컬럼이 있는 경우 종류별로 집계해서 막대그래프로 출력
if 'choice' in df1.columns:
    choice_counts = df1['choice'].value_counts()
    st.subheader("choice 종류별 분포")
    st.dataframe(choice_counts.rename_axis('choice').reset_index(name='count'))
    st.bar_chart(choice_counts)
else:
    st.warning("'choice' 컬럼이 시트에 없습니다.")


st.markdown("---")


# 정보성 메시지 박스
st.info("ℹ️ 정보 메시지입니다.")
st.warning("⚠️ 경고 메시지입니다.")
st.success("✅ 성공 메시지입니다.")
st.error("❌ 오류 메시지입니다.")

import pandas as pd
import numpy as np

# 샘플 데이터프레임 생성
np.random.seed(42)
df = pd.DataFrame({
    "날짜": pd.date_range("2024-01-01", periods=30),
    "매출": np.random.randint(100, 300, size=30),
    "방문자수": np.random.randint(50, 150, size=30)
})
st.dataframe(df)


# 이미지 출력
st.image("https://m.health.chosun.com/site/data/img_dir/2024/11/08/2024110802000_0.jpg", caption="예시 이미지")

# 지도 출력
import pandas as pd
df = pd.DataFrame({"lat": [37.5], "lon": [127.0]})
st.map(df, zoom=12)

# 데이터프레임 테이블 출력
st.dataframe(pd.DataFrame({
    "이름": ["홍길동", "김철수"],
    "점수": [85, 92]
}))




