# PDF Text Extractor (Offline)

This project is a simple and lightweight tool that extracts **clean full text** from PDFs using **Python** and **PyMuPDF**. It is designed to run completely offline without requiring any API or external service.

---

## ✅ Features

- 💡 Extracts all text from each page in order
- 📴 100% offline — no internet or API keys needed
- 📄 Supports multi-page PDFs
- 🔍 Handles scanned PDFs if text layer is present

---

## 🛠️ Technologies Used

- Python 3.x
- PyMuPDF (`fitz`)
- Streamlit (for UI)

---

## 📁 File Structure

📦pdf-text-extractor
┣ 📄extract_text.py # Core logic for text extraction
┣ 📄app.py # Streamlit UI for file upload and output
┣ 📄README.md # Project overview
┗ 📄requirements.txt # Dependency list


## 🚀 How to Run Locally

1. Clone the Repository

```bash
git clone https://github.com/<your-username>/pdf-text-extractor.git
cd pdf-text-extractor
2. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
