
import streamlit as st

st.set_page_config(page_title="🐾 MBTI 동물 추천", page_icon="🐾", layout="centered")

DATA = {
    "INTJ": ("🦉","부엉이","전략적이고 분석적인 성향이 강해."),
    "INTP": ("🦊","여우","호기심 많고 창의적인 탐구가야."),
    "ENTJ": ("🦁","사자","리더십과 추진력이 돋보여."),
    "ENTP": ("🐒","원숭이","재치 있고 새로운 도전을 즐겨."),
    "INFJ": ("🦢","백조","깊이 있는 공감과 통찰력이 있어."),
    "INFP": ("🦋","나비","감수성과 상상력이 풍부해."),
    "ENFJ": ("🐬","돌고래","사람을 이끄는 따뜻한 리더야."),
    "ENFP": ("🦄","유니콘","열정과 아이디어가 넘쳐."),
    "ISTJ": ("🐢","거북이","성실하고 믿음직스러워."),
    "ISFJ": ("🐰","토끼","다정하고 배려심이 깊어."),
    "ESTJ": ("🦅","독수리","현실적이고 조직력이 뛰어나."),
    "ESFJ": ("🐶","강아지","친화력과 책임감이 강해."),
    "ISTP": ("🐈","고양이","독립적이고 실용적이야."),
    "ISFP": ("🦌","사슴","섬세하고 감각적인 매력이 있어."),
    "ESTP": ("🐆","치타","활동적이고 순발력이 좋아."),
    "ESFP": ("🦜","앵무새","밝고 분위기를 띄우는 재주가 있어."),
}

st.markdown("""
<style>
.stApp{
background:linear-gradient(135deg,#7c3aed,#2563eb,#06b6d4);
}
.card{
padding:24px;border-radius:24px;
background:rgba(255,255,255,.15);
backdrop-filter:blur(10px);
color:white;
text-align:center;
animation:fade .6s;
}
@keyframes fade{from{opacity:0;transform:translateY(15px)}to{opacity:1;transform:none}}
.big{font-size:80px}
</style>
""", unsafe_allow_html=True)

st.title("🐾 MBTI 동물 추천")

c1,c2,c3,c4=st.columns(4)
with c1:
    a=st.radio("I/E",["I","E"],horizontal=True)
with c2:
    b=st.radio("N/S",["N","S"],horizontal=True)
with c3:
    c=st.radio("T/F",["T","F"],horizontal=True)
with c4:
    d=st.radio("J/P",["J","P"],horizontal=True)

mbti=a+b+c+d
st.subheader(f"선택한 MBTI: ✨ {mbti}")

if st.button("🎉 결과 보기",use_container_width=True):
    st.balloons()
    st.snow()
    emo,name,desc=DATA[mbti]
    st.markdown(f"""
    <div class="card">
    <div class="big">{emo}</div>
    <h1>{name}</h1>
    <h2>{mbti}</h2>
    <p>{desc}</p>
    <p>⭐ 창의성</p>
    </div>
    """,unsafe_allow_html=True)
    st.progress((sum(map(ord,mbti))%31+70)/100)
    st.caption("💡 이 결과는 재미를 위한 성향 매칭이야.")
