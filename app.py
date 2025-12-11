import streamlit as st
import requests
import math
from io import BytesIO
from PIL import Image
import base64

FASTAPI = "http://localhost:8000"

st.set_page_config(layout="wide")
st.title("Product Recommender System")


@st.cache_data
def load_products():
    r = requests.get(f"{FASTAPI}/products")
    return r.json()

products = load_products()


@st.cache_data
def resize_to_base64(url, size=(250, 250)):
    try:
        r = requests.get(url, timeout=4)
        img = Image.open(BytesIO(r.content)).convert("RGB")
        img = img.resize(size, Image.LANCZOS)

        buf = BytesIO()
        img.save(buf, format="JPEG")
        b64 = base64.b64encode(buf.getvalue()).decode()
        return f"data:image/jpeg;base64,{b64}"
    except:
        return None


IMAGES_PER_PAGE = 6
TOTAL_PAGES = math.ceil(len(products) / IMAGES_PER_PAGE)

page = st.number_input("Page", min_value=1, max_value=TOTAL_PAGES, value=1)
start = (page - 1) * IMAGES_PER_PAGE
end = start + IMAGES_PER_PAGE
page_products = products[start:end]

st.write(f"Page {page}/{TOTAL_PAGES}")


st.markdown("""
<style>
.product-image {
    border-radius: 12px;
    transition: 0.25s;
}
.product-image:hover {
    transform: scale(1.05);
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)


clicked_id = st.session_state.get("clicked_id")

rows, cols = 2, 3
index = 0

for r in range(rows):
    columns = st.columns(cols)
    for c in range(cols):
        if index >= len(page_products):
            break

        product = page_products[index]
        product_id = product["Uniq Id"]
        image_url = product["Product Image Url"].split("|")[0].strip()

        base64_img = resize_to_base64(image_url)

        if base64_img:
            html = f"""
            <form action="" method="get">
                <input type="hidden" name="pid" value="{product_id}">
                <button style="border:none;background:none;padding:0;">
                    <img src="{base64_img}" width="250" class="product-image">
                </button>
            </form>
            """
            columns[c].markdown(html, unsafe_allow_html=True)

        index += 1
    st.markdown("<div style='margin-top:40px;'></div>", unsafe_allow_html=True)

query = st.query_params
if "pid" in query:
    st.session_state["clicked_id"] = query["pid"]
    clicked_id = query["pid"]


if clicked_id:
    st.subheader("Similar Products")

    rec = requests.get(f"{FASTAPI}/recommend", params={"product_id": clicked_id}).json()

    rec_cols = st.columns(3)
    for i, item in enumerate(rec):
        img_url = item["Product Image Url"].split("|")[0].strip()
        img64 = resize_to_base64(img_url)
        if img64:
            rec_cols[i % 3].image(img64, width=250)
