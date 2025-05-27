import google.generativeai as genai
from config import GEMINI_CONFIG
import re

genai.configure(api_key=GEMINI_CONFIG["api_key"])

regular_model = genai.GenerativeModel(
            model_name=GEMINI_CONFIG["model"],
            system_instruction=GEMINI_CONFIG["system_instruction"]+GEMINI_CONFIG["ai_system_instruction"]
        )
my_initial_question = ''
my_initial_response = ''
def get_response(prompt: str) -> tuple[str, str]:
    global my_initial_question
    global my_initial_response
    if my_initial_question != '':
        note = f"User previosly asked you: {my_initial_question}; you replied previously that: {my_initial_response}. Only Use this if the current prompt is related to you. "
    else:
        note = ""
    regular_model = genai.GenerativeModel(
        model_name=GEMINI_CONFIG["model"],
        system_instruction=GEMINI_CONFIG["system_instruction"]+GEMINI_CONFIG["ai_system_instruction"]+note,
    )
    response = regular_model.generate_content(
        prompt,
        generation_config={
            "temperature": GEMINI_CONFIG["temperature"],
            "top_p": GEMINI_CONFIG["top_p"],
            "top_k": GEMINI_CONFIG["top_k"]
        },
        stream=GEMINI_CONFIG["streaming"]
    )
    bot_reply = response.text.strip().splitlines()
    print("AI Output:", bot_reply)
    command = bot_reply[0]
    '''if command.startswith("pass,"):
        reply_text = command[5:] + '\n'.join(bot_reply[1:])
        command = "pass"
    else:'''
    my_initial_question = prompt
    if "```python" in command or "```tool_code" in command:
        print("Reformating format..")
        command = '; '.join(re.findall(r"```(.*?)```", response.text.replace('```python', '```').replace('```tool_code', '```'), re.DOTALL)).strip()
        reply_text = re.sub(r"```(.*?)```", "", response.text.replace('```python', '```').replace('```tool_code', '```'), flags=re.DOTALL).strip()
    else:
        if "command, " in bot_reply[1]: # Just In Case
            command = f"{command}; {bot_reply[1]}"
            reply_text = '\n'.join(bot_reply[2:])
        else:
            reply_text = '\n'.join(bot_reply[1:])
    my_initial_response = reply_text
    print("🤖 Little Bot says:", reply_text)
    print("Command", command)
    print("Init question is", my_initial_question)
    return command, reply_text

#This function is for ai to use
def give_get_response(note: str, prompt: str) -> tuple[str, str]:
    print("Promt: ", prompt)
    model_for_ai = genai.GenerativeModel(
        model_name=GEMINI_CONFIG["model"],
        system_instruction=GEMINI_CONFIG["system_instruction"] + note
    )
    response = model_for_ai.generate_content(
        prompt,
        generation_config={
            "temperature": GEMINI_CONFIG["temperature"],
            "top_p": GEMINI_CONFIG["top_p"],
            "top_k": GEMINI_CONFIG["top_k"]
        },
        stream=GEMINI_CONFIG["streaming"]
    )
    bot_reply = response.text.strip().splitlines()
    command = bot_reply[0]
    if command.startswith("pass,"):
        reply_text = command[5:] + '\n'.join(bot_reply[1:])
        command = "pass"
    else:
        reply_text = '\n'.join(bot_reply[1:])
    print("🤖 Little Bot says:", reply_text)
    print("Command", command)
    return command, reply_text