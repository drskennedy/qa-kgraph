from llama_index.core import (
    PropertyGraphIndex,
    SimpleDirectoryReader,
    Document,
    StorageContext,
    load_index_from_storage,
    Settings,
)
from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.graph_stores import SimpleGraphStore
import timeit
import datetime

# load LLM from local directory
llm = LlamaCPP(
    model_path='./models/mistral-7b-instruct-v0.3.Q2_K.gguf',
    #model_path='./models/Llama-3-Instruct-8B-SPPO-Iter3-Q2_K.gguf',
    #model_path='./models/Phi-3-mini-4k-instruct-q4.gguf',
    #model_path='./models/tinyllama-1.1b-chat-v1.0.Q5_K_M.gguf',
    #model_path='./models/gemma-2-9b-it-Q2_K.gguf',
    temperature=0.1,
    max_new_tokens=256,
    context_window=2048,
    # kwargs to pass to __init__()
    model_kwargs={"n_gpu_layers": 1},
    verbose=False
)
embed_model = HuggingFaceEmbedding()
Settings.llm = llm
Settings.embed_model = embed_model
Settings.chunk_size = 512

# load knowledge graph index from disk
try:
    gstorage_context = StorageContext.from_defaults(persist_dir='./storage')
    kg_index = load_index_from_storage(storage_context = gstorage_context)
except FileNotFoundError:
    graph_store = SimpleGraphStore()
    gstorage_context = StorageContext.from_defaults(graph_store=graph_store)
    documents = SimpleDirectoryReader("./pdf/").load_data()
    start = timeit.default_timer()
    # generate graph
    kg_index = PropertyGraphIndex.from_documents(
        documents,
        storage_context=gstorage_context,
        max_triplets_per_chunk=10,
        include_embeddings=True,
    )
    kg_gen_time = timeit.default_timer() - start # seconds
    print(f'KG generation completed in: {datetime.timedelta(seconds=kg_gen_time)}')
    # save to disk
    gstorage_context.persist()

kg_keyword_query_engine = kg_index.as_query_engine(
    # setting to false uses the raw triplets instead of adding the text from the corresponding nodes
    include_text=True,
    similarity_top_k=2,
)

# load questions from file for querying
with open('qa_list_doc1.txt') as qfile:
    for query in qfile:
        start = timeit.default_timer()
        response = kg_keyword_query_engine.query(query.rstrip())
        kg_qa_resp_time = timeit.default_timer() - start # seconds
        print(f'Query: {query}\nResponse: {response.response}\nTime: {kg_qa_resp_time:.2f}\n{"="*80}')
        # display selected nodes
        for node in response.source_nodes:
            print(node)
        print(f'{"="*80}')

