
# coding=utf-8
import openai
openai.api_key = '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'



def dell():
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "你是一个人"},
            {"role": "user", "content": "谁是马斯克"},
        ]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    r = dell()
    print(r)
