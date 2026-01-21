---
date: '2025-02-11T21:39:48+01:00'
draft: false
tags: ['programming']
title: 'Local AI Development for Free'
url: 'blog/local-ai-development-for-free'
---

In this short article, I'll show you how to develop locally with LLMs, making AI development free and private. With the rising costs of AI services, running models locally is becoming an increasingly attractive option for developers who want full control over their AI development process.

<!--more-->

## Quote Of The Day
>
>The only mistake is almost always to believe that my point of view is the only one from which one can see the truth. The deaf person will always think the dancers are crazy.

<hr>

I recently started using [Jan AI](https://jan.ai) to develop locally with AI (and also for daily use). Basically, you can use Jan as the frontend for any GGUF LLM. It stores the model and all the conversations on your local machine making it private and great for developing as you can launch a OpenAI compatible API and thus don't need to pay for the API.

After downloading the Jan desktop app, installing a model of your choice and starting the server in the UI, you can test it by running the following script:

```python
import openai

client = openai.OpenAI(api_key='APIKEY', base_url='http://127.0.0.1:1337/v1')

response = client.chat.completions.create(
    model="qwen2.5-coder-7b-instruct",
    messages=[
      {"role": "system", "content": "You are a Journalist"},
      {"role": "assistant", "content": "Write a short article"},
      {"role": "user", "content": "what is a computer?"}
    ],
  )

response = response.choices[0].message.content
print(response)
```

This will print the response from the LLM in the console.
>Note: You need to replace the `model` with the model you installed in the Jan UI. You can find the id with `client.models.list()`.

From now on you can use the openai library to interact with your local LLM. Happy coding!
