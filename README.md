# AI Report Generator (with GPT-3.5)

This Python tool generates professional, AI-powered business reports from your CSV data. It uses **Pandas** for data analysis and the **OpenAI GPT-3.5 API** to convert raw statistics into human-friendly, insightful summaries — perfect for reports, presentations, or quick business insights.

---

## ⚡ Features
✅ Reads CSV data  
✅ Calculates statistical summaries using Pandas  
✅ Uses OpenAI GPT-3.5 to generate clear, professional text reports  
✅ Saves the AI-generated report as a `.txt` file  
✅ Quick and easy for non-technical users  

---

## 🛠️ Requirements
- Python 3.x  
- `pandas`  
- `requests`  
- OpenAI API Key (store in `config.py` as `api_key = "YOUR_KEY_HERE"`)

---

## 🚀 How to Use
1. Ensure your `.csv` file is ready in the project folder  
2. Add your OpenAI API key to `config.py`  
3. Run the script:  
   ```bash
   python AI_report_generator.py
