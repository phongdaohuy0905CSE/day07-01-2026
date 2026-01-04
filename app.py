import streamlit as st
from datetime import datetime
import time

# -----------------------------
# Thời điểm mở thư: 00:00 ngày 7/1/2026 UTC
# -----------------------------
TARGET_TIME = 1767744000
PASSWORD = "cunnucheomap"

# -----------------------------
# Streamlit config
# -----------------------------
st.set_page_config(page_title="Bức Thư Dành Cho Em", layout="centered")

# -----------------------------
# CSS đẹp như thư tay + responsive cho mobile
# -----------------------------
st.markdown("""
<style>
    .letter-container {
        max-width: 800px;
        margin: 0 auto;
        background: linear-gradient(to bottom, #fff8e1, #fefce8);
        border: 12px solid #8b4513;
        border-radius: 10px;
        padding: 60px 80px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        min-height: 100vh;
        font-family: 'Georgia', serif;
        position: relative;
    }
    .letter-container::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: url('https://www.transparenttextures.com/patterns/old-wall.png');
        opacity: 0.07;
        pointer-events: none;
    }
    .title {
        font-family: 'Dancing Script', cursive;
        font-size: 52px;
        color: #c0392b;
        text-align: center;
        margin-bottom: 40px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .date {
        text-align: right;
        font-style: italic;
        color: #7f4f24;
        margin-bottom: 50px;
        font-size: 18px;
    }
    .content {
        font-size: 21px;
        line-height: 2;
        color: #3d2817;
        white-space: pre-line;
        text-align: justify;
    }
    .signature {
        text-align: right;
        font-family: 'Dancing Script', cursive;
        font-size: 42px;
        color: #c0392b;
        margin-top: 80px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .countdown {
        font-family: 'Courier New', monospace;
        font-size: 48px;
        color: #c0392b;
        text-align: center;
        margin: 100px 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .waiting-message {
        font-size: 28px;
        text-align: center;
        color: #000000;  /* Đổi thành đen đậm */
        font-style: italic;
        font-weight: bold;
    }
    .password-box {
        max-width: 400px;
        margin: 30px auto;
    }

    /* Responsive tựa đề trên mobile (iPhone 16 Pro Max và các màn nhỏ) */
    @media (max-width: 600px) {
        .title {
            font-size: 36px !important;  /* Nhỏ lại để vừa màn hình mobile */
            margin-bottom: 30px;
        }
        .letter-container {
            padding: 40px 30px;  /* Giảm padding cho mobile thoải mái hơn */
        }
        .content {
            font-size: 19px;
        }
        .countdown {
            font-size: 36px;
        }
        .waiting-message {
            font-size: 24px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Font chữ tay
st.markdown('<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&display=swap" rel="stylesheet">', unsafe_allow_html=True)

# -----------------------------
# Logic thời gian + password
# -----------------------------
current_time = int(datetime.utcnow().timestamp())
time_reached = current_time >= TARGET_TIME

if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

if st.session_state.unlocked or time_reached:
    # ==================== HIỂN THỊ BỨC THƯ ====================
    letter_content = """Em yêu dấu của anh,

Từ rất lâu rồi, anh đã muốn viết cho em những dòng này, nhưng anh chờ mãi đến một ngày thật đặc biệt – ngày mà tình yêu của chúng mình thêm trọn vẹn và sâu đậm hơn.

Em chính là ánh nắng ấm áp nhất trong cuộc đời anh. Mỗi buổi sáng thức dậy nghĩ đến em, tim anh lại rộn ràng. Mỗi nụ cười của em đều làm anh tan chảy, mỗi cái ôm của em đều xua tan mọi mệt mỏi.

Anh nhớ da diết những buổi tối mình nắm tay nhau đi dạo dưới ánh đèn đường, những lần em giận hờn rồi lại chạy đến ôm anh thật chặt để làm hòa. Anh nhớ cách em gọi "anh ơi" ngọt ngào, nhớ cả những lúc em ngủ gật trên vai anh, hơi thở đều đều khiến anh chỉ muốn thời gian ngừng trôi.

Cảm ơn em vì đã đến bên anh, vì đã yêu anh bằng cả trái tim trong trẻo và chân thành nhất. Anh hứa sẽ mãi che chở, yêu thương và cố gắng mỗi ngày để xứng đáng với em – cô gái tuyệt vời nhất mà anh may mắn có được.

Anh yêu em, yêu nhiều lắm, hôm nay, ngày mai, và mãi mãi về sau... Không gì có thể thay đổi điều đó.

Với tất cả tình yêu và nhớ nhung,"""

    edited_content = st.text_area("", value=letter_content, height=700, label_visibility="collapsed", key="letter_content")

    st.markdown(f"""
    <div class="letter-container">
        <h1 class="title">💌 Dành riêng cho em yêu của anh</h1>
        <p class="date">Ngày 7 tháng 1 năm 2026</p>
        <p class="content">{edited_content}</p>
        <p class="signature">Cún Nù ❤️</p>
    </div>
    """, unsafe_allow_html=True)

else:
    # ==================== MÀN HÌNH CHỜ + PASSWORD ====================
    remaining = TARGET_TIME - current_time
    days = remaining // 86400
    hours = (remaining % 86400) // 3600
    minutes = (remaining % 3600) // 60
    seconds = remaining % 60

    st.markdown(f"""
    <div class="letter-container">
        <h1 class="title">💌 Bức Thư Bí Mật</h1>
        <p class="waiting-message">Em yêu dấu,</p>
        <p class="waiting-message">Anh đã chuẩn bị một điều đặc biệt dành riêng cho em...</p>
        <p class="waiting-message">Hãy chờ thêm chút nữa nhé ❤️</p>
        <div class="countdown">
            {days} ngày {hours:02d}:{minutes:02d}:{seconds:02d}
        </div>
        <p class="waiting-message">Thư sẽ mở đúng vào 0:00 ngày 7 tháng 1 năm 2026</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="password-box">', unsafe_allow_html=True)
    password_input = st.text_input("Nếu em có mật khẩu đặc biệt, hãy nhập ở đây để mở thư ngay nhé 💕", type="password")
    if st.button("Mở thư"):
        if password_input.strip().lower() == PASSWORD.lower():
            st.session_state.unlocked = True
            st.success("Mật khẩu đúng! Đang mở bức thư cho em... ❤️")
            st.rerun()
        else:
            st.error("Mật khẩu chưa đúng rồi, thử lại nhé em yêu 😘")
    st.markdown('</div>', unsafe_allow_html=True)

    time.sleep(1)
    st.rerun()
