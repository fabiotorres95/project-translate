import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    history = HistoryModel.list_as_json()
    assert json.loads(history)[0]["translate_from"] == "en"
    assert json.loads(history)[0]["translate_to"] == "pt"
    assert json.loads(history)[1]["text_to_translate"] == "Do you love music?"
    assert json.loads(history)[1]["translate_from"] == "en"
    assert json.loads(history)[1]["translate_to"] == "pt"
