
---

📊 AI Analyst Assistant – Real-Time NLP & Market Insight Chatbot

An intelligent, real-time AI Analyst Assistant that helps users interact with technical indicators, sentiment trends, market patterns, and news analytics — all through a seamless chat interface.

Powered by LLaMA 4 Marvick, this assistant supports intent detection, technical analysis, pattern detection, and social/news sentiment analysis, offering an integrated AI-powered decision-making tool for markets like crypto and finance.


---

🚀 Features

🧠 LLM-Based Intent Detection
Understands user queries contextually using LLaMA 4 Marvick and routes them to analytical modules.

📈 Technical Analysis & Pattern Detection
Detects RSI, EMA crossovers, candlestick formations, and market trend shifts.

🗣️ Natural Language Chat Interface
Seamless WebSocket chat, frontend-ready, supports real-time interaction.

🔌 Modular NLP Handler
trading_assistant_nlp_handler.py is a plug-and-play module for any AI project.

📰 Live News & Social Sentiment
Scrapes Reddit, Twitter/X, and financial news sources for real-time sentiment trends.

📊 Sentiment Analysis Engine
Supports VADER/TextBlob/custom models for analyzing market mood.

⚡ WebSocket-Enabled FastAPI Server
Real-time backend powered by main_websocket_api.py.



---

🧱 Tech Stack


---

📂 Project Structure

├── main_websocket_api.py            # FastAPI WebSocket backend server
├── trading_assistant_nlp_handler.py # NLP + AI logic module
├── frontend/                        # (Optional) Frontend client
├── requirements.txt
└── README.md


---

⚙️ Getting Started

# Clone the repository
git clone https://github.com/Collins-ifedi/CryptSignal-AI.git
cd CryptSignal-AI

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # or use `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Run the WebSocket API server
uvicorn main_websocket_api:app --reload

# OR run the trading_assistant_nlp_handler.py
---

🧪 Example Prompts

"Give me technical analysis on Ethereum"
"What's the Twitter sentiment around Bitcoin?"
"Detect patterns in Solana's recent trend"
"Are there bullish signals in Dogecoin right now?"


---

🌐 Integrate the Core NLP Module

from trading_assistant_nlp_handler import analyze_user_input

response = analyze_user_input("Show me the RSI for Ethereum.")
print(response)

Returns structured insights:

{
  "intent": "technical_analysis",
  "symbol": "ETH",
  "response": "Ethereum is currently overbought with RSI > 70 and showing bullish EMA crossover."
}


---

📈 Real-World Use Cases

Crypto & stock chatbots

AI-based trading dashboards

Fintech NLP insight engines

AI-powered portfolio tools



---

🛣️ Roadmap

[ ] Voice-to-text input support

[ ] SHAP or XAI visualizations

[ ] Hugging Face demo deployment

[ ] Binance & Bybit trading API integration

[ ] Telegram/Slack assistant version



---

👨‍💻 Author

Chukwujiekwu Collins Ifedi 


---

🌟 Support

If you find this project helpful:

⭐ Star it
🍴 Fork it
📣 Share it

Pls, do not forget to adjust the root path of the code and also the api keys found in the file credentials.yaml in the config folder. 
