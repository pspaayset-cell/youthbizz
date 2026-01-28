import streamlit as st

# =====================
# KONFIGURASI AWAL
# =====================
st.set_page_config(
    page_title="YouthBizz",
    page_icon="🐝",
    layout="centered"
)

# =====================
# SESSION STATE
# =====================
if "posts" not in st.session_state:
    st.session_state.posts = []

if "saved" not in st.session_state:
    st.session_state.saved = []

if "likes" not in st.session_state:
    st.session_state.likes = {}

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "username" not in st.session_state:
    st.session_state.username = "username_1"

# =====================
# HEADER
# =====================
st.markdown(
    """
    <div style="background-color:#FFD700;padding:15px;border-radius:10px;text-align:center;">
        <h1>🐝 YouthBizz</h1>
        <p>Wadah Bisnis Kreatif Siswa</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# =====================
# NAVIGASI
# =====================
menu = st.columns(5)
if menu[0].button("🏠"):
    st.session_state.page = "Home"
if menu[1].button("🔍"):
    st.session_state.page = "Search"
if menu[2].button("➕"):
    st.session_state.page = "Upload"
if menu[3].button("🔖"):
    st.session_state.page = "Saved"
if menu[4].button("👤"):
    st.session_state.page = "Profile"

st.write("---")

# =====================
# HOME / FEED
# =====================
if st.session_state.page == "Home":
    st.subheader("📢 Feed Produk")

    if len(st.session_state.posts) == 0:
        st.info("Belum ada postingan.")
    else:
        for i, post in enumerate(reversed(st.session_state.posts)):
            st.markdown(f"**👤 {post['user']}**")
            st.image(post["image"], use_column_width=True)
            st.write(post["desc"])
            st.markdown(f"### 💰 Rp{post['price']:,}".replace(",", "."))

            col1, col2 = st.columns(2)

            # LIKE
            like_count = st.session_state.likes.get(i, 0)
            if col1.button(f"❤️ {like_count}", key=f"like{i}"):
                st.session_state.likes[i] = like_count + 1

            # SAVE
            if col2.button("🔖 Simpan", key=f"save{i}"):
                st.session_state.saved.append(post)
                st.success("Disimpan!")

            st.write("---")

# =====================
# SEARCH
# =====================
elif st.session_state.page == "Search":
    st.subheader("🔍 Pencarian Produk")
    keyword = st.text_input("Masukkan kata kunci")

    for post in st.session_state.posts:
        if keyword.lower() in post["desc"].lower():
            st.markdown(f"**👤 {post['user']}**")
            st.image(post["image"], use_column_width=True)
            st.write(post["desc"])
            st.markdown(f"### 💰 Rp{post['price']:,}".replace(",", "."))
            st.write("---")

# =====================
# UPLOAD
# =====================
elif st.session_state.page == "Upload":
    st.subheader("➕ Upload Produk")

    image = st.file_uploader("Pilih gambar produk", type=["jpg", "png", "jpeg"])
    desc = st.text_area("Masukkan deskripsi produk")
    link = st.text_input("Masukkan tautan (opsional)")
    price = st.number_input("Masukkan harga", min_value=0)

    if st.button("📤 Upload"):
        if image and desc and price > 0:
            with st.spinner("Mengupload..."):
                time.sleep(2)
            st.session_state.posts.append({
                "user": st.session_state.username,
                "image": image,
                "desc": desc,
                "link": link,
                "price": int(price)
            })
            st.success("✅ Postingan berhasil!")
        else:
            st.warning("Lengkapi semua data!")

# =====================
# SAVED
# =====================
elif st.session_state.page == "Saved":
    st.subheader("🔖 Postingan Disimpan")

    if len(st.session_state.saved) == 0:
        st.info("Belum ada postingan disimpan.")
    else:
        for post in st.session_state.saved:
            st.markdown(f"**👤 {post['user']}**")
            st.image(post["image"], use_column_width=True)
            st.write(post["desc"])
            st.markdown(f"### 💰 Rp{post['price']:,}".replace(",", "."))
            st.write("---")

# =====================
# PROFILE
# =====================
elif st.session_state.page == "Profile":
    st.subheader("👤 Profil Akun")

    st.write(f"**Username:** {st.session_state.username}")
    st.write(f"**Total Postingan:** {len(st.session_state.posts)}")
    st.write(f"**Postingan Disimpan:** {len(st.session_state.saved)}")

    st.write("---")
    st.write("📦 Postingan Saya")

    for post in st.session_state.posts:
        if post["user"] == st.session_state.username:
            st.image(post["image"], use_column_width=True)
            st.write(post["desc"])
            st.markdown(f"### 💰 Rp{post['price']:,}".replace(",", "."))
            st.write("---")
