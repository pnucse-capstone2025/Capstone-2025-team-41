# React와 NestJS를 활용한 맛집 지도 웹 애플리케이션 개발
### 1. 프로젝트 배경
#### 1.1. 국내외 시장 현황 및 문제점
현재의 맛집 추천 서비스들은 사용자의 맥락을 충분히 반영하지 못하는 한계를 지니고 있다. 첫째, 정보의 신뢰성 부족이다. 포털 검색 상위에 노출되는 정보는 광고성 블로그나 협찬 리뷰가 많아 실제 경험 기반의 가치가 낮다. 둘째, 사용자 중심성 결여이다. 현 위치, 거리, 선호 키워드 등 개인화 요소가 반영되지 않아 검색 결과의 타당성이 떨어진다. 셋째, 감성 정보 부재이다. 리뷰 수나 별점 평균만을 보여줄 뿐, 해당 리뷰가 긍정적인지 부정적인지에 대한 분석은 제공하지 않는다. 또한 Google Maps API의 유료화로 인한 비용 부담, 크롤링 과정의 법적·기술적 제약 역시 문제로 지적된다. 따라서 공공 API, 사용자 리뷰 데이터, 자동화된 분석 기법을 결합한 새로운 접근 방식이 필요하다.

#### 1.2. 필요성과 기대효과
외식 선택은 단순한 소비가 아니라 경험과 여가 활동으로 자리 잡으며, 이에 따라 맛집 탐색 서비스 수요가 꾸준히 증가하고 있다. 그러나 기존 플랫폼은 광고성 후기와 별점 중심 정보 제공에 치우쳐 신뢰성과 개인화 측면에서 한계를 드러낸다. 본 프로젝트는 이러한 문제를 해결하기 위해 사용자 후기 기반 감성 분석을 도입하고, 위치·키워드·감정 데이터를 종합하여 정교한 추천을 제공한다. 이를 통해 사용자에게 더 높은 신뢰성을 보장하고, 개인 맞춤형 경험을 제공하는 차세대 맛집 추천 시스템을 구축하고자 한다.

### 2. 개발 목표
#### 2.1. 목표 및 세부 내용
본 프로젝트인 “먹킷리스트”는 사용자 리뷰의 감성을 정량적으로 분석하고, 위치 기반 필터링과 키워드 검색기능을 결합하여 신뢰도 높은 맛집 추천 시스템을 구현하는 것을 목표로 한다. 이를 위해 다음과 같은 기술적 목표를 설정하였다.
1. 위치 기반 맛집 탐색 기능 구현: Kakao Maps API를 통해 사용자의 현재 위치 반경 내 음식점 정보를 수집하고, 반경 설정(500m~1km 등)을 통해 결과를 필터링한다.
2. 실제 후기 기반 감성 분석: HuggingFace의 사전학습 모델을 활용하여 사용자가 입력한 리뷰의 감정을 자동으로 분석하고, 긍정/부정/중립을 점수 및 이모지로 시각화한다.
3. 사용자 중심 UI/UX 설계: React 기반 반응형 UI를 통해 모바일에서도 최적화된 사용성을 제공하며, 추천 결과에는 키워드 요약, 대표 문장, 감정 비율 등을 함께 제시한다.
4. 신뢰성 높은 데이터 수집 파이프라인 구축: Python + Selenium 기반 크롤러를 통해 블로그 리뷰 데이터를 수집하고, 정제 및 지오코딩 후 DB에 저장한다.
추후에는 음식 사진 업로드 기반의 이미지 분석 추천(OpenCLIP 등)이나, 사용자 히스토리를 활용한 개인화 추천, 관리자용 가중치 조정 도구 등으로 확장할 계획이다.

