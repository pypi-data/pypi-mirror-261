import spacy
from .base import Metric


class SelfCheck(Metric):
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        super().__init__()

    def score(self, response, references, metrics, level='sentence'):
        if level == 'sentence':
            return self._score_sentence(response, references, metrics)
        elif level == 'passage':
            return self._score_passage(response, references, metrics)
        else:
            raise ValueError("Invalid evaluation level. Choose either 'sentence' or 'passage'.")

    def _score_sentence(self, response, references, metrics):
        
        doc = self.nlp(response[0])
        response = [sent.text for sent in doc.sents]
        scores_list = []
        for idx, sent in enumerate(response):
            score_dict = {'sentence': sent}
            for metric in metrics:
                total_score = 0
                for ref in references:
                    ref_sentences = [sent.text for sent in self.nlp(ref).sents]
                    for ref_sent in ref_sentences:
                        score = metric.score(response=sent, reference=ref_sent)
                        total_score += score
                avg_score = total_score / (len(references) * len(ref_sentences))
                score_dict[metric.name] = round(avg_score, 4)
            scores_list.append(score_dict)
        return scores_list

    def _score_passage(self, response, references, metrics):
        doc = self.nlp(response[0])
        response_sentences = [sent.text for sent in doc.sents]
        scores_list = []
        for ref in references:
            ref_doc = self.nlp(ref)
            ref_sentences = [sent.text for sent in ref_doc.sents]
            metric_scores = {}
            for metric in metrics:
                scores_per_sentence = []
                for response_sent in response_sentences:
                    for ref_sent in ref_sentences:
                        score = metric.score(response=response_sent, reference=ref_sent)
                        scores_per_sentence.append(score)
                avg_score = sum(scores_per_sentence) / len(scores_per_sentence)
                metric_scores[metric.__class__.__name__] = round(avg_score, 4)
            scores_list.append({'passage': ref, 'scores': metric_scores})
        return scores_list
