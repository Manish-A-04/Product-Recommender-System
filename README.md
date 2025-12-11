# 📦 Product Recommender System

A content-based product recommender system using TF-IDF and cosine similarity to suggest similar items based on product tags and metadata. Built with FastAPI for fast recommendations and Streamlit for an interactive, paginated image-based browsing experience.

---

## 🚀 Features

* Content-based recommendation using TF-IDF
* Cosine similarity-based product matching
* FastAPI backend with clean API endpoints
* Streamlit UI with paginated image gallery
* Clickable product images for instant recommendations
* Lightweight, fast, and easy to extend

---

## 🏗 Project Structure

```
/product-recommender-system
│
├── api.py                 # FastAPI backend
├── app.py                 # Streamlit frontend
├── products.parquet       # Preprocessed dataset
├── cosine_sim.npy         # Cosine similarity matrix
├── tfidf_vectorizer.pkl   # TF-IDF model
└── README.md
```

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Backend

```bash
uvicorn api:app --reload --port 8000
```

Backend runs at:

```
http://localhost:8000
```

---

## ▶️ Running the Streamlit UI

```bash
streamlit run app.py
```

UI opens at:

```
http://localhost:8501
```

---

## 🧪 API Endpoints

| Route                       | Description                           |
| --------------------------- | ------------------------------------- |
| `/products`                 | Returns all products (ID + image URL) |
| `/recommend?product_id=XYZ` | Returns similar products              |

---

## 🎯 How It Works

1. TF-IDF is applied on product tags and company metadata
2. Cosine similarity matrix is computed and saved
3. FastAPI serves products and recommendations
4. Streamlit displays products in a 3×2 image grid
5. Clicking a product fetches and displays similar items

---

## 📌 Future Improvements

* Add Sentence-BERT embeddings
* Add search or filtering features
* Add product description popup

---