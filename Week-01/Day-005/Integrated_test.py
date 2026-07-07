from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer 

# Load the model 
model = SentenceTransformer("all-MiniLM-L6-v2")

paragraphs = [
    "Phishing is a social engineering attack where attackers trick people into revealing sensitive information such as passwords or credit card numbers. These attacks often arrive through emails, text messages, or fake websites that appear to be trustworthy.",
    "SQL injection is a web application vulnerability that occurs when user input is inserted into database queries without proper validation. Attackers can manipulate the query to read, modify, or delete information stored in the database.",
    "Malware is malicious software designed to damage systems, steal information, or disrupt normal operations. Common types include ransomware, spyware, worms, and trojans, each with different methods of infecting a computer.",
    "A firewall monitors incoming and outgoing network traffic and decides whether to allow or block connections based on predefined security rules. It helps protect systems from unauthorized access and reduces the attack surface of a network.",
    "Machine learning enables computers to identify patterns from data without being explicitly programmed for every situation. It is widely used in image recognition, recommendation systems, fraud detection, and natural language processing."
]

# create the embeddings of the paragraphs
paragraph_embeddings = model.encode(paragraphs)

# take the user query 
query = input(f"Enter the query: ")

# convert the user query to embeddings 
query_embedding = model.encode(query)

similarities = cosine_similarity([query_embedding], paragraph_embeddings)

result = similarities.argmax()

similarity_score = similarities[0][result]

# output 
print("Query: ", query)
print("Best Match: ")
print(paragraphs[result])
print(f"Similarity Score: {similarity_score:.4f}")