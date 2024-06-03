from openai import OpenAI
client = OpenAI(api_key='api_key')

messages = []
sys_msj = input('What type of bot would you like to create?\n')
messages.append({"role": "system", "content": sys_msj})

print("Your assistant is ready")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages= messages)
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("\n"+ reply + "\n")