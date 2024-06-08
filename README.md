# smartfilesearch

# Semantic Search for File Explorer

Traditional file explorer search tools rely on exact keyword matches to retrieve files and folders, often resulting in frustrating experiences when a user misspells, mistypes, or slightly deviates from the actual file or folder name. In such cases, finding the desired item becomes a tedious task.

This project introduces a novel approach to file exploration through semantic search capabilities. By harnessing the power of natural language processing and semantic embeddings, users can now search for files and folders in a directory with enhanced flexibility and accuracy. Unlike traditional search methods, which depend on precise matches, semantic search can understand the context and semantics of the query, enabling it to return relevant results even when there are spelling mistakes, missing spaces, or slight deviations in the query terms.

Key Features:
Flexibility: Users can input search queries in natural language, allowing for more intuitive and expressive searches.
Enhanced Relevance Ranking: Semantic search employs advanced algorithms to rank search results based on their semantic similarity to the query. This ensures that the most relevant files and folders are presented to the user at the top of the search results, improving the efficiency and effectiveness of the search process.
Robustness: Semantic search can handle spelling errors, missing spaces, and variations in query terms, ensuring robust search results.
Contextual Understanding: By understanding the context of the search query, semantic search can retrieve relevant files and folders even when the query is not an exact match.
Enhanced Exploration: Users can explore files and folders in a directory more efficiently and effectively, reducing the time and effort required to locate specific items.
With semantic search, the file exploration experience is transformed, offering users a more seamless and productive way to navigate through their files and folders.

## Requirements

- Python 3.x
- pandas
- sentence-transformers
- faiss

## Installation

1. Clone or download this repository to your local machine.
2. Install the required Python packages using pip:


## Usage

### 1. Generating File List and Index

1. Open the PowerShell script `powershell.ps1`.
2. Modify the `$directory` variable to specify the directory you want to scan.
3. Run the script. It will generate a CSV file (`file_list.csv`) containing the names and paths of all files and folders in the current working directory.

### 2. Building Index

1. Run the Python script `vec_data.py`. This script reads the CSV file generated in the previous step, generates embeddings for the file and folder names, builds a FAISS index, and saves the index along with the paths and names in a text file.

   
### 3. Performing Semantic Search

1. Run the Python script `search.py`. This script loads the FAISS index and allows you to perform semantic searches using natural language queries.
2. Enter a search term when prompted. The script will return the top 5 most relevant files and folders based on semantic similarity to your query.
3. Continue entering search terms until you want to exit. Type 'exit' to quit the search.

## Note

- Ensure that you have the necessary permissions to access the directories you want to scan.
- You can customize the search behavior by modifying the search query, the number of top results (`k`), and the embedding model in the `semantic_search.py` script.




