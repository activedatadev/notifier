from app import main


def test_telegram_packet(monkeypatch):
    monkeypatch.setenv("BOT_ID", "B3")
    monkeypatch.setenv("GROUP_ID", "G5")

    url, message = main.build_telegram_packet("My message is this")
    assert url == "https://api.telegram.org/botB3/sendmessage"
    assert message == {"chat_id": "G5", "text": "My message is this"}
