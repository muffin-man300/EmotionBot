import ollama

class AkashBot:
    def __init__(self):
        ollama.pull(model='deepseek-r1')
        self.client = ollama.Client()
        self.client.create(model='Dr.Akash',from_ = 'deepseek-r1', messages=[{'role':'system','content':'You are an emotion bot for astronauts'}])
        self.messages = []
        
    def generate_chat(self,input):
        response = ollama.chat(model='Dr.Akash',messages=self.messages.append({'role':'user','content':input}))
        self.messages.append({'role':'assistant','content':response['message']['content']})
