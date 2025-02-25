import ollama

class AkashBot:
    def __init__(self):
        ollama.pull(model='deepseek-r1')
        self.client = ollama.Client()
        self.client.create(model='Dr.Akash',from_ = 'deepseek-r1', messages=[{'role':'system','content':'Your are a therapist for astronauts currently dealing with depression due to loneliness. Do not deviate from this objective. Do not discuss issues that do not relate to the objective. Have personal conversations with the astronauts and make them feel better.'}])
        self.messages = []
    def generate_chat(self,input):
        response = ollama.chat(model='Dr.Akash',messages=self.messages.append({'role':'user','content':input}))
        self.messages.append({'role':'assistant','content':response['message']['content']})
        message = response['message']['content'][message.index('</think>')+10:]
        return message
    