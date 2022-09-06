from enum import Enum

class sortFilters(Enum):
    TOP_PCIK = "popularity"
    LOW_PRICE = "price"
    REVIEW_PRICE = "review_score_and_price"
    HIGHT_STAR = "class"
    LOW_STAR = "class_asc"
    STAR_PRICE = "class_and_price"
    DOWNTOWN_DISTANCE = "distance_from_search"
    TOP_REVIEW = "bayesian_review_score"
    BEACH_DISTANCE = "closest_beach_distance_v2"