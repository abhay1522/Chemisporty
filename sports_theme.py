"""
Sports / stadium theme for Streamlit - pure CSS, no image files needed.

 apply_sports_theme()   -> call once near the top of app.py
 hero(...)              -> returns the scoreboard banner HTML for the Home page

To change the colours, edit the variables at the top of the CSS (:root { ... }).
"""

import base64
import html

import streamlit as st

SPORTS_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Rajdhani:wght@500;600;700&family=Orbitron:wght@600;800&display=swap');

:root {
    --navy-900: #070d1b;
    --navy-800: #0b1426;
    --navy-700: #12213d;
    --navy-600: #1b3358;
    --lime: #c6ff00;
    --orange: #ff6b1a;
    --cyan: #18c8ff;
    --amber: #ffb300;
    --red: #ff3b3b;
    --text: #e8eefc;
    --muted: #9fb3d9;
}

/* ---------- Stadium-night background with floodlights & track lanes ---------- */
.stApp {
    background-color: var(--navy-800);
    background-image:
        radial-gradient(ellipse 600px 320px at 6% -4%, rgba(255,255,255,.16), transparent 70%),
        radial-gradient(ellipse 600px 320px at 94% -4%, rgba(255,255,255,.16), transparent 70%),
        repeating-linear-gradient(180deg,
            transparent 0 46px, rgba(198,255,0,.05) 46px 48px);
    background-attachment: fixed;
}

/* ---------- Top bar ---------- */
[data-testid="stHeader"] {
    background: linear-gradient(90deg, var(--navy-900), var(--navy-600));
    border-bottom: 4px solid var(--lime);
}

/* ---------- Main content panel ---------- */
.block-container {
    background: rgba(7, 13, 27, 0.82);
    border: 1px solid rgba(255,255,255,.10);
    border-top: 5px solid var(--lime);
    border-radius: 6px;
    box-shadow: 0 10px 40px rgba(0,0,0,.45);
    padding: 2.2rem 2.4rem 3rem 2.4rem !important;
    margin-top: 1.2rem;
    margin-bottom: 1.2rem;
}

/* ---------- Fonts & text ---------- */
.stApp p, .stApp label, .stApp li, .stApp input, .stApp textarea,
.stApp [data-testid="stMarkdownContainer"], .stApp [data-testid="stCaptionContainer"] {
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 1.15rem;
    color: var(--text);
}
h1, h2, h3, h4, .cc-hero-title {
    font-family: 'Bebas Neue', sans-serif !important;
    letter-spacing: .05em;
    line-height: 1.15 !important;
    text-transform: uppercase;
}
h1 { font-size: 2.8rem !important; color: #ffffff !important; }
h2 { font-size: 2.1rem !important; color: var(--lime) !important; }
h3 { font-size: 1.7rem !important; color: var(--cyan) !important; }
h4 { font-size: 1.35rem !important; color: var(--amber) !important; }
.main-title, .section-title { font-family: 'Bebas Neue', sans-serif !important; color: #fff; letter-spacing: .05em; }
hr { border: 0; height: 3px; background: linear-gradient(90deg, var(--lime), transparent); }

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, var(--navy-900), var(--navy-700));
    border-right: 4px solid var(--lime);
}
[data-testid="stSidebar"] h1 { font-size: 2rem !important; color: var(--lime) !important; }
[data-testid="stSidebar"] [role="radiogroup"] label {
    background: rgba(255,255,255,.05);
    border-left: 5px solid transparent;
    border-radius: 4px;
    padding: 6px 10px;
    margin-bottom: 6px;
    width: 100%;
    transition: all .15s ease;
}
[data-testid="stSidebar"] [role="radiogroup"] label:hover {
    background: rgba(24,200,255,.18);
    border-left-color: var(--cyan);
}
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
    background: rgba(198,255,0,.16);
    border-left-color: var(--lime);
}

/* ---------- Buttons: angled "scoreboard" buttons ---------- */
.stButton > button, .stDownloadButton > button, [data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, var(--lime), #8fd400);
    color: #0b1426;
    border: 0;
    border-radius: 0;
    clip-path: polygon(0 0, 100% 0, calc(100% - 14px) 100%, 0 100%);
    padding: .6rem 1.7rem .6rem 1.1rem;
    font-weight: 700;
    transition: transform .12s ease, filter .12s ease;
}
.stButton > button p, .stDownloadButton > button p {
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 1.25rem !important;
    letter-spacing: .06em;
    color: #0b1426 !important;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    background: linear-gradient(135deg, var(--orange), #ff9a1a);
    transform: translateY(-2px);
    filter: drop-shadow(0 4px 8px rgba(255,107,26,.5));
}
.stButton > button:active { transform: translateY(1px); }

