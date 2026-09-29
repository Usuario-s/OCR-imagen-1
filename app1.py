import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image


# ---------------- DISEÑO ----------------
st.markdown("""
<style>

.stApp {
    background:
        linear-gradient(
            180deg,
            #dff7ff 0%,
            #a8e5f2 25%,
            #70cbdc 50%,
            #4aaabd 75%,
            #258da5 100%
        );
    background-size: 100% 200%;
    animation: agua 8s ease-in-out infinite alternate;
}

/* Efecto de ondas/reflejos */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    background:
        repeating-linear-gradient(
            0deg,
            rgba(255,255,255,0.10) 0px,
            rgba(255,255,255,0.10) 2px,
            transparent 3px,
            transparent 12px
        );

    opacity: 0.5;
    pointer-events: none;

    animation: ondas 5s linear infinite;
}

/* Título */
h1 {
    text-align: center;
    color: white;
    font-weight: 700;
    text-shadow:
        0px 2px 4px rgba(0,80,110,0.5),
        0px 0px 15px rgba(255,255,255,0.4);
}

/* Texto */
p, label, .stRadio label {
    color: white !important;
}

/* Cámara */
[data-testid="stCameraInput"] {
    background: rgba(255,255,255,0.15);
    padding: 15px;
    border-radius: 20px;
    backdrop-filter: blur(8px);
    box-shadow:
        0 8px 25px rgba(0,70,100,0.25),
        inset 0 1px 8px rgba(255,255,255,0.35);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            rgba(20,130,160,0.85),
            rgba(10,80,110,0.9)
        );
}

/* Caja del texto reconocido */
.stText, .stMarkdown {
    text-shadow: 0px 1px 3px rgba(0,60,80,0.35);
}

/* Animación del agua */
@keyframes agua {
    from {
        background-position: 0% 0%;
    }

    to {
        background-position: 0% 100%;
    }
}

/* Movimiento de ondas */
@keyframes ondas {
    from {
        transform: translateY(0px);
    }

    to {
        transform: translateY(18px);
    }
}

</style>
""", unsafe_allow_html=True)


# ---------------- PROGRAMA ORIGINAL ----------------

st.title("Reconocimiento de imagen")

img_file_buffer = st.camera_input("Toma una Foto")

with st.sidebar:
      filtro = st.radio("Aplicar Filtro",('Con Filtro', 'Sin Filtro'))


if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(
        np.frombuffer(bytes_data, np.uint8),
        cv2.IMREAD_COLOR
    )
    
    if filtro == 'Con Filtro':
         cv2_img = cv2.bitwise_not(cv2_img)
    else:
         cv2_img = cv2_img
    
        
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img_rgb)
    st.write(text)
