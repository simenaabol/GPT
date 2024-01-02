
TEST

context = """
Stig is the boss at Aboveit. He is a very capable boss, and sometimes he laughs at jokes. Always use a capital letter at the beginning when referring to people..
"""
question = "Hello, who is the boss at Aboveit?"

Answer: stig / Stig


model = AutoModelForQuestionAnswering.from_pretrained("ltg/norbert3-large", trust_remote_code=True)
-> Fungerer dårlig på Norsk


model = AutoModelForQuestionAnswering.from_pretrained("ltg/norbert3-large", trust_remote_code=True)
-> Fungerer litt på Engelsk, men begrenset. 
Fant denne på en tilfelidg side. 



Leaderboard på Hugging Face sin side, flere er properitære. 
https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard
Førset åpne modell: WizardLM/WizardLM-70B-V1.0, 
-> Får ikke til å kjøre :/



albert-large-v2
-> Funger dårlig