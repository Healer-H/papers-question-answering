from __future__ import annotations

import chainlit as cl


@cl.on_chat_start
async def start():
    text_content = 'Hello, this is a text element.'
    elements = [
        cl.Text(name='simple_text', content=text_content, display='inline'),
    ]

    msg = cl.Message(
        content='Check out this text element!',
        elements=elements,
        author='Chat hehe',
    )

    await msg.send()
    # await cl.sleep(2)
    # await msg.remove()


@cl.on_message
async def another(message: cl.Message):
    # Your custom logic goes here...

    # Send a response back to the user
    await cl.Message(
        content=f'Received: {message.content}',
    ).send()
