"""
Popularity based recommender
"""


class PopularityRecommender:
    """
    popularity recommender class
    """
    MODEL_NAME = 'Popularity'

    def __init__(self, items):
        """
        class initialization
        :param items: items under consideration to recommend
        """
        pass

    def get_model_name(self):
        """
        gets model name of this recommender
        :return: model name
        """
        return self.MODEL_NAME

    def recommend_items(self, user):
        """
        recommends items to user
        :param user: user for whom we need to recommend items
        :return: items recommended to user
        """
        pass
