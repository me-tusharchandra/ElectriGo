import random

# Dictionary of responses
responses = {
    "hello": "Hello! I'm the EV Chatbot. How can I assist you today?",
    "हैलो": "हैलो! मैं ईवी चैटबॉट हूं। आज मैं आपकी कैसे सहायता कर सकता हूं?",
    "bye": "Goodbye! Feel free to come back if you have more questions.",
    "hindi":"नमस्ते! मैं ईवी चैटबॉट हूं। आज मैं आपकी कैसे सहायता कर सकता हूँ?",
    "ev benefits": "Electric vehicles are environmentally friendly, have lower operating costs, and offer a smooth and quiet ride.",
    "इलेक्ट्रिक वाहन लाभ": "इलेक्ट्रिक वाहन पर्यावरण के अनुकूल हैं, उनकी परिचालन लागत कम है, और एक सहज और शांत सवारी प्रदान करते हैं।",
    "charging time": "Charging times for electric vehicles vary depending on the charger type. Level 1 chargers (standard outlets) take longer, while Level 2 chargers are faster. DC fast chargers provide rapid charging.",
    "चार्ज का समय": "इलेक्ट्रिक वाहनों के लिए चार्जिंग समय चार्जर के प्रकार के आधार पर भिन्न होता है। लेवल 1 चार्जर (मानक आउटलेट) अधिक समय लेते हैं, जबकि लेवल 2 चार्जर तेज़ होते हैं। डीसी फास्ट चार्जर तेजी से चार्जिंग प्रदान करते हैं।",
    "range": "The range of an electric vehicle depends on the model. Modern EVs typically have ranges of 100-300 miles or more on a single charge.",
    "श्रेणी": "इलेक्ट्रिक वाहन की रेंज मॉडल पर निर्भर करती है। आधुनिक ईवी में आमतौर पर एक बार चार्ज करने पर 100-300 मील या उससे अधिक की रेंज होती है।",
    "charging stations": "Charging stations for EVs are becoming more common. You can find them at public places, shopping centers, and along highways. Many apps and websites help you locate charging stations.",
    "चार्जिंग स्टेशन": "ईवी के लिए चार्जिंग स्टेशन आम होते जा रहे हैं। आप उन्हें सार्वजनिक स्थानों, शॉपिंग सेंटरों और राजमार्गों पर पा सकते हैं। कई ऐप्स और वेबसाइटें आपको चार्जिंग स्टेशन ढूंढने में मदद करती हैं।",
    "maintenance": "EVs generally have lower maintenance costs than traditional vehicles since they have fewer moving parts and don't require oil changes.",
    "रखरखाव": "ईवी में आमतौर पर पारंपरिक वाहनों की तुलना में रखरखाव की लागत कम होती है क्योंकि उनके चलने वाले हिस्से कम होते हैं और तेल बदलने की आवश्यकता नहीं होती है।",
    "cost": "The cost of an electric vehicle varies based on the make and model. While the upfront cost might be higher, you can save money over time due to lower fuel and maintenance costs.",
    "लागत": "इलेक्ट्रिक वाहन की लागत मेक और मॉडल के आधार पर भिन्न होती है। हालांकि प्रारंभिक लागत अधिक हो सकती है, आप कम ईंधन और रखरखाव लागत के कारण समय के साथ पैसे बचा सकते हैं।",
    "environment": "Electric vehicles produce fewer emissions compared to traditional internal combustion engine vehicles, which helps reduce air pollution and greenhouse gas emissions.",
    "पर्यावरण": "इलेक्ट्रिक वाहन पारंपरिक आंतरिक दहन इंजन वाहनों की तुलना में कम उत्सर्जन पैदा करते हैं, जो वायु प्रदूषण और ग्रीनहाउस गैस उत्सर्जन को कम करने में मदद करते हैं।",
    "performance": "Many electric vehicles offer instant torque and smooth acceleration, providing excellent performance and driving experience.",
    "प्रदर्शन": "कई इलेक्ट्रिक वाहन तत्काल टॉर्क और सहज त्वरण प्रदान करते हैं, उत्कृष्ट प्रदर्शन और ड्राइविंग अनुभव प्रदान करते हैं।",
    "tax incentives": "In many regions, there are tax incentives, rebates, and subsidies available to encourage the adoption of electric vehicles.",
    "कर प्रोत्साहन": "कई क्षेत्रों में, इलेक्ट्रिक वाहनों को अपनाने को प्रोत्साहित करने के लिए कर प्रोत्साहन, छूट और सब्सिडी उपलब्ध हैं।",
    "default": "I'm sorry, I'm not sure I understand that question. Can you please rephrase or ask something else?"
    
}

def ev_chatbot():
    print("----------------> Welcome to the EV Chatbot! Type 'bye' to exit <----------------")
    print(" Choose Language ")
    while True:

        print("विकल्प संख्या चुनें : ")
        print("1) इलेक्ट्रिक वाहन लाभ")
        print("2) चार्ज का समय")
        print("3) श्रेणी")
        print("4) चार्जिंग स्टेशन")
        print("5) रखरखाव")
        print("6) लागत")
        print("7) पर्यावरण")
        print("8) प्रदर्शन")
        print("9) कर प्रोत्साहन")

        user_input = input("You: ").lower()
        
        if user_input == 'bye':
            print(responses["bye"])
            

        if user_input == 'hello':
            print(responses["hello"])
            

        if user_input == 'ev benefits':
            print(responses["ev benefits"])
            

        if user_input == 'charging time':
            print(responses["charging time"])
            

        if user_input == 'range':
            print(responses["range"])
            

        if user_input == 'charging stations':
            print(responses["charging stations"])
            

        if user_input == 'maintenance':
            print(responses["maintenance"])
            

        if user_input == 'cost':
            print(responses["cost"])
            

        if user_input == 'performance':
            print(responses["performance"])
            

        if user_input == 'tax incentives':
            print(responses["tax incentives"])
            

        if user_input == 'hindi':
            print(responses["hindi"])

        if user_input == '1':
            print(responses["इलेक्ट्रिक वाहन लाभ"])
            
        if user_input == '2':
            print(responses["चार्ज का समय"])

        if user_input == '3':
            print(responses["श्रेणी"])

        if user_input == '4':
            print(responses["चार्जिंग स्टेशन"])

        if user_input == '5':
            print(responses["रखरखाव"])

        if user_input == '6':
            print(responses["लागत"])

        if user_input == '7':
            print(responses["पर्यावरण"])

        if user_input == '8':
            print(responses["प्रदर्शन"])

        if user_input == '9':
            print(responses["कर प्रोत्साहन"])    

        # response = responses.get(user_input, responses["default"])
        # print("EV Chatbot:", response)

ev_chatbot()