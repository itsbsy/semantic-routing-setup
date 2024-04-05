import os
sematic_router_path=os.environ.get('SEMENTIC_ROUTER_PATH')
import sys
sys.path.append(sematic_router_path)
from semantic_router import Route
from semantic_router.layer import RouteLayer
from semantic_router.encoders import HuggingFaceEncoder
from helpers.logger import logger


class SemanticRouter:
    def __init__(self):
        self.encoder = HuggingFaceEncoder()
        # logger.info(f":::::::::::::SemanticRouter Created:::::::::::")
    
    def create_route(self, name, utterances):
        return Route(name=name, utterances=utterances)
    
    def router(self, routes):
        return RouteLayer(encoder=self.encoder, routes=routes)