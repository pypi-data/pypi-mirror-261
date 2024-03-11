import os
import pickle
import pandas as pd
from embeddings_utils import TextEmbeddingsAnalyzer

script_dir = os.path.dirname(os.path.abspath(__file__))
cache_path = os.path.join(script_dir, '', 'cache', 'article_recommender.pkl')


class ArticleRecommender:
    def __init__(self, embedding_model, dataset_path, batch_size=100):
        self.embedding_model = embedding_model
        self.dataset_path = dataset_path
        self.embedding_cache_path = cache_path
        self.batch_size = batch_size
        self.embedding_cache = self._load_embedding_cache_()
        self.embedder = TextEmbeddingsAnalyzer()

    def _load_embedding_cache_(self):
        try:
            return pd.read_pickle(self.embedding_cache_path)
        except FileNotFoundError:
            return {}

    def _update_embedding_cache_(self, string):
        self.embedding_cache[string] = self.embedder.get_embedding(string)

        with open(self.embedding_cache_path, "wb") as embedding_cache_file:
            pickle.dump(self.embedding_cache, embedding_cache_file)

    def _embedding_from_string_(self, string):

        if string not in self.embedding_cache.keys():
            self._update_embedding_cache_(string)

        return self.embedding_cache[string]

    def recommend_articles(self, user_target_title, k_nearest_neighbors=5):
        df = pd.read_csv(self.dataset_path)

        data = []

        user_input_embedding = self._embedding_from_string_(user_target_title)

        article_descriptions = df["description"].tolist()

        for i in range(0, len(article_descriptions), self.batch_size):
            batch_descriptions = article_descriptions[i:i + self.batch_size]

            embeddings = [self._embedding_from_string_(description) for description in batch_descriptions]

            distances = self.embedder.distances_from_embeddings(user_input_embedding, embeddings,
                                                                distance_metric="cosine")

            indices_of_nearest_neighbors = self.embedder.indices_of_nearest_neighbors_from_distances(distances)

            for j in range(min(k_nearest_neighbors, len(indices_of_nearest_neighbors))):
                article_index = indices_of_nearest_neighbors[j]
                article_title = df.loc[article_index, 'title']
                article_description = df.loc[article_index, 'description']
                distance = distances[article_index]

                data.append({'title': article_title, 'description': article_description, 'distance': f'{distance:0.3f}'})

        return data