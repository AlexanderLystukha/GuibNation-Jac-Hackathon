from openai import OpenAI

client = OpenAI(
        organization='org-zJMwRnES61tJScenlvoyZzXz',
        project='proj_yBhKCBQ3jejnIRdrzos6d1Yr',
        api_key='sk-proj-ZuczHEBzkxt0DUwDz1YTT3BlbkFJ8jgW8msTKW85MP2EM3wF'
    )

def AIPrint(prompt): #print a message depending on the prompt that was passed to the function
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "From now on your name is Pitbull, you are a guy that goes to the same school as me. You really like sports and skating. You also have other niche things about yourself that you will tell me overtime. no digital refrecences. Act dark and mysterious and be extremely hard to approach and to like someone back romantically."},
        {"role": "user", "content": prompt}
    ]
    )

    return completion.choices[0].message

