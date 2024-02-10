import wikipedia

class WikiSearch:
    def __init__(self, search_term):
        self.search_term = search_term
    
    def getSummary(self):
        wikipedia.set_lang("pt")
        return wikipedia.summary(self.search_term)