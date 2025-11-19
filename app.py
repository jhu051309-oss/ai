import streamlit as st
from openai import OpenAI
import os

# 🔐 환경변수에서 API 키 불러오기
# 터미널에서 아래처럼 설정해야 함:
# export OPENAI_API_KEY="your_api_key"
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OPENAI_API_KEY 환경변수가 설정되어 있지 않습니다.")
else:
    client = OpenAI(api_key=api_key)

    st.title('단위 변환기')

    # 사용자 입력
    substance = st.text_input("단위를 변환하는 물질:")
    number = st.text_input("물질의 수:")
    first_unit = st.text_input("주어진 단위:")
    converted_unit = st.text_input("변환될 단위:")

    # 입력이 모두 완료되면 API 요청
    if substance and number and first_unit and converted_unit:
        prompt = f"물질 {substance} {number} {first_unit}을 {converted_unit}단위로 변환"

        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": "문장 생성, 번호 부여, 다른 답은 하지 말것"},
                {"role": "user", "content": prompt}
            ]
        )

        st.write("### 변환 결과")
        st.write(response.choices[0].message.content)
    else:
        st.write("모든 입력을 완료해주세요.")
