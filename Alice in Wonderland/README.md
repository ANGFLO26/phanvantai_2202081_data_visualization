                 Analysis of Alice in Wonderland Using NLP and Data Visualization
Objective:
- This script is designed to process the text from Alice in Wonderland and utilize Natural Language Processing (NLP) techniques combined with data visualization methods to understand the structure and meaning of words in the text. The main objectives include:

       1. Clean and preprocess the text.

       2. Visualize word frequencies using Word Cloud and Bar Chart.

       3. Plot semantic relationships between words using GloVe embeddings and PCA.

       4. Display word similarities using a Heatmap.

Requirements:
- Python (any version that supports the libraries)
- Required libraries:
        "pip install nltk matplotlib wordcloud gensim numpy scikit-learn seaborn"
- Input file named Alice in Wonderland.txt (or a similar text).

Usage Instructions:
1. Read and Preprocess the Text
    - Read the text from the Alice in Wonderland.txt file.
    - Clean the text: Remove unnecessary parts like metadata, punctuation, and non-alphabetic characters.
    - Preprocess: Convert the text to lowercase, remove stopwords, and retain only meaningful words (no numbers or punctuation).

2. Analyze and Generate Word Frequencies
    - Tokenize: Split the text into individual words.
    - Remove Stopwords: Remove common words that do not carry significant meaning, such as "the", "and", "of", etc.
    - Lemmatization: Use WordNet Lemmatizer to reduce words to their base form (e.g., "running" → "run").

3. Visualize Word Frequencies
    - Word Cloud: Generate a Word Cloud to display the most frequent words in the text.
    - Bar Chart: Create a bar chart showing the top 20 most frequent words.

4. Plot Semantic Relationships Between Words
    - GloVe Embeddings: Use the GloVe model to obtain word vectors for the most frequent words in the text.
    - PCA: Apply Principal Component Analysis (PCA) to reduce the dimensionality of the word vectors and visualize the semantic relationships between them in a scatter plot.

5. Display Word Similarities
    - Cosine Similarity: Calculate cosine similarity between word vectors.
    - Heatmap: Generate a heatmap to visualize the similarity between words.

Output:
        - Word Cloud: A Word Cloud that displays the most frequent words in Alice in Wonderland.

        - Bar Chart: A bar chart displaying the top 20 most frequent lemmatized words.

        - Scatter Plot: A scatter plot showing the semantic relationships between words using PCA.

        - Heatmap: A heatmap showing the word similarity between the most frequent words.

Notes:

    - Ensure that the Alice in Wonderland.txt file is stored correctly and encoded in UTF-8 for the script to work properly.
    - This script uses the gensim library to load the GloVe model and the nltk library for preprocessing tasks.

Conclusion:
    -  This script enables the application of basic NLP techniques and data visualization methods to analyze a literary work, providing deeper insights into the vocabulary and semantic relationships within the text.