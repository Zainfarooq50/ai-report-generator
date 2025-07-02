🧠 AI Report Generator (with GPT-3.5)
This Python tool analyzes your CSV data and generates professional, AI-powered summaries using Pandas and the OpenAI GPT-3.5 API. Ideal for client-ready business reports, presentations, or extracting quick insights from raw data.

⚡ Features
✅ Reads and cleans CSV data
✅ Generates statistical summaries using pandas
✅ Sends data to GPT-3.5 for human-friendly text generation
✅ Saves the AI-generated summary as a .txt file
✅ Lightweight, easy to run, beginner-friendly setup

🛠️ Requirements
Python 3.x

pandas

requests

python-dotenv

OpenAI API key (added to the provided .env file)

Install dependencies (if needed):

bash
Copy
Edit
pip install pandas requests python-dotenv
🔐 API Key Setup
In the project folder, you’ll find a file named .env.

Open the .env file and paste your OpenAI API key like this:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_api_key_here
Save the file. That’s it — your API key is now ready to use!

🚀 How to Run
Place your .csv file (e.g., sampledata.csv) inside the project folder.

Run the script from your terminal:

bash
Copy
Edit
python AI_report_generator.py
Enter the CSV filename when prompted (e.g., sampledata.csv).

View the AI-generated report in the output .txt file.

📁 Output
A text file named like AI_Report_sampledata.txt will be saved in the same folder.

It contains human-friendly insights generated from your data.
