import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

index = faiss.read_index("file_index.index")
with open("paths_and_names.txt", "r") as f:
    paths_and_names = [line.strip().split('\t') for line in f]
    paths = [x[0] for x in paths_and_names]
    names = [x[1] for x in paths_and_names]

model = SentenceTransformer('all-MiniLM-L6-v2')

while True:
    query = input("Enter search term (or type 'exit' to quit): ").strip()
    if query.lower() == 'exit':
        print("Exiting the search.")
        break

    query_embedding = model.encode([query])

    _, indices = index.search(np.array(query_embedding), k=5)  # k is the number of top results you want

    print(f"\nTop {len(indices[0])} results for '{query}':")
    for idx in indices[0]:
        print(f"Name: {names[idx]}, Path: {paths[idx]}")
    
    print("\n" + "-"*50 + "\n")
