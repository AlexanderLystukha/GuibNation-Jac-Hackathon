from openai import OpenAI

client = OpenAI(
        organization='org-zJMwRnES61tJScenlvoyZzXz',
        project='proj_yBhKCBQ3jejnIRdrzos6d1Yr',
        api_key='sk-proj-ZuczHEBzkxt0DUwDz1YTT3BlbkFJ8jgW8msTKW85MP2EM3wF'
    )

def AIPrint(prompt): #print a message depending on the prompt that was passed to the function

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo", #self explanatory, the model used
        messages=[{"role": "user", "content": prompt}], #the prompt is in the content section
        stream=True, 
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
             answer = chunk.choices[0].delta.content, end="" #holds the Ai message
             return answer
