
import helpers.utterances as utterances
from helpers.logger import logger
from router.SemanticRouter import SemanticRouter


class Routing(SemanticRouter):
  
    def __init__(self):
        """
        Initialize the object with the constructor of the parent class.
        """
        super().__init__()

    def scrapper(self):
        """
        Create a route for the "scrapper" feature.
        :return: The created route.
        """
        return self.create_route(
            name="scrapper",
            utterances=utterances.scrapper
        )
    
    
    

