## Emedding and Vector Store
	1. Langachain come with build in loader tools to quickly load files to its document object.
	2. many loaders require other libraries like PDF loading requires pypdf lib and HTML loading requires BS4 lib.
	3. Choose initial embedding model very carefully. Different embedding model cannot interact with each other. Let say you choose embedding model A to embed a document and later swtiched to embedding model B to embedd new documents, those embedding will be on different set of dimension with different set of trained models and cosine similarity will no longer work between those 2 models. That means if u have historical vector store and your organization decides to switch to some new/better embedding model u need to reembedd all your historical vectorized documents. this also means u have to store intital text documents because u are not able to go from vector to new vector. u have to go from original string to new vector. 
	4. embedding method in general accept strings. so if we want to emedd a csv file. how to do it.
		1. for csv file, u will first load and when u print, it will be list of Documents. 
		2. so u have to ge the page content out of all the list of document ecause page content is string.

 ## MultiQuery Retrievel Strategy
 
 1. MultiQueryRetriever is a retrieval strategy in LangChain that improves recall by generating multiple reformulated versions of your query using an LLM, then retrieving documents for each version.
	a. Then it embeds each generated query
	b. Retrieves result for each.
	c. Merges and deduplicates them.
	d. Returns the combined set.

	
	#### Purpose:
	1. Vector search is semantic not magic. Basic similarity seach might miss it. MultiqueryRetriever reduces that mismatch by expanding the question space.

	#### When to use it:
	1. Document too large or complex.
	2. User questions are vague.
	3. Terminology differs between query and document.
	4. You care more more about recall than speed.

	#### When not to use it:
	1. Tiny documents.
	2. Latency must be minimal.
	
	#### Cons:
	1. It increases cost and latency because it calls an LLM.

	###### Normal Retrieveal: 
	User Query → Embed → Similarity Search → Top K

	###### MultiQuery Retrieveal: 
	User Query
      	  ↓
	LLM generates N reformulated queries
	      ↓
	Each query embedded separately
	      ↓
	Multiple similarity searches
	      ↓
	Combine + deduplicate results


## Context Compression:
1. We returned the entirety of the vectorized document. Ideally we would pass this document as context to an LLM to get more relevant (compressed) answer.
2. Just making the reply more smaller and clear.
	
	#### Method-1: Manual Compression:
	1. Create Basic Retriever
	2. Retrieve Documents
	3. Loop through all retrieved document and invoke LLM with supplied query and document.


	#### Method-2: Runnable Pipeline
		User Question
			↓
		Retriever gets context
			↓
		Prompt is constructed
			↓
		LLM generates answer
			↓
		Output converted to string   

	1. Create a runnable pipeline.
	2. The json here is Runnable Map.
	3. Mental Model:
		a. Think of each component as Runnable = something that takes input → returns output
		b. And | means: output_of_left → input_of_right