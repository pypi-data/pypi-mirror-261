from torchmetrics import Metric
import torch
from typing import Optional
from nlu_inference.utils import get_ents
from typing import List


class ChunkF1(Metric):

    full_state_update: Optional[bool] = False
    
    def __init__(self):
        super().__init__()
        self.add_state('correct', default=torch.tensor(0.0), dist_reduce_fx='sum')
        self.add_state('all_pred', default=torch.tensor(0.0), dist_reduce_fx='sum')
        self.add_state('all_true', default=torch.tensor(0.0), dist_reduce_fx='sum')

    def update(self, pred: List[List[str]], true: List[List[str]]):
        true_entities = set()
        for p in pred:
            for ent in get_ents(p):
                true_entities.add(ent)
        pred_entities = set()
        for t in true:
            for ent in get_ents(t):
                pred_entities.add(ent)
        self.correct += len(true_entities & pred_entities)
        self.all_pred += len(pred_entities)
        self.all_true += len(true_entities)

    def compute(self):
        return 2 * self.correct / (self.all_pred + self.all_true)