#### 2.2. 기존 서비스 대비 차별성 
본 프로젝트는 기존 맛집 추천 서비스와 차별적으로 다음과 같은 특성을 지닌다. 첫째, 광고성 정보 배제이다. 포털 상위 노출이나 협찬 리뷰에 의존하지 않고, 사용자 후기와 직접 크롤링된 데이터를 기반으로 신뢰성 있는 정보를 제공한다. 둘째, 맥락 기반 탐색 기능이다. 단순 평점 중심의 검색에서 벗어나, 사용자의 현재 위치 반경, 입력 키워드, 감정 분석 결과 등을 종합적으로 반영하여 보다 정밀한 추천을 구현한다. 셋째, 정성적 데이터 분석 강화이다. HuggingFace 모델을 활용해 리뷰의 긍정·부정 감정을 자동 분류한다. 마지막으로, 확장성 높은 아키텍처를 채택하였다. 초기에는 감성 분석과 지도 기반 추천을 MVP로 구현하되, 추후 이미지 검색, 개인화 추천, 관리자 설정 등 확장 기능을 단계적으로 적용할 수 있도록 설계하였다.

#### 2.3. 사회적 가치 도입 계획 
본 서비스는 단순한 상업적 추천 시스템을 넘어, 사용자 중심의 공정한 정보 제공을 목표로 한다.  
첫째, 정보 비대칭 해소이다. 광고성 콘텐츠가 난무하는 기존 환경에서, 실제 사용자 후기에 기반한 감정 분석 결과를 제공함으로써 소비자가 신뢰할 수 있는 선택을 돕는다. 둘째, 소상공인 지원이다. 별점이 낮더라도 특정 키워드나 긍정적인 감정이 많이 언급된 음식점은 추천 결과에 반영되어, 지역 소상공인의 노출 기회를 확대할 수 있다. 셋째, 사회적 비용 절감이다. 사용자 맞춤형 탐색을 통해 불필요한 소비와 시간 낭비를 줄이고, 건강하고 지속 가능한 외식 문화를 조성하는 데 기여한다. 궁극적으로 본 프로젝트는 단순히 맛집을 찾는 도구를 넘어, 신뢰 기반의 데이터 생태계와 지역 경제 활성화에 기여하는 사회적 가치를 창출하고자 한다.

### 3. 시스템 설계
#### 3.1. 시스템 구성도
<img width="1168" height="729" alt="시스템 구성도" src="https://github.com/user-attachments/assets/831a9a15-cebf-41d1-929d-ae46c370ac30" />

#### 3.2. 사용 기술
| 분류        | 도입 기술                                              |
|-------------|--------------------------------------------------------|
| 프론트엔드  | React, TypeScript, Emotion(Styled CSS), Kakao Maps SDK |
| 백엔드      | NestJS, Swagger, TypeORM, Redis, PostgreSQL(예정)      |
| 감성분석    | HuggingFace Transformers, KcELECTRA, Flask             |
| 인증/보안   | JWT, HttpOnly 쿠키, JwtCookieGuard, CORS 설정          |
| 크롤링 서버 | Python, Selenium, Docker                               |
| 배포 환경   | Nginx, Let's Encrypt, GitHub Actions (예정)            |

### 4. 개발 결과
#### 4.1. 전체 시스템 흐름도
<img width="1507" height="779" alt="서비스 전체 구성도" src="https://github.com/user-attachments/assets/cff9bd56-0b4b-47d2-bfe0-ff054f2b1fb0" />

#### 4.2. 기능 설명 및 주요 기능 명세서
| 요구사항명      | 기능명                 | 상세 설명                                                         |
|-----------------|------------------------|-------------------------------------------------------------------|
| 로그인/회원가입 | 사용자 로그인/회원가입 | JWT 기반 인증 구현. HttpOnly 쿠키 사용으로 보안 강화.             |
| 음식점 검색     | 위치 기반 탐색         | 사용자의 현재 위치 및 반경 기반 음식점 탐색 (Kakao Maps API 활용) |
| 키워드 자동완성 | 키워드 추천            | TF-IDF 기반 키워드 맵을 기반으로 자동완성 제안                    |
| 감성 분석       | 리뷰 감정 분석         | HuggingFace 모델 기반으로 긍/부정 감정 분류                       |
| 리뷰 저장       | 후기 저장 기능         | 사용자가 입력한 리뷰와 감정 결과를 함께 DB에 저장                 |
| 설명 패널 생성  | 추천 이유 제공         | 키워드 요약, 대표 문장, 출처비율 등 JSON 형태 설명 제공           |
| 관리자 설정     | 점수 가중치 조정       | 관리자 UI에서 α, β, γ, δ 계수 설정 가능 (예정)                    |
| 프론트 연동     | 인증 포함 통신 구현    | credentials: 'include' 설정을 통한 쿠키 기반 인증 연동            |
| 블로그 크롤링   | 외부 데이터 수집       | 네이버 지도 기반 크롤러로 음식점 정보 및 리뷰 수집                |
| 개인화 추천     | 사용자 기반 추천       | 유저 히스토리를 기반으로 선호도 기반 추천 로직 설계 예정          |

