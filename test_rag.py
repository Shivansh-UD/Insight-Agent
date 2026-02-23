from rag.vector_store import add_documents, retrieve

# Step 1: Clear test data
docs = [
    "AI helps detect cancer in medical imaging using deep learning.",
    "Hospitals use predictive analytics to reduce patient readmission rates.",
    "Chatbots assist patients by answering healthcare-related questions.",
    "Climate change affects global agriculture and food security."
]

# Step 2: Add documents
add_documents(docs)

# Step 3: Test retrieval
query = "How does climate impact farming?"
results = retrieve(query)

print("\nQuery:", query)
print("\nRetrieved Results:\n")

for r in results:
    print("-", r)