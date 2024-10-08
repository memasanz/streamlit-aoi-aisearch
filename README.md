# streamlit-aoi-aisearch

https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/use-your-data-securely#role-assignments

### Configure your environment file: .env
```
AZURE_SEARCH_SERVICE_ENDPOINT = "https://aisearch.search.windows.net"
AZURE_SEARCH_ADMIN_KEY = "zkaN6K2"
AZURE_SEARCH_INDEX = "stor-int-vector-index-ada-002"
AZURE_SEARCH_SEMANTIC_SEARCH_CONFIG = "my-semantic-config"
BLOB_STORAGE_FOR_URL = "https://storage.blob.core.windows.net/data/"
BLOB_CONNECTION_STRING = "Defaul+HCm45/Oows.net"
BLOB_CONTAINER_NAME = "data"
AZURE_OPENAI_ENDPOINT = "https://xmm-openai-eastus.openai.azure.com/"
AZURE_OPENAI_KEY = "10aa"
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = "text-embedding-ada-002" 
AZURE_OPENAI_EMBEDDING_MODEL_NAME =  "text-embedding-ada-002"
AZURE_OPENAI_EMBEDDING_DIMENSIONS =  1536 
AZURE_OPENAI_MODEL = "gpt-4o"
#must be in region that AI SEarch is in.
AZURE_AI_SERVICES_KEY = "750"
```


| Role                           | Assignee       | Resource          | Description                                                                                                  |  
|--------------------------------|----------------|-------------------|--------------------------------------------------------------------------------------------------------------|  
| Search Index Data Reader        | Azure OpenAI   | Azure AI Search   | Inference service queries the data from the index.                                                           |  
| Search Service Contributor      | Azure OpenAI   | Azure AI Search   | Inference service queries the index schema for auto fields mapping. Data ingestion service creates index, data sources, skill set, indexer, and queries the indexer status. |  
| Storage Blob Data Contributor   | Azure OpenAI   | Storage Account   | Reads from the input container, and writes the preprocessed result to the output container.                   |  
| Cognitive Services OpenAI Contributor | Azure AI Search | Azure OpenAI  | Custom skill.                                                                                                |  
| Storage Blob Data Reader        | Azure AI Search | Storage Account   | Reads document blobs and chunk blobs.                                                                         |  
| Cognitive Services OpenAI User  | Web app        | Azure OpenAI      | Inference.                                                                                                   |  