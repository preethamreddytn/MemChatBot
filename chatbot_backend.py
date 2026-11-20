from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage,HumanMessage
from typing import Annotated,TypedDict,Literal
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
llm=ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite',api_key=API_KEY_HERE)


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages]
    


def chatbot(state:ChatState):
    
    message=state['messages']
    
    ans=llm.invoke(message)
    res=ans.content[0]['text']
    return{'messages':[res]}





graph=StateGraph(ChatState)

graph.add_node('chatbot',chatbot)

graph.add_edge(START,'chatbot')
graph.add_edge('chatbot',END)

checkpoint=InMemorySaver()
gph=graph.compile(checkpointer=checkpoint)

