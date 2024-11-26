
# Hotel Voice Bot

This is a voice-activated bot designed to assist customers with hotel inquiries, such as room availability, pricing, amenities, booking, and frequently asked questions (FAQs) like check-in times or pet policies. The bot uses speech recognition and text-to-speech capabilities to provide a seamless interaction.

---

## **Features**
- Check room availability.
- Get details about room types (single, double, and suite).
- Book a room if available.
- Answer FAQs like:
  - Check-in and check-out times.
  - Pet policy.
  - Parking details.
- Graceful exit upon user request.

---

## **Technologies Used**
- **Python**: Programming language.
- **Libraries**:
  - `speech_recognition`: For voice input.
  - `pyttsx3`: For text-to-speech functionality.
  - `json`: To manage hotel data.

---

## **Installation**

### Prerequisites
- Python 3.7 or later
- A working microphone and audio setup

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/hotel-voice-bot.git
   cd hotel-voice-bot
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the `hotel_data.json` file in the project directory. This file contains hotel details and configurations.

---

## **How to Use**
1. Run the bot:
   ```bash
   python hotel_bot.py
   ```

2. Follow the bot's voice prompts to:
   - Ask about room availability, details, or amenities.
   - Book a room by specifying the type.
   - Inquire about FAQs like check-in times or pet policies.

3. Say **"stop"** or **"exit"** to end the conversation.

---

## **File Structure**
```
.
├── hotel_bot.py          # Main application script
├── hotel_data.json       # Hotel data (rooms, FAQs, etc.)
├── README.md             # Project documentation
├── requirements.txt      # Dependency list for Python packages
```

---

## **Example Interactions**
- **User**: Are there any rooms available?  
  **Bot**: We have single, double, and suite rooms available.

- **User**: Tell me about the suite room.  
  **Bot**: The suite room is available for $300 per night. It includes amenities like WiFi, Luxury Bed, Private Pool, and Mini Bar.

- **User**: Are pets allowed?  
  **Bot**: We allow pets with an additional cleaning fee.

- **User**: What are the check-in and check-out times?  
  **Bot**: Check-in time is 2 PM and check-out time is 11 AM.

- **User**: Exit.  
  **Bot**: Goodbye! Have a great day!

