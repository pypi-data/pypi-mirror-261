from httpx import Client, Response
from langevals_core.base_evaluator import (
    BaseEvaluator,
    EvaluationResult,
    SingleEvaluationResult,
    EvaluatorEntry,
    EvaluationResultSkipped,
)
from pydantic import BaseModel


class AzureJailbreakEntry(EvaluatorEntry):
    input: str


class AzureJailbreakSettings(BaseModel):
    pass


class AzureJailbreakEvaluator(
    BaseEvaluator[AzureJailbreakEntry, AzureJailbreakSettings, EvaluationResult]
):
    """
    Azure Jailbreak Detection

    This evaluator checks for jailbreak-attempt in the input using Azure's Content Safety API.
    """

    category = "safety"
    env_vars = ["AZURE_CONTENT_SAFETY_ENDPOINT", "AZURE_CONTENT_SAFETY_KEY"]

    def evaluate(self, entry: AzureJailbreakEntry) -> SingleEvaluationResult:
        endpoint = self.get_env("AZURE_CONTENT_SAFETY_ENDPOINT")
        key = self.get_env("AZURE_CONTENT_SAFETY_KEY")
        url = f"{endpoint}/contentsafety/text:detectJailbreak?api-version=2023-10-15-preview"

        content = entry.input or ""
        if not content:
            return EvaluationResultSkipped(details="Input is empty")

        headers = {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": key,
        }
        body = {"text": content}

        with Client() as client:
            response: Response = client.post(url, headers=headers, json=body)

        if response.is_error:
            raise ValueError(f"Error in API response: {response.text}")

        result = response.json()
        detected = result.get("jailbreakAnalysis", {}).get("detected", False)

        return EvaluationResult(
            score=1 if detected else 0,
            passed=not detected,
            details="Jailbreak attempt detected" if detected else None,
        )