#### 4.3. 디렉토리 구조
<details>
  <summary>프론트엔드</summary>
  
```text
├── crawling/
│   ├── get_reviews.py
│   └── get_store_list.py
└── frontend/
    ├── .env
    ├── .gitignore
    ├── .prettierrc
    ├── README.md
    ├── eslint.config.js
    ├── index.html
    ├── kakao-sdk-ping.html
    ├── localhost-key.pem
    ├── localhost.pem
    ├── package-lock.json
    ├── package.json
    ├── public/
    │   ├── icons/
    │   │   ├── location.png
    │   │   ├── restaurant.png
    │   │   ├── review.png
    │   │   └── search.png
    │   └── vite.svg
    ├── src/
    │   ├── App.tsx
    │   ├── api/
    │   │   └── search.ts
    │   ├── assets/
    │   │   └── react.svg
    │   ├── components/
    │   │   ├── Layout/
    │   │   │   └── Layout.tsx
    │   │   ├── Map/
    │   │   │   └── KakaoMap.tsx
    │   │   ├── Ranking/
    │   │   │   └── RankingSection.tsx
    │   │   ├── Review/
    │   │   │   └── ReviewSection.tsx
    │   │   ├── TopBar/
    │   │   │   └── TopBar.tsx
    │   │   └── common/
    │   │       ├── IconImg.tsx
    │   │       └── Spinner.tsx
    │   ├── main.tsx
    │   ├── mocks/
    │   │   └── keywordSearch.mock.ts
    │   ├── pages/
    │   │   ├── Auth/
    │   │   │   ├── Login.tsx
    │   │   │   └── Signup.tsx
    │   │   └── Home.tsx
    │   ├── styles/
    │   │   ├── GlobalStyles.tsx
    │   │   ├── colors.ts
    │   │   ├── emotion.d.ts
    │   │   ├── spacing.ts
    │   │   ├── theme.ts
    │   │   └── typography.ts
    │   ├── types/
    │   │   └── ranking.ts
    │   └── vite-env.d.ts
    ├── tsconfig.app.json
    ├── tsconfig.json
    ├── tsconfig.node.json
    └── vite.config.ts
```
</details>
<details>
  <summary>백엔드</summary>