/* ---------- Inputs ---------- */
.stTextInput input, .stTextArea textarea, .stNumberInput input {
    background: #0a1020 !important;
    color: #fff !important;
    border: 2px solid var(--navy-600) !important;
    border-radius: 8px !important;
}
.stTextInput input:focus, .stTextArea textarea:focus { border-color: var(--lime) !important; box-shadow: 0 0 0 2px rgba(198,255,0,.25) !important; }
[data-baseweb="select"] > div {
    background: #0a1020 !important;
    border: 2px solid var(--navy-600) !important;
    border-radius: 8px !important;
}

/* ---------- Metrics = LED scoreboard digits ---------- */
[data-testid="stMetric"] {
    background-color: #05080f;
    background-image: radial-gradient(rgba(255,255,255,.05) 1px, transparent 1px);
    background-size: 4px 4px;
    border: 2px solid #222c40;
    border-top: 4px solid var(--amber);
    border-radius: 6px;
    padding: 12px 16px;
}
[data-testid="stMetric"] label, [data-testid="stMetric"] p { color: var(--muted) !important; text-transform: uppercase; letter-spacing: .08em; font-size: .95rem !important; }
[data-testid="stMetricValue"], [data-testid="stMetricValue"] * {
    font-family: 'Orbitron', monospace !important;
    color: var(--amber) !important;
    font-size: 1.6rem !important;
    text-shadow: 0 0 10px rgba(255,179,0,.55);
}

/* ---------- Alerts, images, expanders, tabs, progress ---------- */
[data-testid="stAlert"] { border-radius: 6px !important; border-left: 6px solid var(--lime) !important; }
[data-testid="stImage"] img { border-radius: 8px; border: 2px solid var(--navy-600); }
[data-testid="stDataFrame"] { border: 2px solid var(--navy-600); border-radius: 6px; }
[data-testid="stExpander"] { border: 1px solid var(--navy-600); border-radius: 8px; background: rgba(18,33,61,.55); }
[data-baseweb="tab"] { font-family: 'Bebas Neue', sans-serif !important; font-size: 1.3rem !important; letter-spacing: .06em; }
[data-baseweb="tab-highlight"] { background-color: var(--lime) !important; height: 4px !important; }
[data-testid="stProgress"] > div > div > div > div { background: linear-gradient(90deg, var(--lime), var(--cyan)); }

/* ---------- Chat bubbles ---------- */
[data-testid="stChatMessage"] {
    background: rgba(27,51,88,.55);
    border: 1px solid var(--navy-600);
    border-left: 5px solid var(--cyan);
    border-radius: 10px;
}
[data-testid="stChatInput"] textarea { background: #0a1020 !important; }

/* ---------- Scrollbar ---------- */
::-webkit-scrollbar { width: 12px; height: 12px; }
::-webkit-scrollbar-track { background: var(--navy-900); }
::-webkit-scrollbar-thumb { background: var(--navy-600); border-radius: 6px; border: 2px solid var(--navy-900); }
::-webkit-scrollbar-thumb:hover { background: var(--lime); }

/* =====================================================
   Reusable components (used by pages_extra.py)
   ===================================================== */

/* Scoreboard stat tiles */
.cc-stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 12px; margin: 10px 0 22px 0; }
.cc-stat {
    background-color: #05080f;
    background-image: radial-gradient(rgba(255,255,255,.05) 1px, transparent 1px);
    background-size: 4px 4px;
    border: 2px solid #222c40; border-top: 4px solid var(--amber);
    border-radius: 6px; padding: 12px 8px; text-align: center;
}
.cc-stat-num { font-family: 'Orbitron', monospace !important; font-size: 1.9rem; color: var(--amber) !important; text-shadow: 0 0 12px rgba(255,179,0,.6); }
.cc-stat-lab { font-family: 'Bebas Neue', sans-serif !important; font-size: 1.15rem; letter-spacing: .1em; color: var(--muted) !important; }

