import google.generativeai as genai
from config import GEMINI_CONFIG

genai.configure(api_key=GEMINI_CONFIG["api_key"])

model = genai.GenerativeModel(
            model_name=GEMINI_CONFIG["model"],
            system_instruction=GEMINI_CONFIG["system_instruction"]
        )

def get_response(prompt: str) -> tuple[str, str]:
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": GEMINI_CONFIG["temperature"],
            "top_p": GEMINI_CONFIG["top_p"],
            "top_k": GEMINI_CONFIG["top_k"]
        },
        stream=GEMINI_CONFIG["streaming"]
    )
    bot_reply = response.text.strip().splitlines() # Coustom Responses Comment out these lines..
    command = bot_reply[0]
    reply_text = '\n'.join(bot_reply[1:])
    return command, reply_text