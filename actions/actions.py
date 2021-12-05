# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import webbrowser
import mysql.connector

# This is a simple example for a custom action which utters "Hello World!"

from typing import Dict, Text, List, Optional, Any

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction

# class ValidateAccountNumber(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_account_number"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         account_number = tracker.get_slot("Account Number")
#         if not acc_num:
#             dispatcher.utter_message(text="Please Give you account number")
#         else:
#             dispatcher.utter_message(text=f"Your account number is given as {account_number}.)
#
#         # security_pin = tracker.get_slot("Security PIN")
#         return []
# #
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ValidateUserLocationForm(Action):

    def name(self) -> Text:
        return "user_location_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        required_slots = ["location"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]
        #
        # # location = tracker.latest_message.get["Enter your location"]
        # print(Location)
        # dispatcher.utter_message(text=f"https://www.google.com/maps/place/{Location}/")
        #
        # return []

class ActionUserLocationSubmit(Action):
    def name(self) -> Text:
        return "action_user_location_submit"

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_location_details",
                                 Location = tracker.get_slot("location"))

class ValidateUserDetailsForm(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["name", "account_number"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]
        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionUserDetailsSubmit(Action):
    def name(self) -> Text:
        return "action_user_details_submit"

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_details_thanks",
                                 Name=tracker.get_slot("name"),
                                 Account_number=tracker.get_slot("account_number"))

class ClassRetrieveL5Transactions(Action):

    def name(self) -> Text:
        return "action_last5_transactions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="username",
            password="password"
        )
        mycursor = mydb.cursor()
        Account_Number = tracker.get_slot("account_number")
        mycursor.execute(f"SELECT * FROM bank.transactions where AccountNumber={Account_Number}")
        records = mycursor.fetchall()
        info = "The transaction details are as follows: \n"
        dispatcher.utter_message(info)
        for record in records:
            print(record)
            records_1 = """{}.""".format(record)
            dispatcher.utter_message(records_1)

        return []
