from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate 

#instruction to the llm model to follow when answering the prompt frm user
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)



model = OllamaLLM(model='llama3')

def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template) #create a prompt template
    chain = prompt | model #chain the prompt from model

    parse_content = []

    #iterate through the chuns and pass them through
    for i, chunk in enumerate(dom_chunks, start=1):
        #parse the contnet a chunk at a time.
        response = chain.invoke({ 'dom_content': chunk, 'parse_description': parse_description })
        print(f"Parsed Chunk {i} of the total {len(dom_chunks)}")
        parse_content.append(response)

    return "\n".join(parse_content)