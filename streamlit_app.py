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
st.dataframe(df1)
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

st.image("sample.png")

st.markdown("---")
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# ----------------------------------------------------------------
# 1. 페이지 설정
# ----------------------------------------------------------------
st.set_page_config(page_title="넌센스 퀴즈 배틀", page_icon="🤪")
st.title("🤪 뇌풀기 넌센스 퀴즈")
st.markdown("센스 있는 사람만 맞힐 수 있는 **넌센스 퀴즈**입니다!")

# ----------------------------------------------------------------
# 2. 데이터 연결 (제공해주신 새 링크 자동 연결)
# ----------------------------------------------------------------
conn = st.connection("gsheets", type=GSheetsConnection)


try:
    # secrets.toml의 링크를 가져옵니다.
    url = st.secrets["connections"]["gsheets"]["public_url"]
    
    # 캐시 없이 즉시 로딩 (ttl=0)
    df = conn.read(spreadsheet=url, ttl=0)

except Exception as e:
    st.error("🚨 시트 연결 실패! secrets.toml에 링크를 정확히 넣었는지 확인하세요.")
    st.stop()


# ----------------------------------------------------------------
# 3. 퀴즈 로직
# ----------------------------------------------------------------
# 'is_active'가 TRUE인 것만 가져오기
active_rows = df[df["is_active"] == True]

if active_rows.empty:
    st.warning("🥲 현재 오픈된 퀴즈가 없습니다. (관리자가 문제를 출제 중입니다)")
else:
    # 진행률 표시줄 (있어 보임)
    st.progress(len(active_rows) / 10, text=f"총 {len(active_rows)}개의 문제가 준비되었습니다.")
    st.divider()

    for i, row in active_rows.iterrows():
        st.subheader(f"Q{i+1}. {row['question_text']}")

        # 보기 옵션 가져오기
        options = [row[col] for col in df.columns if col.startswith("opt_") and pd.notna(row[col])]

        # 정답 입력
        user_choice = st.radio(
            "정답은?", 
            options, 
            key=f"quiz_{row['question_id']}", 
            index=None
        )

        # 정답 확인 버튼
        if st.button("정답 확인", key=f"btn_{row['question_id']}"):
            if user_choice == row["answer"]:
                st.balloons()
                st.success(f"🎉 정답입니다! ({row['answer']})")
            else:
                st.error("💥 땡! 다시 생각해보세요.")
        
        st.divider()

# ----------------------------------------------------------------
# 4. 마무리 멘트 (숨겨진 문제 유도)
# ----------------------------------------------------------------
st.caption("문제가 더 보고 싶나요? 구글 시트에서 'is_active'를 켜보세요!")




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




