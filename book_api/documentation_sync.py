from __future__ import annotations

import json
from typing import Any

from .contracts import BookContract

AUTO_DOC_START = "<!-- BEGIN AUTO DOCS: GET /books/{id} -->"
AUTO_DOC_END = "<!-- END AUTO DOCS: GET /books/{id} -->"


def render_contract_documentation(contract: BookContract) -> str:
    request_block = json.dumps(contract.request_params, indent=2, sort_keys=True) if contract.request_params else "{}"
    response_block = json.dumps(contract.response, indent=2, sort_keys=True)
    return "\n".join(
        [
            "### GET /books/{id}",
            contract.summary,
            "",
            "**Request parameters**",
            "```json",
            request_block,
            "```",
            "",
            "**Response**",
            "```json",
            response_block,
            "```",
        ]
    )


def _replace_or_append_generated_section(documentation_text: str, rendered_block: str) -> str:
    full_block = f"{AUTO_DOC_START}\n{rendered_block}\n{AUTO_DOC_END}"
    start_index = documentation_text.find(AUTO_DOC_START)
    end_index = documentation_text.find(AUTO_DOC_END)

    if start_index != -1 and end_index != -1 and end_index > start_index:
        segment = documentation_text[start_index : end_index + len(AUTO_DOC_END)]
        if segment == full_block:
            return documentation_text
        return documentation_text.replace(segment, full_block, 1)

    if documentation_text.strip():
        return f"{documentation_text.rstrip()}\n\n{full_block}\n"
    return f"{full_block}\n"


def sync_documentation(documentation_text: str, contract_value: Any) -> str:
    contract = BookContract.from_mapping(contract_value)
    rendered_block = render_contract_documentation(contract)
    return _replace_or_append_generated_section(documentation_text or "", rendered_block)
