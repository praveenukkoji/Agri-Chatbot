# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import pandas as pd
import numpy as np


class ActionSFGetInfo(Action):

    def name(self) -> Text:
        return "action_sf_get_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        short_form = tracker.get_slot('short_form')
        data = ""

        try:
            df = pd.read_csv('/Users/praveenukkoji/Developer/Internship/main/rasa/actions/data1.csv')
            df.columns = ['short_form', 'full_form', 'year', 'location', 'points']
            df["short_form"].fillna(value="")
            str1 = ""
            for x in range(len(df)):
                str_1 = str(df["short_form"][x]).lower()
                str_2 = str(short_form.lower())
                if str_1 == str_2:
                    str1 = "Title: " + str(df["full_form"][x]) + " -- Year: " + str(df["year"][x]).split(".")[0] + "\n\n" + str(df["points"][x])
            if str1 == "":
                for x in range(len(df)):
                    str_11 = str(df["short_form"][x]).lower()
                    str_22 = str(short_form.lower())
                    if str_11.find(str_22):
                        str1 = "Title: " + str(df["full_form"][x]) + " -- Year: " + str(df["year"][x]).split(".")[0] + "\n\n" + str(df["points"][x])
            if str1 != "":
                data = str1
            else:
                data = "No such scheme is present."
        except Exception as e:
            data = "Some error occured. Try again!!!"

        dispatcher.utter_message(text=data)
        str1 = ""

        return [SlotSet('short_form', short_form)]


class ActionFFGetInfo(Action):

    def name(self) -> Text:
        return "action_ff_get_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        full_form = tracker.get_slot('full_form')
        data = ""
        
        try:
            df = pd.read_csv('/Users/praveenukkoji/Developer/Internship/main/rasa/actions/data1.csv')
            df.columns = ['short_form', 'full_form', 'year', 'location', 'points']
            str1 = ""
            for x in range(len(df)):
                str_1 = str(df["full_form"][x]).lower()
                str_2 = str(full_form.lower())
                if str_1 == str_2:
                    str1 = "Title: " + str(df["full_form"][x]) + " -- Year: " + str(df["year"][x]).split(".")[0] + "\n\n" + str(df["points"][x])
            if str1 == "":
                for x in range(len(df)):
                    str_11 = str(df["full_form"][x]).lower()
                    str_22 = str(full_form.lower())
                    if str_11.find(str_22):
                        str1 = "Title: " + str(df["full_form"][x]) + " -- Year: " + str(df["year"][x]).split(".")[0] + "\n\n" + str(df["points"][x])
            if str1 != "":
                data = str1
            else:
                data = "No such scheme is present."
        except Exception as e:
            data = "Some error occured. Try again!!!"

        dispatcher.utter_message(text=data)
        str1 = ""

        return [SlotSet('full_form', full_form)]


# this action is used to empty slots
class Actionreset(Action):
	def name(self):
		return 'action_reset'

	def run(self, dispatcher, tracker, domain):
		return [AllSlotsReset()]


class OutOfScopeMessage(Action):
	def name(self):
		return 'action_default'

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message("I'm not sure I understand!!!")
		return []


