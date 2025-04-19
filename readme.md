1. Run the virtual environment 
`source venv/bin/activate`

2. Install all necessary packages at the requirement.txt
`pip install -r requirements.txt`

3. Run the project by
`python3 app.py`

4. To interact, open CMD and follow the below instruction:

**To make sure your file is read and analyzed by the RAG model:**
curl --request POST \
--url http://localhost:8080/embed \
--header 'Content-Type: multipart/form-data' \
--form "file=@/Users/joshuafaburada/Local-Work/SelfExploration/local-rag/Joshua Faburada Resume.pdf"

**Now we want to send inquiry based on that pdf file:**
curl -X POST http://localhost:8080/query \
     -H "Content-Type: application/json" \
     -d '{"query": "How many years of experience does Joshua have?"}'