from openai import OpenAI
from decouple import config

class ChatGptAi:
    def __init__(self):
        self.contents = ''

    def response_contents(self, category,styleoption,toneoption):
        print('category: ' + category)
        api_key = config("OPENAI_API_KEY")
        client = OpenAI(api_key=api_key)

        prompt = f"""
                당신은 실제로 블로그를 운영 중인 작가입니다. 
                아래 키워드를 바탕으로 네이버 블로그에 어울리는 자연스럽고 공감 가는 글을 작성해주세요.

                키워드: {category}
                스타일: {styleoption}
                말투: {toneoption}

                요구사항:
                1. 글을 읽는 독자가 친구처럼 느낄 수 있도록 자연스럽고 친근한 말투로 작성
                2. 서론에서는 인사와 함께 글을 쓰게 된 배경 또는 이유를 간단히 설명
                3. 본문은 2~3개의 소제목으로 나누고, 개인적인 경험이나 감상을 섞어 작성
                4. 결론에서는 요약과 함께 독자에게 말을 거는 마무리 멘트를 넣기

                마크다운이나 HTML은 사용하지 말고, 일반 블로그 글처럼 작성해주세요.
                """

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "당신은 사람처럼 자연스러운 블로그 글을 쓰는 전문 작가입니다."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.6,
            max_tokens=1200,
        )

        contents = response.choices[0].message.content
        return contents