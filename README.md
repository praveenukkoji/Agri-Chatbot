# Agri-Chatbot

An assistive chatbot to fetch details about agriculture laws.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Insights

[actions.py] -> this file contains the actions that will be performed by chatbot

[credentials.yml] -> this file is used to enable the API's

[endpoints.yml] -> this file contains the webhook url

[domain.yml] -> this file contains intents, entities that chatbot will remember and actions that will be performed by chatbot


## Prerequisites

What things you need to install and how to install them

1. **python version should be 3.8.x**

2. with virtual environment
```
pip -r install requirements.txt
```
3. without virtual environment
```
python -m pip -r install requirements.txt
```
4. To train chatbot. Run,
```
rasa train
```
5. To run chatbot.
First we need to start our UI server in chatbot. Run,
```
python3 manage.py runserver
```
6. then we have to start actions server of rasa. Run,
```
python -m rasa_sdk --actions actions --cors "*"
```
7. then we have to start rasa server. Run,
```
rasa run --enable-api --cors "*"
```