import os
import json
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

okt = Okt()

def tokenize(text):
    return [word for word, pos in okt.pos(text) if pos in ["Noun", "Adjective"] and len(word) > 1]

def extract_keywords(texts, top_n=5):
    tokenized_texts = [" ".join(tokenize(t)) for t in texts]
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(tokenized_texts)
    scores = tfidf.sum(axis=0).A1
    words = vectorizer.get_feature_names_out()
    sorted_words = sorted(zip(words, scores), key=lambda x: -x[1])
    return [w for w, _ in sorted_words[:top_n]]

def main():
    # PostgreSQL에서 restaurant 데이터 가져오기
    restaurants = pd.read_sql_query("SELECT id, name FROM restaurant", con=engine)

    results = []

    for _, row in restaurants.iterrows():
        r_id, r_name = row["id"], row["name"]
        
        # 각 음식점의 리뷰 가져오기
        query = text("SELECT text FROM review WHERE restaurant_id = :id")
        reviews_df = pd.read_sql_query(query, con=engine, params={"id": r_id})
        reviews = reviews_df["text"].tolist()

        if not reviews:
            continue

        keywords = extract_keywords(reviews)
        results.append((r_id, keywords))
        print(f"📌 {r_name} → {keywords}")

    # UPDATE 쿼리 생성
    with open("update_keywords.sql", "w", encoding="utf-8") as f:
        for r_id, keywords in results:
            keyword_str = json.dumps(keywords, ensure_ascii=False)
            f.write(f"UPDATE restaurant SET keywords = '{keyword_str}' WHERE id = {r_id};\n")

    print("✅ 완료: update_keywords.sql 생성됨!")

if __name__ == "__main__":
    main()
