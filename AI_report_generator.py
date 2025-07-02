import pandas as pd
import requests
import os
from config import api_key

def main():
    csv_file = input("Enter CSV file name (with .csv extension): ")


    # GPT API setup
    url = "https://api.openai.com/v1/chat/completions"
    headers ={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Read and clean data
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"File '{csv_file}' not found. Please check the filename.")
        exit()

    print("\nData Preview:\n", df.head())

    # Basic Pandas stats summary
    summary_stats = df.describe(include="all").to_string()

    # Send summary to GPT for human-friendly report
    prompt_text = f"Summarize this dataset insightfully for a client report:\n\n{summary_stats}"

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You generate professional business summaries."},
            {"role": "user", "content": prompt_text}
        ],
        "max_tokens": 500
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        print("❌ API Error:", response.text)
        exit()

    result = response.json()

    # Extract AI generated report
    report_text = result["choices"][0]["message"]["content"].strip()


    output_file = f"AI_Report_{os.path.splitext(csv_file)[0]}.txt"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(report_text)

    print(f"\n✅ AI-generated report saved as '{output_file}'.")
    print("\n📄 Report Preview:\n", report_text)


if __name__ == "__main__":
    main()