/* Generic card */
.cc-card {
    background: linear-gradient(145deg, var(--navy-700), #0d1a30);
    border: 1px solid var(--navy-600); border-left: 5px solid var(--lime);
    border-radius: 8px; padding: 16px 18px; height: 100%;
    transition: transform .15s ease, box-shadow .15s ease;
}
.cc-card:hover { transform: translateY(-4px); box-shadow: 0 10px 24px rgba(198,255,0,.18); }
.cc-card-icon { font-size: 2rem; }
.cc-card-title { font-family: 'Bebas Neue', sans-serif !important; font-size: 1.6rem; color: #fff !important; letter-spacing: .05em; }
.cc-card-text { color: var(--muted) !important; font-size: 1.1rem; line-height: 1.3; }

/* Player-card style datasheet */
.cc-tooltip {
    background: linear-gradient(160deg, #10203d, #0a1226);
    border: 1px solid var(--navy-600); border-top: 6px solid var(--lime);
    border-radius: 8px; padding: 16px 20px;
}
.cc-tooltip-title { font-family: 'Bebas Neue', sans-serif !important; font-size: 2.4rem; color: #fff !important; letter-spacing: .05em; line-height: 1.1; }
.cc-tooltip-sub { font-family: 'Orbitron', monospace !important; color: var(--cyan) !important; font-size: 1rem; margin-bottom: 6px; }
.cc-tooltip-note { color: var(--text) !important; font-size: 1.15rem; margin-top: 8px; font-style: italic; }
.cc-row { display: flex; justify-content: space-between; align-items: baseline; padding: 7px 0; border-bottom: 1px dashed rgba(159,179,217,.3); }
.cc-row:last-child { border-bottom: 0; }
.cc-row-key { color: var(--muted) !important; text-transform: uppercase; letter-spacing: .06em; font-size: 1rem; }
.cc-row-val { font-family: 'Orbitron', monospace !important; color: var(--amber) !important; font-size: 1rem; text-align: right; }

/* Chips and badges */
.cc-chip { display: inline-block; margin: 3px 4px 3px 0; padding: 2px 14px; border: 2px solid var(--lime); border-radius: 999px; background: rgba(198,255,0,.10); color: #fff !important; font-size: 1.05rem; font-weight: 600; }
.cc-badge { display: inline-block; padding: 1px 12px; border-radius: 4px; font-family: 'Orbitron', monospace !important; font-size: .85rem; letter-spacing: .08em; color: #05080f !important; font-weight: 800; }
.cc-badge-gas { background: var(--cyan); }
.cc-badge-liquid { background: #4d8dff; }
.cc-badge-solid { background: #c9d3e8; }

/* =====================================================
   Hero scoreboard banner
   ===================================================== */
.cc-hero {
    position: relative; overflow: hidden;
    display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 22px;
    padding: 30px 30px 34px 30px; margin-bottom: 22px;
    background:
        repeating-linear-gradient(90deg, transparent 0 78px, rgba(255,255,255,.05) 78px 80px),
        linear-gradient(135deg, #12306a, #0a1630 70%);
    border: 1px solid var(--navy-600); border-top: 6px solid var(--lime); border-radius: 8px;
}
.cc-hero::after {   /* running-track lanes along the bottom */
    content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 16px;
    background: repeating-linear-gradient(180deg, #d4572a 0 4px, rgba(255,255,255,.85) 4px 5px);
    opacity: .85;
}
.cc-hero-main { display: flex; align-items: center; gap: 22px; z-index: 1; }
.cc-medal { width: 92px; height: auto; transform-origin: 50% 0; animation: cc-swing 3.2s ease-in-out infinite; filter: drop-shadow(0 6px 10px rgba(0,0,0,.5)); }
@keyframes cc-swing { 0%,100% { transform: rotate(-7deg); } 50% { transform: rotate(7deg); } }
.cc-live { display: inline-flex; align-items: center; gap: 8px; font-family: 'Orbitron', monospace !important; font-size: .8rem; letter-spacing: .15em; color: #fff !important; background: rgba(255,59,59,.18); border: 1px solid var(--red); padding: 2px 12px; border-radius: 4px; }
.cc-live-dot { width: 10px; height: 10px; border-radius: 50%; background: var(--red); animation: cc-blink 1.1s infinite; }
@keyframes cc-blink { 0%,100% { opacity: 1; } 50% { opacity: .15; } }
.cc-hero-title { font-size: 4.2rem; color: #fff !important; line-height: 1 !important; margin: 8px 0 0 0; text-shadow: 3px 3px 0 rgba(0,0,0,.45); }
.cc-hero-title span { color: var(--lime); }
.cc-hero-sub { font-family: 'Bebas Neue', sans-serif !important; font-size: 1.7rem; letter-spacing: .12em; color: var(--amber) !important; }
.cc-hero-by { color: var(--muted) !important; font-size: 1.05rem; margin-top: 4px; }
.cc-board { display: flex; gap: 10px; z-index: 1; }
.cc-board-cell {
    background-color: #05080f; background-image: radial-gradient(rgba(255,255,255,.05) 1px, transparent 1px); background-size: 4px 4px;
    border: 2px solid #222c40; border-radius: 6px; padding: 8px 14px; text-align: center; min-width: 92px;
}
.cc-board-num { font-family: 'Orbitron', monospace !important; font-size: 2rem; font-weight: 800; color: var(--amber) !important; text-shadow: 0 0 12px rgba(255,179,0,.7); }
.cc-board-lab { font-family: 'Bebas Neue', sans-serif !important; letter-spacing: .12em; font-size: 1rem; color: var(--muted) !important; }
.cc-splash {
    position: absolute; right: 18px; top: 14px; transform: rotate(8deg); z-index: 2;
    background: var(--orange); color: #fff !important; font-family: 'Bebas Neue', sans-serif !important;
    font-size: 1.2rem; letter-spacing: .1em; padding: 2px 16px; clip-path: polygon(0 0, 100% 0, calc(100% - 10px) 100%, 0 100%);
    animation: cc-pulse 1.6s ease-in-out infinite;
}
@keyframes cc-pulse { 0%,100% { transform: rotate(8deg) scale(1); } 50% { transform: rotate(8deg) scale(1.1); } }
@media (max-width: 760px) {
    .cc-hero-title { font-size: 2.8rem; }
    .cc-hero-main { flex-direction: column; text-align: center; }
    .cc-board { width: 100%; justify-content: center; }
    .block-container { padding: 1.2rem 1rem 2rem 1rem !important; }
}
</style>
"""


def _medal_data_uri():
    """A small gold-medal SVG, embedded as a data URI so no image file is needed."""
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 125">'
        '<polygon points="26,0 48,0 58,52 36,52" fill="#e63946"/>'
        '<polygon points="74,0 52,0 42,52 64,52" fill="#1d6fff"/>'
        '<circle cx="50" cy="84" r="32" fill="#ffc300" stroke="#b8860b" stroke-width="5"/>'
        '<circle cx="50" cy="84" r="23" fill="none" stroke="#b8860b" stroke-width="3"/>'
        '<text x="50" y="95" text-anchor="middle" font-size="30" font-weight="bold" '
        'font-family="Arial, sans-serif" fill="#b8860b">1</text>'
        '</svg>'
    )
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


def hero(title_main, title_accent, subtitle, byline, stats, splash="Game on!"):
    """
    Build the scoreboard banner HTML (kept on ONE line - Streamlit's markdown
    would treat indented / blank-line HTML as a code block).

    stats: list of (number, label) tuples shown on the little scoreboard.
    """
    cells = "".join(
        f'<div class="cc-board-cell"><div class="cc-board-num">{html.escape(str(n))}</div>'
        f'<div class="cc-board-lab">{html.escape(l)}</div></div>'
        for n, l in stats
    )
    return (
        '<div class="cc-hero">'
        f'<div class="cc-splash">{html.escape(splash)}</div>'
        '<div class="cc-hero-main">'
        f'<img class="cc-medal" src="{_medal_data_uri()}" alt="medal">'
        '<div>'
        '<div class="cc-live"><span class="cc-live-dot"></span>LIVE LAB</div>'
        f'<div class="cc-hero-title">{html.escape(title_main)}<span> {html.escape(title_accent)}</span></div>'
        f'<div class="cc-hero-sub">{html.escape(subtitle)}</div>'
        f'<div class="cc-hero-by">{html.escape(byline)}</div>'
        '</div></div>'
        f'<div class="cc-board">{cells}</div>'
        '</div>'
    )


def apply_sports_theme():
    """Inject the sports CSS into the page."""
    st.markdown(SPORTS_CSS, unsafe_allow_html=True)
