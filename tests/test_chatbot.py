import pytest
from chatbot.chatbot import predict_class, get_response

# Example tests for predict_class function
def test_predict_class():
    # Test if predict_class returns the correct intent for a given sentence
    model = None  # Mock model for testing purposes
    words = ["hello", "how", "are", "you"]
    sentence = "Hi there!"
    result = predict_class(sentence, model)
    assert result == [{"intent": "greeting", "probability": "0.95"}]

    # Test if predict_class handles unknown intents properly
    sentence = "What's your name?"
    result = predict_class(sentence, model)
    assert result == [{"intent": "unknown", "probability": "0.85"}]

# Example tests for get_response function
def test_get_response():
    # Test if get_response returns a response for a given intent
    intents_json = {
        "intents": [
            {"tag": "greeting", "responses": ["Hello!", "Hi there!"]}
        ]
    }
    intent = [{"intent": "greeting", "probability": "0.95"}]
    result = get_response(intent, intents_json)
    assert result in ["Hello!", "Hi there!"]

    # Test if get_response handles unknown intents properly
    intent = [{"intent": "unknown", "probability": "0.85"}]
    result = get_response(intent, intents_json)
    assert result == "I'm sorry, I didn't understand that."

if __name__ == "__main__":
    pytest.main()
