from __future__ import annotations

import os

import google.generativeai as genai
import PIL.Image


genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


class Chatbot:
    def __init__(self, model_name: str = 'gemini-1.5-flash'):
        self.model = genai.GenerativeModel(model_name)


def main():
    model = genai.GenerativeModel('gemini-1.5-flash')
    # image_path = '/home/hiuminee/Downloads/cs115/9420_L01_V003_start.jpg'
    # image = PIL.Image.open(image_path)

    # response = model.generate_content(["Tell me about this instrument", image])
    # print(response.text)
    # response = model.generate_content("Write a story about a magic backpack.", stream=True)
    # for chunk in response:
    #     print(chunk.text)
    #     print("_" * 80)

    # model = genai.GenerativeModel("gemini-1.5-flash")
    # chat = model.start_chat(
    #     history=[
    #         {"role": "user", "parts": "Hello"},
    #         {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    #     ]
    # )
    # response = chat.send_message("I have 2 dogs in my house.")
    # print(response.text)
    # response = chat.send_message("How many paws are in my house?")
    # print(response.text)

    # print("*" * 80)
    # print("Chat history:", chat.history)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(
        'Tell me a story about a magic backpack.',
        generation_config=genai.types.GenerationConfig(
            candidate_count=1,
            stop_sequences=['x'],
            max_output_tokens=20,
            temperature=1.0,
        ),
    )

    print(response.text)


if __name__ == '__main__':
    main()
