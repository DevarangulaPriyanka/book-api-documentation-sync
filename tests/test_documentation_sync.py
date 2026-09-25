import unittest

from book_api.contracts import BookContract
from book_api.documentation_sync import AUTO_DOC_END, AUTO_DOC_START, render_contract_documentation, sync_documentation


class DocumentationSyncTests(unittest.TestCase):
    def setUp(self):
        self.contract = {
            "method": "GET",
            "path": "/books/{id}",
            "summary": "Return a book by id.",
            "request_params": {},
            "response": {
                "id": 42,
                "title": "The Hobbit",
                "author": "J.R.R. Tolkien",
            },
        }

    def test_contract_change_updates_generated_section(self):
        original_contract = {
            "method": "GET",
            "path": "/books/{id}",
            "summary": "Return a book by id.",
            "request_params": {},
            "response": {"id": 1, "title": "Old title", "author": "Old author"},
        }
        updated_contract = {
            **original_contract,
            "summary": "Return a book by id with the latest metadata.",
            "response": {"id": 42, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
        }

        doc_text = "# Book API\n\nManual notes stay here.\n\n" + (
            f"{AUTO_DOC_START}\n{render_contract_documentation(BookContract.from_mapping(original_contract))}\n{AUTO_DOC_END}"
        )

        updated = sync_documentation(doc_text, updated_contract)

        self.assertIn("latest metadata", updated)
        self.assertIn("The Hobbit", updated)
        self.assertIn("Manual notes stay here.", updated)
        self.assertNotIn("Old title", updated)

    def test_unchanged_contract_is_noop(self):
        doc_block = f"{AUTO_DOC_START}\n{render_contract_documentation(BookContract.from_mapping(self.contract))}\n{AUTO_DOC_END}"
        doc_text = "# Book API\n\nManual notes stay here.\n\n" + doc_block

        updated = sync_documentation(doc_text, self.contract)

        self.assertEqual(doc_text, updated)

    def test_invalid_contract_raises_clear_error(self):
        doc_text = "# Book API\n\nManual notes stay here.\n\n"
        invalid_contract = {"method": "POST", "path": "/books/{id}", "summary": "Invalid", "response": {}}

        with self.assertRaises(ValueError):
            sync_documentation(doc_text, invalid_contract)

    def test_manual_content_outside_generated_section_is_preserved(self):
        doc_text = "# Book API\n\n# Human-maintained section\nThis should stay.\n"
        generated = f"\n\n{AUTO_DOC_START}\n{render_contract_documentation(BookContract.from_mapping(self.contract))}\n{AUTO_DOC_END}\n"

        updated = sync_documentation(doc_text + generated, self.contract)

        self.assertIn("# Human-maintained section", updated)
        self.assertIn("This should stay.", updated)
        self.assertIn("Return a book by id.", updated)


if __name__ == "__main__":
    unittest.main()
