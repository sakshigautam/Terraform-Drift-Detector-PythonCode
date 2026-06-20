from pydantic import BaseModel
from typing import List


class DriftChange(BaseModel):
    resource: str
    action: List[str]
    before: dict = {}
    after: dict = {}


class AnalysisResult(BaseModel):
    severity: str
    intent: str
    risk: str
    explanation: str
    remediation_script: str
