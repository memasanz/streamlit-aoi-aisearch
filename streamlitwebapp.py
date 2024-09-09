#https://docs.microsoft.com/en-us/azure/app-service/tutorial-custom-container?pivots=container-linux
# https://towardsdatascience.com/deploying-a-streamlit-web-app-with-azure-app-service-1f09a2159743
# https://towardsdatascience.com/beginner-guide-to-streamlit-deployment-on-azure-f6618eee1ba9
#https://learn.microsoft.com/en-us/azure/app-service/configure-authentication-provider-aad?tabs=workforce-tenant


# az acr build --registry acrcensusapp --resource-group CensusApp --image census-app .
# az appservice plan create --name mmAppServicePlan --resource-group CensusApp --is-linux
# az webapp create --resource-group CensusApp --plan mmAppServicePlan --name mmanotherapp --deployment-container-image-name acrcensusapp.azurecr.io/census-app:latest
# az webapp config appsettings set --resource-group CensusApp --name mmanotherapp --settings WEBSITES_PORT=80
# az webapp log config --name mmanotherapp --resource-group CensusApp --docker-container-logging filesystem
# az webapp log tail --name mmanotherapp --resource-group CensusApp
# az webapp create -g CensusApp -p CensusAppServicePlan -n xmmcensus-web-app -i xmmcensusappregistry.azurecr.io/census-app:latest
# az webapp create -g MyResourceGroup -p MyPlan -n MyUniqueAppName -i myregistry.azurecr.io/docker-image:tag


import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv  
import os 
import json
import requests
import logging
import time
from typing import List, Optional
from openai import AzureOpenAI
from dotenv import load_dotenv 
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI
from ChatOnYourDataWithAzureOpenAI import ChatOnYourDataWithAzureOpenAI




st.title('Ask About My Data')


reset = st.checkbox('Reset Messages')

if reset:
        st.write('Sure thing!')
        st.session_state.messages = [{"role":"system","content":"You are an AI assistant that helps people find information."}]
        st.session_state.messages.append({"role": "assistant", "content": "How can I help you?"}) 
        print("completed reset")

if "messages" not in st.session_state:
        print("messages not in session state")
        st.session_state["messages"] = [{"role":"system","content":"You are an AI assistant that helps people find information."}]
        st.session_state.messages.append({"role": "assistant", "content": "How can I help you?"})

def print_messages():
        for i in range (len(st.session_state.messages) -1, -1, -1):
            msg = st.session_state.messages[i]
            if msg is not None:
                if msg["role"] == "user":
                    message(msg["content"], is_user=True, key = str(i) + "user", avatar_style = "initials", seed = "👤")
                else:
                    if msg["role"] == "assistant":
                        message(msg["content"], is_user=False, key = str(i) + "system", avatar_style="initials", seed = "😉")


with st.form("chat_input", clear_on_submit=True):
        a, b = st.columns([4, 1])
        user_input = a.text_input(
                label="Your message:",
                placeholder="What would you like to ask?",
                label_visibility="collapsed",
        )
        b.form_submit_button("Send")

if user_input:
        print('user input:', user_input)

        st.session_state.messages.append({"role": "user", "content": user_input})

        #response = get_fromOpenAI(user_input)
        #response = "Hello! How can I help you today?"

        blah = ChatOnYourDataWithAzureOpenAI()
        response, citation_content, file_paths, urls_paths = blah.make_request(user_input)

        print(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

print_messages()