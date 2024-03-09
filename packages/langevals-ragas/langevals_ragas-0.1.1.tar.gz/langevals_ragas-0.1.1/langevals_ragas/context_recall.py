from langevals_core.base_evaluator import (
    BaseEvaluator,
    EvaluatorEntry,
    SingleEvaluationResult,
)
from .lib.common import evaluate_ragas, RagasSettings, RagasResult


class RagasContextRecallEntry(EvaluatorEntry):
    contexts: list[str]
    expected_output: str


class RagasContextRecallEvaluator(
    BaseEvaluator[RagasContextRecallEntry, RagasSettings, RagasResult]
):
    """
    Ragas Context Recall

    This evaluator measures the extent to which the retrieved context aligns with the annotated answer, treated as the ground truth. Higher values indicate better performance.
    """

    category = "rag"
    env_vars = [
        "OPENAI_API_KEY",
        "AZURE_CONTENT_SAFETY_ENDPOINT",
        "AZURE_CONTENT_SAFETY_KEY",
    ]
    docs_url = "https://docs.ragas.io/en/latest/concepts/metrics/context_recall.html"

    def evaluate(self, entry: RagasContextRecallEntry) -> SingleEvaluationResult:
        return evaluate_ragas(
            evaluator=self,
            metric="context_recall",
            contexts=entry.contexts,
            ground_truth=entry.expected_output,
            settings=self.settings,
        )