```text
├── .gitignore
├── README.md
├── backend.code-workspace
├── backend/
│   ├── .gitignore
│   ├── .prettierrc
│   ├── README.md
│   ├── dev.sqlite
│   ├── eslint.config.mjs
│   ├── generate_keywords.py
│   ├── meokkitlist-clean-mirror/
│   │   ├── HEAD
│   │   ├── config
│   │   ├── description
│   │   ├── filter-repo/
│   │   │   ├── already_ran
│   │   │   ├── changed-refs
│   │   │   ├── commit-map
│   │   │   ├── first-changed-commits
│   │   │   ├── ref-map
│   │   │   └── suboptimal-issues
│   │   ├── hooks/
│   │   │   ├── applypatch-msg.sample
│   │   │   ├── commit-msg.sample
│   │   │   ├── fsmonitor-watchman.sample
│   │   │   ├── post-update.sample
│   │   │   ├── pre-applypatch.sample
│   │   │   ├── pre-commit.sample
│   │   │   ├── pre-merge-commit.sample
│   │   │   ├── pre-push.sample
│   │   │   ├── pre-rebase.sample
│   │   │   ├── pre-receive.sample
│   │   │   ├── prepare-commit-msg.sample
│   │   │   ├── push-to-checkout.sample
│   │   │   ├── sendemail-validate.sample
│   │   │   └── update.sample
│   │   ├── info/
│   │   │   ├── exclude
│   │   │   └── refs
│   │   ├── objects/
│   │   │   ├── info/
│   │   │   │   ├── commit-graph
│   │   │   │   └── packs
│   │   │   └── pack/
│   │   │       ├── pack-68b8f5bb2905742273d7d8fc20ff9547dd62731e.bitmap
│   │   │       ├── pack-68b8f5bb2905742273d7d8fc20ff9547dd62731e.idx
│   │   │       ├── pack-68b8f5bb2905742273d7d8fc20ff9547dd62731e.pack
│   │   │       └── pack-68b8f5bb2905742273d7d8fc20ff9547dd62731e.rev
│   │   ├── packed-refs
│   │   └── refs/
│   │       └── remotes/
│   │           └── origin/
│   │               ├── backend
│   │               ├── backend_bug_fix
│   │               ├── frontend
│   │               └── main
│   ├── meokkitlist.sqlite
│   ├── nest-cli.json
│   ├── package-lock.json
│   ├── package.json
│   ├── scripts/
│   │   ├── crawl/
│   │   │   ├── get_reviews.py
│   │   │   └── get_store_list.py
│   │   └── keyword_extractor.py
│   ├── sqlite3.exe
│   ├── src/
│   │   ├── app.controller.spec.ts
│   │   ├── app.controller.ts
│   │   ├── app.module.ts
│   │   ├── app.service.ts
│   │   ├── auth/
│   │   │   ├── auth.controller.ts
│   │   │   ├── auth.module.ts
│   │   │   ├── auth.service.ts
│   │   │   ├── dto.ts
│   │   │   └── jwt-cookie.guard.ts
│   │   ├── config/
│   │   │   └── ranking.config.ts
│   │   ├── controllers/
│   │   │   ├── keyword.controller.ts
│   │   │   ├── meokkitlist-project.code-workspace
│   │   │   ├── redis.controller.ts
│   │   │   ├── restaurant.controller.ts
│   │   │   ├── review.controller.ts
│   │   │   ├── search.controller.ts
│   │   │   └── sentiment.controller.ts
│   │   ├── dto/
│   │   │   ├── create-restaurant.dto.ts
│   │   │   ├── search-keyword.dto.ts
│   │   │   └── sentiment-test.dto.ts
│   │   ├── entities/
│   │   │   ├── restaurant.entity.ts
│   │   │   ├── review.entity.ts
│   │   │   └── user.entity.ts
│   │   ├── gpt/
│   │   │   ├── dto/
│   │   │   │   ├── extract-keywords.dto.ts
│   │   │   │   └── search-keyword.query.dto.ts
│   │   │   ├── gpt.controller.ts
│   │   │   └── gpt.service.ts
│   │   ├── kakao/
│   │   │   ├── dto/
│   │   │   │   └── search.dto.ts
│   │   │   ├── kakao.controller.ts
│   │   │   └── kakao.service.ts
│   │   ├── main.ts
│   │   ├── services/
│   │   │   ├── keyword-extraction.service.ts
│   │   │   ├── keyword-map.service.ts
│   │   │   ├── restaurant.service.ts
│   │   │   ├── review.service.ts
│   │   │   ├── search.service.ts
│   │   │   └── sentiment.service.ts
│   │   └── types/
│   │       └── cache-manager-ioredis.d.ts
│   ├── test/
│   │   ├── app.e2e-spec.ts
│   │   └── jest-e2e.json
│   ├── tsconfig.build.json
│   ├── tsconfig.json
│   └── update_keywords.sql
├── dev.sqlite
├── sentiment-server/
│   ├── Dockerfile
│   ├── __pycache__/
│   │   └── main.cpython-311.pyc
│   ├── download_model.py
│   ├── main.py
│   ├── model/
│   │   └── beomi_model/
│   │       ├── config.json
│   │       ├── special_tokens_map.json
│   │       ├── tokenizer.json
│   │       └── tokenizer_config.json
│   └── requirements.txt
└── src_backup/
    ├── App.css
    ├── App.test.tsx
    ├── App.tsx
    ├── KakaoMap.tsx
    ├── app.controller.spec.ts
    ├── app.controller.ts
    ├── app.module.ts
    ├── app.service.ts
    ├── auth/
    │   ├── auth.controller.ts
    │   ├── auth.module.ts
    │   ├── auth.service.ts
    │   ├── dto.ts
    │   └── jwt-cookie.guard.ts
    ├── config/
    │   └── ranking.config.ts
    ├── controllers/
    │   ├── keyword.controller.ts
    │   ├── meokkitlist-project.code-workspace
    │   ├── redis.controller.ts
    │   ├── restaurant.controller.ts
    │   ├── review.controller.ts
    │   ├── search.controller.ts
    │   └── sentiment.controller.ts
    ├── dto/
    │   ├── create-restaurant.dto.ts
    │   └── search-keyword.dto.ts
    ├── entities/
    │   ├── restaurant.entity.ts
    │   ├── review.entity.ts
    │   └── user.entity.ts
    ├── gpt/
    │   ├── dto/
    │   │   ├── extract-keywords.dto.ts
    │   │   └── search-keyword.query.dto.ts
    │   ├── gpt.controller.ts
    │   └── gpt.service.ts
    ├── index.css
    ├── index.tsx
    ├── kakao/
    │   ├── dto/
    │   │   └── search.dto.ts
    │   ├── kakao.controller.ts
    │   └── kakao.service.ts
    ├── logo.svg
    ├── main.ts
    ├── react-app-env.d.ts
    ├── reportWebVitals.ts
    ├── services/
    │   ├── keyword-extraction.service.ts
    │   ├── keyword-map.service.ts
    │   ├── restaurant.service.ts
    │   ├── review.service.ts
    │   ├── search.service.ts
    │   └── sentiment.service.ts
    ├── setupTests.ts
    └── types/
        ├── cache-manager-ioredis.d.ts
        └── csv-parser.d.ts
```
</details>

