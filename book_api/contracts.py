from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class BookContract:
    method: str
    path: str
    summary: str
    response: dict[str, Any]
    request_params: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any]) -> "BookContract":
        if not isinstance(value, Mapping):
            raise TypeError("Contract must be a mapping of endpoint metadata.")

        missing = [name for name in ("method", "path", "summary", "response") if name not in value]
        if missing:
            raise ValueError(f"Contract is missing required fields: {', '.join(missing)}")

        method = str(value["method"]).strip().upper()
        path = str(value["path"]).strip()
        summary = str(value["summary"]).strip()

        if method != "GET":
            raise ValueError("Only GET /books/{id} is supported for this story.")
        if path != "/books/{id}":
            raise ValueError("Only /books/{id} is supported for this story.")
        if not isinstance(value["response"], Mapping):
            raise ValueError("Contract response must be a mapping.")

        request_params = value.get("request_params", {})
        if request_params is None:
            request_params = {}
        if not isinstance(request_params, Mapping):
            raise ValueError("Contract request_params must be a mapping when provided.")

        return cls(
            method=method,
            path=path,
            summary=summary,
            response=dict(value["response"]),
            request_params=dict(request_params),
        )
