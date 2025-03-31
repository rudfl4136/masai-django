import pandas as pd
from datetime import datetime
from masai.models import BlogKeyword

def load_excel_to_blogkeyword(path):
    df = pd.read_excel(path, engine='openpyxl')  # 🔥 여기 엔진 명시!

    objects = []
    now = datetime.now()

    for _, row in df.iterrows():
        obj = BlogKeyword(
            thema=row['카테고리'],   # B열 → thema
            category=row['키워드'], # A열 → category
            worked_date=now
        )
        objects.append(obj)

    BlogKeyword.objects.bulk_create(objects, batch_size=1000)
    print(f"{len(objects)}건 삽입 완료")