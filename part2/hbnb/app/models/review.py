from . import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        if rating >= 0 and rating <= 5:
            self.rating = rating
        else:
            return "Error"
        self.place = place
        self.user = user    

    def __del__(self):
        #elmininar review
        return "Review deleted"