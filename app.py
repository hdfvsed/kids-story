import streamlit as st
import google.generativeai as genai

# 1. 앱 설정
st.set_page_config(page_title="우리 아이 단어 동화 만들기", page_icon="📖")

# 2. 제미나이 API 설정
# [중요] 아래 큰따옴표 안에 복사 버튼으로 가져온 전체 키를 붙여넣으세요!
API_KEY = "AIzaSyDp1KqI7AQxlmh56Wq6dRbtoPB3blbkKeA" 

try:
    genai.configure(api_key=API_KEY)
    # 최신 모델인 gemini-1.5-flash를 사용하여 더 빠르게 생성합니다.
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("API 설정 중 오류가 발생했습니다. 키를 다시 확인해주세요.")

# 3. 기초 어휘 리스트 (학령전기 500개 중 샘플)
VOCAB_LIST = [
    "사과", "바나나", "강아지", "고양이", "기차", "우유", "포도", "딸기", "토끼", "사자",
    "코끼리", "자동차", "비행기", "자전거", "학교", "선생님", "친구", "동생", "안경", "모자",
    "해", "달", "별", "구름", "꽃", "나무", "나비", "공", "인형", "로봇"
]

# 4. UI 구성
st.title("📖 단어로 만드는 마법 동화")
st.write("아이와 함께 단어를 골라보세요. 멋진 이야기가 만들어집니다!")

selected_words = st.multiselect(
    "이야기에 넣고 싶은 단어를 골라주세요 (최대 3개):",
    options=VOCAB_LIST,
    max_selections=3
)

mood = st.radio("동화의 분위기를 골라주세요:", ["재미있는", "감동적인", "모험이 가득한"], horizontal=True)

# 5. 동화 생성
if st.button("✨ 동화 만들기"):
    if not selected_words:
        st.warning("단어를 선택해주세요!")
    elif API_KEY == "여기에_복사한_키를_붙여넣으세요":
        st.error("코드를 수정하여 실제 API 키를 입력해주셔야 합니다.")
    else:
        with st.spinner("AI 작가가 이야기를 짓고 있어요..."):
            try:
                prompt = f"""
                너는 아동 문학 작가야. 학령전기 아동이 이해하기 쉬운 단어를 사용해줘.
                조건:
                1. 포함 단어: {', '.join(selected_words)}
                2. 분위기: {mood}
                3. 길이: 5문장 내외의 아주 짧은 동화
                4. 마지막에는 아이에게 질문을 하나 던져줘.
                """
                response = model.generate_content(prompt)
                
                st.success("동화 완성!")
                st.markdown("---")
                st.subheader("우리 아이를 위한 마법 이야기")
                st.write(response.text)
                st.markdown("---")
                st.balloons()
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")

st.caption("이 앱은 학령전기 기초 어휘를 바탕으로 AI가 이야기를 생성합니다.")        
st.warning("단어를 최소 하나 이상 골라주세요!")
    else:
        with st.spinner("제미나이가 이야기를 짓고 있어요..."):
            try:
                # 프롬프트 구성 (바이브 코딩의 핵심: LLM에게 명확한 역할 부여)
                prompt = f"""
                너는 아동 문학 작가야. 학령전기 아동이 이해하기 쉬운 단어와 문장을 사용해줘.
                다음 조건을 지켜서 짧은 동화를 지어줘:
                1. 포함될 단어: {', '.join(selected_words)}
                2. 분위기: {mood}
                3. 길이: 5문장 내외
                4. 마지막에는 아이에게 질문을 하나 던져줘.
                """
                
                response = model.generate_content(prompt)
                
                # 결과 출력
                st.success("동화가 완성되었습니다!")
                st.markdown("---")
                st.subheader(f"제목: {selected_words[0]}와(과) 친구들의 이야기")
                st.write(response.text)
                st.markdown("---")
                
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
                st.info("API 키가 정확한지, 혹은 사용량이 초과되지 않았는지 확인해주세요.")

# 하단 정보
st.caption("이 앱은 학령전기 기초 어휘를 바탕으로 AI가 이야기를 생성합니다.")
