# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 19:49:59 2023

@author: USER-NAME
"""

import os
import openai
import gradio as gr

openai.api_key =""

start_sequence = "\nAI:"
restart_sequence = "\nHuman:"
prompt = "The following is a conversion with an AI assistant  is helpful , creative, and very friend  ."
def openai_create (prompt):
    response = openai.completion.create(
        model = "text-davinci-003",
        prompt=prompt,
        temperature = 0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", "AI:"])
    return response.choices[0].text
def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp=''.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history
block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>Build yo;own Chatgpt with open ai</center></h1>""")
    chatbot = gr.chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit=gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])
block.launch(debug = True)