### 5. 설치 및 실행 방법
#### 5.1. 설치절차 및 실행 방법
##### 프론트엔드
```bash
cd frontend
npm install
npm run dev
# 기본 포트: http://localhost:5173
```
##### 백엔드
```bash
cd backend
npm install
npm build
nest start
# 기본 포트: http://localhost:3001
```

### 6. 소개 자료 및 시연 영상
#### 6.1. 프로젝트 소개 자료
[PPT](https://github.com/pnucse-capstone2025/Capstone-2025-team-41/blob/main/docs/03.%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C/%E1%84%86%E1%85%A5%E1%86%A8%E1%84%8F%E1%85%B5%E1%86%BA%E1%84%85%E1%85%B5%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%20%E1%84%87%E1%85%A1%E1%86%AF%E1%84%91%E1%85%AD.pptx)

#### 6.2. 시연 영상
[![먹킷리스트 시연 영상](https://img.youtube.com/vi/FjNO5QgeNCQ/0.jpg)](https://www.youtube.com/watch?v=FjNO5QgeNCQ)    

### 7. 팀 구성
#### 7.1. 팀원별 소개 및 역할 분담
| Profile | Role                                                                                                                                                                      | Email                    | GitHub        |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|---------------|
| 최민기  | 백엔드 API, 감성 분석 연동, 크롤링 서버 설계,JWT 인증 및 쿠키 기반 로그인 구현,Redis 캐시 도입 및 CORS 설 정,Render 배포 환경 구성 및 오류 디버깅                         | cmg0513@pusan.ac.kr      | @minggichoiii |
| 권소현  | 프론트엔드(지도, UI, 후기 입력, 감성 분석 결과 표시), 크롤링 로직 설계 및 모델 개발, 사용자 입력 데이터 통합 표시,추천/검색 페이지 구현, Vercel 배포 및 API 연동 테스트 | sohyun10521052@gmail.com | @thgus0       |
