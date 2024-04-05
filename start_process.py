
from router.SemanticRouter import SemanticRouter
from helpers.logger import logger
from router.routing import Routing

class StartProcess():
    def __init__(self):
        self.agents_route = [
            Routing().scrapper(),
            Routing().scrapper(),
            Routing().scrapper(),
        ]
        # logger.info(f"Agents route has been created{self.agents_route}")
        pass
    
    async def start_process(self, query):
        """
        Start the process of handling the given query.
        Parameters:
            query (str): The query to be processed.
        Returns:
            dict or str: The result of the query processing or a message indicating no route found.
        """
        try:
            logger.info("inside the start process")
            logger.info("Pick agent on the basis of query: " + query)
            router = SemanticRouter().router(self.agents_route)
            route = router(query)
            logger.info(f":::::::SEMANTIC ROUTING RESULT: ::::::: {route.name}")
            if route.name == "scrapper":
                logger.info(":::::::SCRAPPER:::::::")
                return {"message":f"Route found:{route.name}"}  
            else:
                return {"message":"No route found."}
        except Exception as e:
            return {"message":"An error occurred. Please try again. Error: " + str(e)}


