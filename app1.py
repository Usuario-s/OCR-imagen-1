st.markdown("""
<style>

/* =========================
   FONDO DE AGUA
   ========================= */

.stApp {
    background:
        linear-gradient(
            180deg,
            #d9f8ff 0%,
            #8ed9e8 35%,
            #48b5c9 70%,
            #167d98 100%
        );

    overflow: hidden;
}

/* Ondas grandes */
.stApp::before {
    content: "";
    position: fixed;
    left: -10%;
    top: 0;
    width: 120%;
    height: 100%;

    background:
        repeating-radial-gradient(
            ellipse at 50% 100%,
            rgba(255,255,255,0.20) 0px,
            rgba(255,255,255,0.08) 3px,
            transparent 8px,
            transparent 25px
        );

    opacity: 0.45;
    pointer-events: none;

    animation: movimientoAgua 8s ease-in-out infinite;
}

/* Reflejos de luz */
.stApp::after {
    content: "";
    position: fixed;
    top: -20%;
    left: -30%;

    width: 160%;
    height: 140%;

    background:
        repeating-linear-gradient(
            100deg,
            transparent 0px,
            transparent 35px,
            rgba(255,255,255,0.12) 40px,
            transparent 48px,
            transparent 80px
        );

    opacity: 0.35;
    pointer-events: none;

    animation: reflejos 12s linear infinite;
}


/* =========================
   TÍTULO
   ========================= */

h1 {
    text-align: center;
    color: white;

    text-shadow:
        0px 2px 5px rgba(0,60,90,0.5),
        0px 0px 20px rgba(255,255,255,0.5);
}


/* =========================
   SIDEBAR
   ========================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            rgba(15,125,155,0.90),
            rgba(5,65,95,0.95)
        );

    backdrop-filter: blur(10px);
}


/* =========================
   CÁMARA
   ========================= */

[data-testid="stCameraInput"] {
    background: rgba(255,255,255,0.15);

    padding: 15px;

    border-radius: 20px;

    backdrop-filter: blur(10px);

    box-shadow:
        0 10px 30px rgba(0,60,90,0.30),
        inset 0 1px 10px rgba(255,255,255,0.35);
}


/* =========================
   TEXTO
   ========================= */

p, label, .stRadio label {
    color: white !important;
}


/* =========================
   ANIMACIONES
   ========================= */

@keyframes movimientoAgua {

    0% {
        transform:
            translateX(-3%)
            translateY(0px)
            scale(1);
    }

    50% {
        transform:
            translateX(3%)
            translateY(12px)
            scale(1.04);
    }

    100% {
        transform:
            translateX(-2%)
            translateY(-8px)
            scale(1.02);
    }
}


@keyframes reflejos {

    0% {
        transform: translateX(-10%);
    }

    50% {
        transform: translateX(10%);
    }

    100% {
        transform: translateX(-10%);
    }
}

</style>
""", unsafe_allow_html=True)
