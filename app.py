import streamlit as st
from datetime import datetime

# -----------------------------
# Thời điểm mở thư: 00:00 ngày 7/1/2026 UTC
# -----------------------------
TARGET_TIME = 1767744000  # Unix timestamp: 2026-01-07 00:00:00 UTC
PASSWORD = "cunnucheomap"  # Mật khẩu để mở sớm

# -----------------------------
# Streamlit config
# -----------------------------
st.set_page_config(page_title="Bức Thư Dành Cho Em", layout="centered")

# -----------------------------
# CSS đẹp như thư tay thật
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
        font-size: 20px;
        line-height: 1.8;
        color: #3d2817;
        white-space: pre-line;
    }
    .signature {
        text-align: right;
        font-family: 'Dancing Script', cursive;
        font-size: 36px;
        color: #c0392b;
        margin-top: 60px;
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
        color: #7f4f24;
        font-style: italic;
    }
    .photo-gallery {
        margin-top: 60px;
        columns: 2;
        column-gap: 20px;
    }
    .photo-item {
        break-inside: avoid;
        margin-bottom: 20px;
        border: 8px solid #fff;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        border-radius: 5px;
        overflow: hidden;
    }
    .password-box {
        max-width: 400px;
        margin: 30px auto;
    }
</style>
""", unsafe_allow_html=True)

# Font chữ viết tay đẹp (Google Fonts)
st.markdown('<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&display=swap" rel="stylesheet">', unsafe_allow_html=True)

# -----------------------------
# Kiểm tra thời gian và mật khẩu
# -----------------------------
current_time = int(datetime.utcnow().timestamp())
time_reached = current_time >= TARGET_TIME

# Sử dụng session_state để lưu trạng thái đã mở bằng password
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

# Nếu đã unlock bằng password hoặc đã đến giờ → hiển thị thư
if st.session_state.unlocked or time_reached:
    # Hiển thị bức thư đầy đủ
    st.markdown("""
    <div class="letter-container">
        <h1 class="title">💌 Dành riêng cho em yêu của anh</h1>
        <p class="date">Ngày 7 tháng 1 năm 2026</p>
    """, unsafe_allow_html=True)

    default_letter = """Em yêu dấu,

Hôm nay là một ngày rất đặc biệt với anh. Đã lâu rồi anh muốn nói với em những điều này, nhưng anh muốn chờ đến đúng khoảnh khắc hoàn hảo nhất.

Em chính là điều tuyệt vời nhất từng đến trong cuộc đời anh. Mỗi ngày bên em đều là một món quà, mỗi nụ cười của em đều làm tim anh tan chảy.

Anh nhớ những buổi tối mình cùng nhau đi dạo, những lần em giận dỗi rồi lại làm hòa bằng một cái ôm thật chặt. Anh nhớ cách em cười, cách em gọi tên anh, và cả cách em ngủ gật trên vai anh nữa.

Cảm ơn em vì đã ở bên anh, vì đã yêu anh bằng cả trái tim. Anh hứa sẽ luôn cố gắng để trở thành người xứng đáng với tình yêu của em.

Anh yêu em, hôm nay, ngày mai, và mãi mãi về sau.

Với tất cả tình yêu của anh,"""

    message = st.text_area(
        "",
        value=default_letter,
        height=600,
        label_visibility="collapsed",
        key="letter_content"
    )

    st.markdown(f'<p class="content">{message}</p>', unsafe_allow_html=True)

    st.markdown('<p class="signature">Anh của em ❤️</p>', unsafe_allow_html=True)
       # Phần ảnh kỷ niệm - HIỂN THỊ SẴN (không cần upload)
    st.markdown('<h2 style="text-align: center; color: #c0392b; font-family: Dancing Script, cursive; font-size: 36px; margin-top: 80px;">Kỷ niệm đẹp của chúng mình</h2>', unsafe_allow_html=True)

    # Danh sách tên file ảnh bạn đã chuẩn bị sẵn (thêm/bớt tùy ý)
    photo_files = [
        # thêm bao nhiêu cũng được, chỉ cần file tồn tại trong thư mục
    ]

    if photo_files:
        st.markdown('<div class="photo-gallery">', unsafe_allow_html=True)
        for photo in photo_files:
            try:
                st.markdown('<div class="photo-item">', unsafe_allow_html=True)
                st.image(photo, use_column_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            except:
                pass  # nếu file không tồn tại thì bỏ qua, không lỗi
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("Chưa có ảnh kỷ niệm nào được thêm.")

    st.markdown('</div>', unsafe_allow_html=True)  # Đóng letter-container

else:
    # Chưa đến giờ và chưa unlock → hiển thị màn hình chờ + ô nhập password
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

    # Ô nhập mật khẩu để mở sớm
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

    # Auto refresh mỗi giây để cập nhật countdown
    import time
    time.sleep(1)
    st.rerun()