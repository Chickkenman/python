import openai

# OpenAI API 키 설정
openai.api_key = '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'


def get_chatgpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # 모델 이름을 gpt-4o-mini로 변경
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']


# 반복할 업무 정의
def main():
    while True:
        # 사용자로부터 입력 받기
        prompt = input("어떤 작업을 수행할까요? (종료하려면 'exit' 입력): ")
        if prompt.lower() == 'exit':
            break

        # ChatGPT에 요청하고 응답 받기
        response = get_chatgpt_response(prompt)
        print("ChatGPT의 응답:", response)


if __name__ == "__main__":
    main()
