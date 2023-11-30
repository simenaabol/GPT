# Create an assistant
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-3.5-turbo-1106"
)


# Create a Thread
thread = client.beta.threads.create()

# Add a message to a Thread

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)
# Now if you list Messages in Thread, you will see that this message is added to the thread on creation:
# {
#   "object": "list",
#   "data": [
#     {
#       "created_at": 1696995451,
#       "id": "msg_4rb1Skx3XgQZEe4PHVRFQhr0",
#       "object": "thread.message",
#       "thread_id": "thread_34p0sfdas0823smfv",
#       "role": "user",
#       "content": [{
#         "type": "text",
#         "text": {
#           "value": "I need to solve the equation `3x + 11 = 14`. Can you help me?",
#           "annotations": []
#         }
#           }],
#         ...


# Ru the  Assistant
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Jane Doe. The user has a premium account."
)