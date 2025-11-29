# Function:  practice building a demo of a large language model (LLM)-based AI system.
# First Step is Select OPENAI API 
# Second Step is build a synthetic dataset for Information Retrival task.
## The Synthetic dataset should include at least 5 documents with relevant information.
## Each Document should have a unique identifier, feature, and count.
## Unique Identifier: US, UK, IT, DE, APAC
## Feature: Browse, Recording, T9 Search, Voice Search, Alpha Search, Purchase
## Count: Random number between 1k to 10M
# Third Step is build a demo application that uses the LLM to perform Information Retrival task using the synthetic dataset.
# Make sure to include necessary prompts for each step to capture correct information.


from openai import OpenAI
from typing import Dict

client = OpenAI()


# Synthetic dataset for Information Retrieval task
synthetic_dataset = [
    {"id": "US", "feature": "Browse", "count": 5000000},
    {"id": "US", "feature": "Recording", "count": 200000},
    {"id": "US", "feature": "T9 Search", "count": 750000},
    {"id": "US", "feature": "Voice Search", "count": 3000000},
    {"id": "US", "feature": "Alpha Search", "count": 500000},  
    {"id": "US", "feature": "Purchase", "count": 4500000},

    {"id": "UK", "feature": "Browse", "count": 300000},
    {"id": "UK", "feature": "Recording", "count": 1200000},
    {"id": "UK", "feature": "T9 Search", "count": 200000},
    {"id": "UK", "feature": "Voice Search", "count": 1500000},
    {"id": "UK", "feature": "Alpha Search", "count": 300000},  
    {"id": "UK", "feature": "Purchase", "count": 200000},

    {"id": "IT", "feature": "Browse", "count": 200000},
    {"id": "IT", "feature": "Recording", "count": 10000},
    {"id": "IT", "feature": "T9 Search", "count": 7000},
    {"id": "IT", "feature": "Voice Search", "count": 40000},
    {"id": "IT", "feature": "Alpha Search", "count": 3000},  
    {"id": "IT", "feature": "Purchase", "count": 4000},

    {"id": "DE", "feature": "Browse", "count": 50000},
    {"id": "DE", "feature": "Recording", "count": 1000},
    {"id": "DE", "feature": "T9 Search", "count": 700},
    {"id": "DE", "feature": "Voice Search", "count": 80000},
    {"id": "DE", "feature": "Alpha Search", "count": 6000},  
    {"id": "DE", "feature": "Purchase", "count": 4500},

    {"id": "APAC", "feature": "Browse", "count": 50000},
    {"id": "APAC", "feature": "Recording", "count": 1000},
    {"id": "APAC", "feature": "T9 Search", "count": 7000},
    {"id": "APAC", "feature": "Voice Search", "count": 430000},
    {"id": "APAC", "feature": "Alpha Search", "count": 32000},  
    {"id": "APAC", "feature": "Purchase", "count": 45000},
]

#print(synthetic_dataset)

def retrieve_information(region: str, feature: str) -> Dict:
    """
    Retrieve information from the synthetic dataset based on region and feature.
    
    :param region: The unique identifier for the region (e.g., US, UK, IT, DE, APAC).
    :param feature: The feature to retrieve information for (e.g., Browse, Recording, T9 Search, Voice Search, Alpha Search, Purchase).
    :return: A dictionary containing the relevant information or a message if not found.
    """
    for document in synthetic_dataset:
        if document["id"] == region and document["feature"] == feature:
            return document
    return {"message": "No data found for the specified region and feature."}


#print(retrieve_information("US", "Browse"))



def llm_information_retrieval(region: str, feature: str) -> str:
    info = retrieve_information(region, feature)

    prompt = f"""
Here is the synthetic dataset for the Information Retrieval task:
{synthetic_dataset}

Using only the dataset above, answer:

1. Which region is using more & less Browse?
2. Which region is purchasing more and what is your insight into that?
3. Which country use Voice and Alpha Search on equal terms?
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that analyzes usage metrics."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=500,
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()





#print(llm_information_retrieval("US", "Browse"))
# Example usage of the LLM-based information retrieval
result = llm_information_retrieval("US", "Browse")
print(result)




