import streamlit as st
import random
from textwrap import dedent

# =========================
# Page setup
# =========================
st.set_page_config(
    page_title="MBTI 동물 추천 🐾",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# =========================
# Data
# =========================
MBTI_DATA = {
    "INTJ": {
        "animal": "🦉 부엉이",
        "title": "전략형 야행성 천재",
        "one_liner": "조용하지만 머릿속은 이미 다음 3단계를 계산 중!",
        "traits": ["분석력", "독립성", "계획성", "통찰력"],
        "description": "혼자서도 아주 잘하고, 목표가 보이면 끝까지 밀고 가는 타입이야. 겉으로는 차분해 보여도 속은 엄청 치밀한 편!",
        "why": "부엉이는 조용히 관찰하면서도 정확하게 판단하는 느낌이 강해서 INTJ랑 잘 어울려.",
    },
    "INTP": {
        "animal": "🦊 여우",
        "title": "호기심 폭발 아이디어 머신",
        "one_liner": "궁금한 게 생기면 끝까지 파고드는 탐구형!",
        "traits": ["호기심", "유연성", "분석력", "창의성"],
        "description": "생각의 점프가 빠르고, 새로운 관점 찾는 걸 좋아해. 규칙보다 '왜?'를 먼저 묻는 스타일!",
        "why": "여우는 영리하고 재치 있는 이미지가 있어서 INTP의 번뜩이는 사고방식과 잘 맞아.",
    },
    "ENTJ": {
        "animal": "🦁 사자",
        "title": "리더십 풀가동 카리스마",
        "one_liner": "결정하면 바로 추진하는 강력한 실행력!",
        "traits": ["리더십", "결단력", "추진력", "목표지향"],
        "description": "방향을 잡으면 팀을 이끌고 성과를 만드는 데 강해. 망설이기보다 움직이는 편이야.",
        "why": "사자는 존재감과 리더십의 상징이라 ENTJ의 당당한 추진력과 찰떡이야.",
    },
    "ENTP": {
        "animal": "🐒 원숭이",
        "title": "아이디어 폭죽형 유쾌러",
        "one_liner": "재밌는 얘기, 기발한 생각, 즉흥 변주 다 좋아!",
        "traits": ["재치", "즉흥성", "창의성", "활발함"],
        "description": "대화의 흐름을 바꾸는 재주가 있고, 새로운 시도를 즐기는 타입이야. 분위기를 살리는 능력이 좋아!",
        "why": "원숭이는 장난기와 민첩함이 돋보여서 ENTP의 유쾌하고 번뜩이는 매력과 잘 맞아.",
    },
    "INFJ": {
        "animal": "🦢 백조",
        "title": "깊고 조용한 감성 철학자",
        "one_liner": "겉은 শান্ত, 속은 깊은 생각의 바다!",
        "traits": ["공감", "직관", "이상주의", "깊이"],
        "description": "사람과 관계의 의미를 잘 읽고, 조용하지만 강한 신념을 가진 편이야. 진심이 느껴지는 타입!",
        "why": "백조는 우아하고 고요하지만 내면의 깊이가 느껴져서 INFJ 분위기와 잘 어울려.",
    },
    "INFP": {
        "animal": "🦋 나비",
        "title": "감성 가득 몽글몽글 상상가",
        "one_liner": "예쁜 의미를 발견하는 데 진심인 사람!",
        "traits": ["감수성", "이상", "공감", "상상력"],
        "description": "마음속 기준이 분명하고, 좋아하는 것에는 따뜻하게 몰입해. 분위기와 감성을 정말 잘 느껴.",
        "why": "나비는 섬세하고 아름답게 변화를 상징해서 INFP의 감성적인 매력과 잘 맞아.",
    },
    "ENFJ": {
        "animal": "🐬 돌고래",
        "title": "분위기를 살리는 따뜻한 리더",
        "one_liner": "사람들 사이를 밝게 연결하는 에너지!",
        "traits": ["배려", "소통", "리더십", "활력"],
        "description": "주변 사람의 기분과 분위기를 잘 캐치하고, 자연스럽게 좋은 흐름을 만드는 능력이 있어.",
        "why": "돌고래는 친화력, 지능, 에너지가 모두 느껴져서 ENFJ의 매력과 잘 어울려.",
    },
    "ENFP": {
        "animal": "🦄 유니콘",
        "title": "반짝반짝 아이디어 메이커",
        "one_liner": "상상력과 에너지가 동시에 튀는 타입!",
        "traits": ["열정", "낙천성", "창의성", "자유로움"],
        "description": "새로운 가능성을 보는 눈이 있고, 분위기를 확 끌어올리는 힘이 있어. 즐거움에 강해!",
        "why": "유니콘은 자유롭고 독특한 상징이라 ENFP의 반짝이는 개성과 잘 맞아.",
    },
    "ISTJ": {
        "animal": "🐢 거북이",
        "title": "묵묵한 신뢰의 완성형",
        "one_liner": "천천히 가도 결국 해내는 안정감!",
        "traits": ["책임감", "성실함", "안정성", "신중함"],
        "description": "약속, 규칙, 순서를 중요하게 생각하고 맡은 일을 꾸준히 해내는 편이야. 믿음직한 타입!",
        "why": "거북이는 느려 보여도 꾸준하고 단단한 이미지가 있어서 ISTJ의 성실함과 잘 맞아.",
    },
    "ISFJ": {
        "animal": "🐰 토끼",
        "title": "다정하고 세심한 케어형",
        "one_liner": "주변을 부드럽게 챙겨주는 따뜻함!",
        "traits": ["배려", "안정감", "세심함", "헌신"],
        "description": "티 나지 않게 도와주고 기억해 주는 디테일이 강해. 편안하고 포근한 분위기를 잘 만들어.",
        "why": "토끼는 부드럽고 친근한 느낌이 강해서 ISFJ의 따뜻한 성향과 잘 어울려.",
    },
    "ESTJ": {
        "animal": "🦅 독수리",
        "title": "판단 빠른 실전형 관리자",
        "one_liner": "흐름을 보고 바로 정리하는 능력!",
        "traits": ["조직력", "현실성", "결단력", "책임감"],
        "description": "상황을 빠르게 정리하고 기준을 세우는 데 강해. 실행과 결과를 중시하는 편이야.",
        "why": "독수리는 높은 시야와 강한 추진력이 느껴져서 ESTJ의 리더십과 잘 맞아.",
    },
    "ESFJ": {
        "animal": "🐶 강아지",
        "title": "친절도 만렙 분위기 메이커",
        "one_liner": "사람들이 편해지는 공감력 폭신함!",
        "traits": ["친화력", "배려", "조화", "사교성"],
        "description": "사람들과 잘 어울리고, 상대가 편안하게 느끼도록 배려하는 데 능해. 모임에서 빛나는 타입!",
        "why": "강아지는 친근하고 다정한 이미지가 강해서 ESFJ의 따뜻한 느낌과 잘 어울려.",
    },
    "ISTP": {
        "animal": "🐈 고양이",
        "title": "쿨하고 손재주 좋은 관찰자",
        "one_liner": "말보다 행동, 감정보다 실력!",
        "traits": ["실용성", "독립성", "관찰력", "순발력"],
        "description": "직접 해보며 익히는 걸 좋아하고, 필요할 때 정확하게 움직이는 편이야. 깔끔한 실전파!",
        "why": "고양이는 독립적이고 자유로운 느낌이 있어서 ISTP의 쿨한 매력과 잘 맞아.",
    },
    "ISFP": {
        "animal": "🦌 사슴",
        "title": "부드럽고 예민한 예술 감각형",
        "one_liner": "조용하지만 분위기 읽는 감각이 뛰어나!",
        "traits": ["감성", "유연함", "섬세함", "미적감각"],
        "description": "자연스럽고 편안한 분위기를 좋아하고, 감각적인 취향이 돋보여. 부드러운 매력이 있어.",
        "why": "사슴은 온화하고 아름다운 분위기가 느껴져서 ISFP의 섬세함과 잘 어울려.",
    },
    "ESTP": {
        "animal": "🐆 치타",
        "title": "즉흥력 끝판왕 액션형",
        "one_liner": "지금 재미있는 일에 바로 뛰어드는 타입!",
        "traits": ["대담함", "순발력", "현장감", "에너지"],
        "description": "생각보다 먼저 움직이고, 현장에서 감각적으로 대응하는 능력이 뛰어나. 스피드가 강점!",
        "why": "치타는 빠르고 날렵한 느낌이 강해서 ESTP의 즉각적인 행동력과 잘 맞아.",
    },
    "ESFP": {
        "animal": "🦜 앵무새",
        "title": "무대 위에서 반짝이는 흥부자",
        "one_liner": "밝은 에너지로 분위기를 확 띄워버려!",
        "traits": ["표현력", "사교성", "즉흥성", "활기"],
        "description": "분위기를 읽는 센스가 좋고, 즐거움을 자연스럽게 퍼뜨리는 타입이야. 존재감이 선명해!",
        "why": "앵무새는 화려하고 밝은 이미지가 있어서 ESFP의 생기 넘치는 매력과 잘 어울려.",
    },
    "UNKNOWN": {
        "animal": "✨ 미지의 생명체",
        "title": "아직 형태가 완전히 정해지지 않은 매력형",
        "one_liner": "MBTI를 4글자로 정확히 넣어주면 더 딱 맞게 추천할 수 있어!",
        "traits": ["개성", "가능성", "호기심", "유연성"],
        "description": "아직 확정하기 어려워도 괜찮아. 입력만 제대로 되면 바로 너한테 어울리는 동물을 찾아줄게!",
        "why": "정확한 MBTI 형식일 때 가장 잘 맞는 추천이 가능해.",
    },
}

ANIMALS = [
    ("🦉", "부엉이"),
    ("🦊", "여우"),
    ("🦁", "사자"),
    ("🐒", "원숭이"),
    ("🦢", "백조"),
    ("🦋", "나비"),
    ("🐬", "돌고래"),
    ("🦄", "유니콘"),
    ("🐢", "거북이"),
    ("🐰", "토끼"),
    ("🦅", "독수리"),
    ("🐶", "강아지"),
    ("🐈", "고양이"),
    ("🦌", "사슴"),
    ("🐆", "치타"),
    ("🦜", "앵무새"),
]

# =========================
# Helpers
# =========================
def normalize_mbti(text: str) -> str:
    if not text:
        return ""
    t = text.strip().upper().replace(" ", "")
    return t

def is_valid_mbti(mbti: str) -> bool:
    if len(mbti) != 4:
        return False
    valid_sets = [
        {"I", "E"},
        {"N", "S"},
        {"T", "F"},
        {"J", "P"},
    ]
    return (
        mbti[0] in valid_sets[0]
        and mbti[1] in valid_sets[1]
        and mbti[2] in valid_sets[2]
        and mbti[3] in valid_sets[3]
    )

def get_match_text(mbti: str) -> dict:
    if is_valid_mbti(mbti):
        return MBTI_DATA.get(mbti, MBTI_DATA["UNKNOWN"])
    return MBTI_DATA["UNKNOWN"]

def sparkle_line():
    return "✨ " * random.randint(4, 7)

# =========================
# Custom CSS
# =========================
st.markdown(
    """
<style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(255,255,255,0.28), transparent 26%),
            radial-gradient(circle at top right, rgba(255,255,255,0.18), transparent 24%),
            linear-gradient(135deg, #7c3aed 0%, #2563eb 45%, #06b6d4 100%);
        color: white;
    }

    /* Bubble background */
    .bubble-wrap {
        position: fixed;
        inset: 0;
        overflow: hidden;
        pointer-events: none;
        z-index: 0;
    }
    .bubble {
        position: absolute;
        bottom: -120px;
        border-radius: 999px;
        background: rgba(255,255,255,0.18);
        box-shadow: inset 0 0 20px rgba(255,255,255,0.16);
        animation: floatUp linear infinite;
        backdrop-filter: blur(2px);
    }
    .bubble:nth-child(1){ left: 8%; width: 18px; height: 18px; animation-duration: 11s; animation-delay: 0s; }
    .bubble:nth-child(2){ left: 16%; width: 28px; height: 28px; animation-duration: 16s; animation-delay: 1s; }
    .bubble:nth-child(3){ left: 24%; width: 12px; height: 12px; animation-duration: 12s; animation-delay: 3s; }
    .bubble:nth-child(4){ left: 38%; width: 22px; height: 22px; animation-duration: 14s; animation-delay: 2s; }
    .bubble:nth-child(5){ left: 50%; width: 36px; height: 36px; animation-duration: 18s; animation-delay: 0s; }
    .bubble:nth-child(6){ left: 63%; width: 16px; height: 16px; animation-duration: 13s; animation-delay: 4s; }
    .bubble:nth-child(7){ left: 75%; width: 30px; height: 30px; animation-duration: 17s; animation-delay: 1.5s; }
    .bubble:nth-child(8){ left: 86%; width: 14px; height: 14px; animation-duration: 10s; animation-delay: 5s; }
    .bubble:nth-child(9){ left: 92%; width: 24px; height: 24px; animation-duration: 15s; animation-delay: 2.5s; }

    @keyframes floatUp {
        0%   { transform: translateY(0) scale(1); opacity: 0; }
        10%  { opacity: 1; }
        100% { transform: translateY(-120vh) scale(1.3); opacity: 0; }
    }

    /* Main content cards */
    .hero {
        position: relative;
        z-index: 1;
        padding: 1.2rem 1.2rem 0.3rem 1.2rem;
        border-radius: 28px;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: 0 16px 40px rgba(0,0,0,0.18);
        backdrop-filter: blur(16px);
        margin-bottom: 1rem;
        animation: fadeInUp 0.8s ease both;
    }

    .title {
        font-size: 2.2rem;
        font-weight: 900;
        margin-bottom: 0.2rem;
        line-height: 1.15;
        text-shadow: 0 2px 14px rgba(0,0,0,0.18);
    }

    .subtitle {
        font-size: 1.0rem;
        opacity: 0.92;
        margin-bottom: 0.5rem;
    }

    .chip-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-top: 0.8rem;
        margin-bottom: 0.2rem;
    }

    .chip {
        display: inline-block;
        padding: 0.42rem 0.72rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.16);
        border: 1px solid rgba(255,255,255,0.22);
        font-size: 0.85rem;
        font-weight: 700;
        box-shadow: 0 8px 18px rgba(0,0,0,0.08);
        animation: pop 1.2s ease both;
    }

    .card {
        position: relative;
        z-index: 1;
        padding: 1.1rem 1.1rem 1rem 1.1rem;
        border-radius: 26px;
        background: rgba(255,255,255,0.14);
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: 0 18px 40px rgba(0,0,0,0.16);
        backdrop-filter: blur(16px);
        margin-top: 1rem;
        animation: fadeInUp 0.9s ease both;
    }

    .big-animal {
        font-size: 3rem;
        font-weight: 900;
        margin-bottom: 0.25rem;
        animation: bounce 2.6s ease-in-out infinite;
        display: inline-block;
    }

    .animal-name {
        font-size: 1.5rem;
        font-weight: 900;
        margin-bottom: 0.2rem;
    }

    .tiny-note {
        opacity: 0.88;
        font-size: 0.92rem;
        line-height: 1.55;
    }

    .quote {
        margin-top: 0.8rem;
        padding: 0.9rem 1rem;
        border-left: 4px solid rgba(255,255,255,0.75);
        border-radius: 16px;
        background: rgba(255,255,255,0.1);
        font-weight: 700;
        line-height: 1.6;
    }

    .trait {
        display: inline-block;
        margin: 0.28rem 0.35rem 0 0;
        padding: 0.38rem 0.68rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.14);
        border: 1px solid rgba(255,255,255,0.18);
        font-size: 0.85rem;
        font-weight: 700;
    }

    .footer {
        position: relative;
        z-index: 1;
        margin-top: 1.3rem;
        text-align: center;
        font-size: 0.9rem;
        opacity: 0.92;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(18px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    @keyframes pop {
        from { opacity: 0; transform: scale(0.85); }
        to   { opacity: 1; transform: scale(1); }
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-8px) rotate(-2deg); }
    }

    /* Make Streamlit buttons prettier */
    div.stButton > button {
        border: none !important;
        border-radius: 999px !important;
        padding: 0.72rem 1.2rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #ffffff 0%, #f5f7ff 100%) !important;
        color: #1f2937 !important;
        box-shadow: 0 14px 28px rgba(0,0,0,0.16) !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease !important;
    }
    div.stButton > button:hover {
        transform: translateY(-2px) scale(1.01);
        box-shadow: 0 18px 32px rgba(0,0,0,0.2) !important;
    }

    /* Input */
    div[data-baseweb="input"] > div {
        border-radius: 18px !important;
        background: rgba(255,255,255,0.95) !important;
    }

    /* Hide streamlit decoration */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""",
    unsafe_allow_html=True,
)

# Bubble overlay
st.markdown(
    """
<div class="bubble-wrap" aria-hidden="true">
  <div class="bubble"></div><div class="bubble"></div><div class="bubble"></div>
  <div class="bubble"></div><div class="bubble"></div><div class="bubble"></div>
  <div class="bubble"></div><div class="bubble"></div><div class="bubble"></div>
</div>
""",
    unsafe_allow_html=True,
)

# =========================
# UI
# =========================
st.markdown(
    f"""
<div class="hero">
  <div class="title">🐾 MBTI 동물 추천소</div>
  <div class="subtitle">
    MBTI를 넣으면 너랑 찰떡인 동물을 추천하고, 성향도 재밌게 알려줄게. {sparkle_line()}
  </div>
  <div class="chip-row">
    <span class="chip">🧠 성향 분석</span>
    <span class="chip">🐶 동물 매칭</span>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("### MBTI 입력")
mbti_input = st.text_input(
    "예: ENFP, ISTJ, INFJ ...",
    placeholder="MBTI를 입력해줘",
    label_visibility="collapsed",
)

col1, col2 = st.columns([1, 1])
with col1:
    submit = st.button("동물 추천 받기 🎉", use_container_width=True)
with col2:
    random_pick = st.button("랜덤 MBTI 보기 🎲", use_container_width=True)

if "picked_mbti" not in st.session_state:
    st.session_state.picked_mbti = ""

if random_pick:
    st.session_state.picked_mbti = random.choice(list(MBTI_DATA.keys()))

if submit and mbti_input.strip():
    st.session_state.picked_mbti = normalize_mbti(mbti_input)

picked = st.session_state.picked_mbti or normalize_mbti(mbti_input)

if picked:
    data = get_match_text(picked)

    if is_valid_mbti(picked):
        st.markdown(
            f"""
<div class="card">
  <div class="big-animal">{data["animal"].split(" ", 1)[0]}</div>
  <div class="animal-name">{data["animal"]}</div>
  <div class="tiny-note">
    <b>{picked}</b> 타입은 <b>{data["title"]}</b> 느낌이야.
  </div>

  <div class="quote">“{data["one_liner"]}”</div>

  <p style="margin-top: 0.9rem; margin-bottom: 0.4rem; font-weight: 900;">성향 포인트</p>
  <div>
    {''.join([f'<span class="trait">{t}</span>' for t in data["traits"]])}
  </div>

  <p style="margin-top: 0.9rem; margin-bottom: 0.4rem; font-weight: 900;">이 동물이 어울리는 이유</p>
  <div class="tiny-note">{data["why"]}</div>

  <p style="margin-top: 0.9rem; margin-bottom: 0.4rem; font-weight: 900;">한 줄 설명</p>
  <div class="tiny-note">{data["description"]}</div>
</div>
""",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
<div class="card">
  <div class="big-animal">✨</div>
  <div class="animal-name">입력값을 다시 확인해줘</div>
  <div class="tiny-note">
    MBTI는 <b>4글자</b>여야 하고, 각 자리는 아래처럼 맞아야 해:
    <br><br>
    1번째: I / E<br>
    2번째: N / S<br>
    3번째: T / F<br>
    4번째: J / P
  </div>

  <div class="quote">예시: ENFP, ISTJ, INFJ, ESTP</div>

  <p style="margin-top: 0.9rem; margin-bottom: 0.4rem; font-weight: 900;">그래도 먼저 하나 골라줄게</p>
  <div class="tiny-note">
    너한테 지금 뜬 동물은 <b>{data["animal"]}</b> 이고, 느낌은 <b>{data["title"]}</b> 쪽이야.
  </div>
</div>
""",
            unsafe_allow_html=True,
        )

st.markdown(
    """
<div class="card">
  <div class="animal-name">🧪 재미있는 설명</div>
  <div class="tiny-note">
    이 앱은 MBTI를 아주 가볍고 유쾌하게 해석하는 버전이야.
    진짜 성격은 더 다양하니까, 결과는 <b>재미있는 참고용</b>으로 보면 딱 좋아.
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="footer">
  ✨ 오늘의 동물 운세는 가볍고 귀엽게 즐기기 🐾
</div>
""",
    unsafe_allow_html=True,
)
