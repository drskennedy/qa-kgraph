# Customizing Knowledge Graphs Constructed Using LlamaIndex module PropertyGraphIndex

**Step-by-step guide on Medium**: [Customizing Knowledge Graph Generation and Querying for Improved Response](https://medium.com/ai-advances/customizing-knowledge-graph-generation-and-querying-for-improved-response-ef2e269f4395?sk=18773c1bcfdf742073091dfb8d98193a)
___
## Context
Knowledge graphs are expected to improve adaptation of LLMs to niche domains, as they capture semantics or relationships underlying entities captured from internal documents unlike Retrieval-Augmented Generation. The latter additionally suffers from hallucinations, which is expected to be better handled by knowledge-graph powered LLMs.

In this project, we develop a QA application using `LlamaIndex`'s module `PropertyGraphIndex` powered by a locally hosted LLM loaded using `llama-cpp-python`. This app is tested using 5 different pre-downloaded models from HuggingFace.
<br><br>
![Knowledge Graph](/assets/kgraph.png)
___
## How to Setup Python virtual environment
- Create and activate the environment:
```
$ python3.11 -m venv kg_qa
$ source kg_qa/bin/activate
```
- Install libraries:
```
$ pip install -r requirements.txt
```
- Download Mistral-7B-Instruct-v0.3.Q2_K.gguf from [MaziyarPanahi HF repo](https://huggingface.co/MaziyarPanahi/Mistral-7B-Instruct-v0.3-GGUF) to directory `models`.
- Download Phi-3-mini-4k-instruct-q4.gguf from [Microsoft HF repo](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/blob/main/Phi-3-mini-4k-instruct-q4.gguf) to directory `models`.
- Run script `main.py` to start the testing:
```
$ python main.py
```
___
## Quickstart
- To start the app, launch terminal from the project directory and run the following command:
```
$ source kg_qa/bin/activate
$ python main.py
```
- Here is a sample run:
```
$ python main.py
Query: When should simplified routing be used on SteelHeads?

Response:  Simplified routing should be enabled in scenarios with multiple LAN subnets or multiple VLANs on the LAN segment that need to be optimized through the Steelhead.
Time: 36.15
================================================================================
Node ID: 9c8bf5d2-f4b1-4221-8d47-1e86b7c9777e
Text: Here are some facts extracted from the provided text:
Simplified routing -> Can be enabled in scenarios with -> Multiple lan
subnets and vlans  recommends setting Simpliﬁed Routing to Dest Only.•
Simpliﬁed routing can't be used with broadcast support.• Simpliﬁed
routing can't be used with WCCP.• Simpliﬁed routing can't be used with
PBR.• Simpli...
Score:  1.000
...
================================================================================
Query: Under what situations simplified routing should not be enabled on SteelHeads?

Response:  Simplified routing can't be used with broadcast support, WCCP, PBR, or in an Interceptor deployment.
Time: 35.46
================================================================================
Node ID: 9c8bf5d2-f4b1-4221-8d47-1e86b7c9777e
Text: Here are some facts extracted from the provided text:
Simplified routing -> Can be enabled in scenarios with -> Multiple lan
subnets and vlans  recommends setting Simpliﬁed Routing to Dest Only.•
Simpliﬁed routing can't be used with broadcast support.• Simpliﬁed
routing can't be used with WCCP.• Simpliﬁed routing can't be used with
PBR.• Simpli...
Score:  1.000
...
================================================================================
Query: If you have an asymmetric setup through the SteelHead, does it have any impact on the simplified routing feature?

Response:  Yes, if you have an asymmetrically routed network, source-gathering methods (such as Simplified Routing set to Source-Dest or All) might cause undesirable results. For these networks, Riverbed recommends setting Simplified Routing to Dest Only.
Time: 40.28
================================================================================
Node ID: 9c8bf5d2-f4b1-4221-8d47-1e86b7c9777e
Text: Here are some facts extracted from the provided text:  Steelhead
-> Requires default route on -> Each router Simplified routing -> Can
be enabled in scenarios with -> Multiple lan subnets and vlans
Steelhead -> Has version number 6.0 or later -> For deployment guide
details Steelhead -> Uses virtual routers -> May use virtual macs
Steelhead -> S...
Score:  1.000
...
================================================================================
```
___
## Key Libraries
- **LlamaIndex**: Framework for developing applications powered by LLM
- **llama-cpp-python**: Library to load GGUF-formatted LLM from a local directory

___
## Files and Content
- `models`: Directory hosting the downloaded LLM in GGUF format
- `pdf`: Directory hosting the sample niche domain documents
- `main.py`: Main Python script to launch the application
- `requirements.txt`: List of Python dependencies (and version)
___

## References
- https://docs.llamaindex.ai/en/stable/module_guides/indexing/lpg_index_guide/
