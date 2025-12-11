from fastapi import FastAPI
import numpy as np
import pandas as pd

app = FastAPI()

df = pd.read_parquet("products.parquet")
cosine_sim = np.load("cosine_sim.npy")

ID_COL = "Uniq Id"


@app.get("/products")
def list_products():
    return df[[ID_COL, "Product Image Url"]].to_dict(orient="records")


@app.get("/recommend")
def recommend(product_id: str, top_k: int = 6):
    idx = df.index[df[ID_COL] == product_id].tolist()[0]
    
    scores = list(enumerate(cosine_sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:top_k+1]

    indices = [i[0] for i in scores]

    return df.loc[indices, [
        ID_COL,
        "Product Image Url"
    ]].to_dict(orient="records")
