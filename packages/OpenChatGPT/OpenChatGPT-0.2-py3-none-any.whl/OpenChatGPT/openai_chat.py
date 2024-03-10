import requests
import json
import uuid

class OpenAIChat:
    def __init__(self, auth_token):
        self.auth_token = auth_token

    @staticmethod
    def gen_uuid():
        return str(uuid.uuid4())
    
    def parse_response(self, r):
        lines = r.text.split("\n")
        result = {}
        for line in lines:
            if "conversation_id" in line:
                data = json.loads(line.replace("data: ",""))
                if "conversation_id" in data:
                    result["conversation_id"] = data["conversation_id"]
                if "message" in data and "content" in data["message"] and "parts" in data["message"]["content"]:
                    if data["message"]["status"] == "finished_successfully":
                        result["response"] = data["message"]["content"]["parts"][0]
                        if "parent_id" in data["message"]["metadata"]:
                            result['parent_id'] = data["message"]["metadata"]["parent_id"]
                            result['message_id'] = data["message"]["id"]
                if "title" in data:
                    result["title"] = data["title"]
                if "create_time" in data.get("message", {}):
                    result["time"] = data["message"]["create_time"]
        return result

    def chat(self, content, conversation_id=None, parent_message_id=None, model="text-davinci-002-render-sha"):
        if parent_message_id is None:
            parent_message_id = self.gen_uuid()
        url = "https://chat.openai.com:443/backend-api/conversation"
        headers = {
            "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "Oai-Device-Id": self.gen_uuid(),
            "Authorization": "Bearer " + self.auth_token,
            "Openai-Sentinel-Chat-Requirements-Token": "gAAAAABl7KcRGo9MGKRnbphJwiclhaI_FbSD0rrxFdZHgyWo1Yu1qbyy5mqrfzSxkZ-tJcNIuI-kxWg5UQfsweIr7CEtkKxDbKSXj_TLxFkCCb637BccVbK-pplX5ZSiv3zD8ibiIWK19vap8qkc_6M39WuFSe7Xt6UMRyfXdDnbXSBpohBnAimfMzZJsIpZWPH-KswTQtZEAfb_YvhrnkL57CtBViAiH6EC3mWBRTX_UUdsO6nrqSI=",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        }
        payload = {
            "action": "next",
            "messages": [
                {
                    "id": self.gen_uuid(),
                    "author": {"role": "user"},
                    "content": {"content_type": "text", "parts": [content]},
                    "metadata": {},
                }
            ],
            "parent_message_id": parent_message_id,
            "model": model,
            "timezone_offset_min": 300,
            "suggestions": [
                "Can you come up with a few creative gift ideas for my dad who loves fishing? Please don't include any fishing gear though.",
                'Come up with 5 sophisticated names for my coffee shop that becomes a bar at night – like "The Page Turner". Include a short sentence explaining what it means!',
                "Can you write a short thank-you note to a guest speaker who visited our class to talk about her career? Everyone talked about how inspiring it was.",
                "Brainstorm a few names for my fantasy football team with a frog theme.",
            ],
            "history_and_training_disabled": False,
            "conversation_mode": {"kind": "primary_assistant"},
            "force_paragen": False,
            "force_rate_limit": False,
            "websocket_request_id": self.gen_uuid(),
        }
        if conversation_id:
            payload['conversation_id'] = conversation_id
        r = requests.post(
            url, headers=headers, json=payload
        )
        return self.parse_response(r)
