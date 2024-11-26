import json
import speech_recognition as sr
import pyttsx3
import random

# File path for hotel data
HOTEL_DATA_FILE = "hotel_data.json"

# Initialize speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user input via microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio).lower()
            print(f"You said: {query}")
            return correct_input(query)
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that. Could you please repeat?")
            return ""
        except sr.RequestError:
            speak("There seems to be an issue with the speech recognition service. Please try again later.")
            return ""

def correct_input(query):
    """Correct common misinterpretations (e.g., 'sweet' to 'suite')."""
    corrections = {
        "sweet room": "suite room",
        "suite room": "suite",
        "sweet": "suite"
    }
    for incorrect, correct in corrections.items():
        query = query.replace(incorrect, correct)
    return query

def load_hotel_data():
    """Load hotel data from a JSON file."""
    try:
        with open(HOTEL_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        speak("Hotel data file not found. Please ensure the file exists.")
        return {}
    except json.JSONDecodeError:
        speak("Hotel data file is corrupted. Please fix the file.")
        return {}

def save_hotel_data(data):
    """Save updated hotel data to the JSON file."""
    try:
        with open(HOTEL_DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving hotel data: {e}")

def greet():
    """Provide a random greeting."""
    hotel_data = load_hotel_data()
    if "greetings" in hotel_data:
        greeting = random.choice(hotel_data["greetings"])
        speak(greeting)
    else:
        speak("Hello! Welcome to our hotel. How can I assist you?")

def room_details(room_type):
    """Provide details of the specified room type."""
    hotel_data = load_hotel_data()
    if "rooms" in hotel_data and room_type in hotel_data["rooms"]:
        room = hotel_data["rooms"][room_type]
        price = room["price_per_night"]
        discount = room.get("discount", 0)
        final_price = price - (price * discount / 100)
        amenities = ", ".join(room["amenities"])
        speak(f"The {room_type} room is available for {final_price} dollars per night after a discount of {discount}%. "
              f"It includes amenities like {amenities}.")
    else:
        speak("Sorry, I couldn't find that room type.")

def book_room(room_type):
    """Book a room if available."""
    hotel_data = load_hotel_data()
    if "rooms" in hotel_data and room_type in hotel_data["rooms"]:
        room = hotel_data["rooms"][room_type]
        if room["available"] > 0:
            room["available"] -= 1
            save_hotel_data(hotel_data)
            speak(f"Successfully booked a {room_type} room at {hotel_data['hotel_name']}.")
            return True
        else:
            speak(f"Sorry, no {room_type} rooms are available.")
            return False
    else:
        speak("Sorry, I couldn't find that room type.")
        return False

def check_room_availability():
    """List available room types."""
    hotel_data = load_hotel_data()
    available_rooms = []
    for room_type, room in hotel_data["rooms"].items():
        if room["available"] > 0:
            available_rooms.append(room_type)
    if available_rooms:
        speak(f"We have the following rooms available: {', '.join(available_rooms)}.")
    else:
        speak("I'm sorry, but no rooms are available at the moment.")

def faq_details(query):
    """Provide answers to frequently asked questions."""
    hotel_data = load_hotel_data()
    faq_responses = {
        "check-in": hotel_data["faqs"].get("check_in_out", "I don't have information on check-in and check-out times."),
        "parking": hotel_data["faqs"].get("parking", "I don't have information on parking."),
        "pets": hotel_data["faqs"].get("pets", "I don't have information on pets.")
    }
    if "check-in" in query or "check out" in query:
        speak(faq_responses["check-in"])
    elif "parking" in query:
        speak(faq_responses["parking"])
    elif "pets" in query:
        speak(faq_responses["pets"])
    else:
        speak("I'm sorry, I don't have information on that. Please ask about check-in times, parking, or pets.")

def voice_bot():
    """Main bot interaction logic."""
    greet()
    while True:
        query = listen()

        # Check room availability
        if "available" in query and "room" in query:
            check_room_availability()

        # Room details requests
        elif "single" in query and "book" not in query:
            room_details("single")

        elif "double" in query and "book" not in query:
            room_details("double")

        elif "suite" in query and "book" not in query:
            room_details("suite")

        # Booking request
        elif "book" in query:
            if "single" in query:
                if book_room("single"):
                    break
            elif "double" in query:
                if book_room("double"):
                    break
            elif "suite" in query:
                if book_room("suite"):
                    break
            else:
                speak("Sorry, I didn't understand the room choice. Please specify single, double, or suite.")

        # FAQ requests
        elif any(keyword in query for keyword in ["check-in", "check out", "parking", "pets"]):
            faq_details(query)

        # Exit the bot
        elif any(keyword in query for keyword in ["stop", "exit", "quit", "goodbye"]):
            speak("Goodbye! Have a great day!")
            break

        # Unknown request
        else:
            speak("Sorry, I didn't understand your request. Please ask about room availability, pricing, or booking.")

if __name__ == "__main__":
    voice_bot()
