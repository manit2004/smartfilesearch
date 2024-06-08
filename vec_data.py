import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

df = pd.read_csv("file_list.csv")
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(df['Name'].tolist())

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))
paths = df['FullName'].tolist()
names = df['Name'].tolist()

faiss.write_index(index, "file_index.index")
with open("paths_and_names.txt", "w") as f:
    for path, name in zip(paths, names):
        f.write(f"{path}\t{name}\n")
