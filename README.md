# AI Portfolio Tracker Bot

A simple AI-powered bot for tracking cryptocurrency portfolios, accessible via X (formerly Twitter). Users can interact with the bot by mentioning it in tweets or sending a direct message (DM) with their wallet address. The bot fetches wallet balances, token holdings, and performance data to provide a concise portfolio summary.

## Features
- Fetch wallet balances and token holdings from blockchain explorers.
- Respond to mentions or DMs with portfolio summaries.
- Support for Ethereum blockchain (extendable to other chains).
- Basic error handling for invalid wallet addresses or API errors.

## Tech Stack
- **Programming Language**: Python
- **APIs**:
  - Twitter API (via Tweepy) for user interaction.
  - Etherscan API for blockchain data.
- **Hosting**: Heroku, AWS Lambda, or any cloud service.

## Project Structure
```
portfolio-tracker-bot/
├── app/
│   ├── __init__.py
│   ├── twitter_bot.py       # Handles Twitter API integration
│   ├── blockchain_api.py    # Interacts with blockchain explorers
│   ├── portfolio_manager.py # Processes and formats wallet data
│   └── utils.py             # Helper functions
├── config/
│   ├── config.py            # Stores API keys and configurations
├── requirements.txt         # Python dependencies
├── main.py                  # Entry point to run the bot
└── README.md                # Documentation
```

## Prerequisites
1. Python 3.7+
2. Twitter Developer Account to create an app and obtain API keys.
3. Etherscan API key for accessing blockchain data.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/portfolio-tracker-bot.git
   cd portfolio-tracker-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up API keys in `config/config.py`:
   ```python
   TWITTER_API_KEY = "your_twitter_api_key"
   TWITTER_API_SECRET = "your_twitter_api_secret"
   TWITTER_ACCESS_TOKEN = "your_access_token"
   TWITTER_ACCESS_SECRET = "your_access_secret"
   ETHERSCAN_API_KEY = "your_etherscan_api_key"
   ```

## Usage
1. Run the bot:
   ```bash
   python main.py
   ```
2. Interact with the bot by tweeting or DMing it with your wallet address (e.g., `@CryptoAgentBot track 0x123...`).
3. The bot will reply with a summary of your wallet balance and holdings.

## Future Enhancements
- Multi-chain support (e.g., BSC, Polygon, Solana).
- Price alerts for significant changes in token values.
- Portfolio performance tracking over time.
- Integration with more blockchain explorers for detailed data.

## Contributions
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

## License
This project is licensed under the MIT License.

---
For questions or support, contact odoch1m3z13@gmail.com or open an issue on GitHub.

