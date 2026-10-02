
import unittest
from unittest.mock import patch
import os
import main


class TestFilePathValidation(unittest.TestCase):

    def setUp(self):
        main.error_count = 0
        main.errors = []
        main.invalid_rows = set()

    @patch("builtins.input", return_value="")
    def test_empty_file_path(self, mock_input):
        with self.assertRaises(SystemExit) as error:
            main.main()

        self.assertEqual(error.exception.code, 1)

    @patch("builtins.input", return_value="data/sample.txt")
    def test_invalid_file_extension(self, mock_input):
        with self.assertRaises(SystemExit) as error:
            main.main()

        self.assertEqual(error.exception.code, 1)

    @patch("builtins.input", return_value="data/unknown.csv")
    def test_missing_csv_file(self, mock_input):
        with self.assertRaises(SystemExit) as error:
            main.main()

        self.assertEqual(error.exception.code, 1)

    @patch("builtins.input", return_value="data/combined_test.csv")
    def test_valid_csv_file(self, mock_input):
        result = main.main()
        self.assertIsNone(result)


class TestCSVValidation(unittest.TestCase):

    def setUp(self):
        main.error_count = 0
        main.errors = []
        main.invalid_rows = set()

    def test_valid_csv(self):
        result = main.validate_csv("data/valid_test.csv")
        self.assertTrue(result)
        self.assertEqual(main.error_count, 0)

    def test_invalid_csv(self):
        result = main.validate_csv("data/combined_test.csv")
        self.assertTrue(result)
        self.assertGreater(main.error_count, 0)

    def test_report_is_created(self):
        main.validate_csv("data/valid_test.csv")

        self.assertTrue(
            os.path.isfile("reports/validation_report.txt")
        )

    def test_report_contains_status(self):
        main.validate_csv("data/valid_test.csv")

        with open(
            "reports/validation_report.txt",
            mode="r",
            encoding="utf-8"
        ) as report:
            content = report.read()

        self.assertIn("Status: PASSED", content)


if __name__ == "__main__":
    unittest.main()