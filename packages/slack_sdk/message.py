from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def send_message_to_channel(slack_token, slack_channel, message):
    client = WebClient(token=slack_token)

    try:
        response = client.chat_postMessage(channel=slack_channel, text=message)
        assert response["message"]["text"] == message
    except SlackApiError as e:
        assert e.response["ok"] is False
        assert e.response["error"]
        print(f"Got an error: {e.response['error']}")


if __name__ == "__main__":
    slack_token = "token"
    slack_channel = "channel_id"
    message = "hello world"
    send_message_to_channel(slack_token, slack_channel, message)
