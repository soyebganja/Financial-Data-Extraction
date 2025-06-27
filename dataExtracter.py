from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException


from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model_name="llama-3.3-70b-versatile")

def extract(article_text):
  prompt = '''
    From the below news article, extract revenue and eps in json format containing the
    following keys:
    - revenue_actual, revenue_expected
    - eps_actual, eps_expected

    Each value should have a unit such as million, billion cents etc... and currency symbol.

    Only return the valid JSON, no preamble.

    Article
    *********
    {article}
  '''

  pt = ChatPromptTemplate.from_messages([("human", prompt)])
  global llm
  chain = pt | llm

  res = chain.invoke({"article": article_text})

  parser = JsonOutputParser()
  try:
    response = parser.parse(res.content)
  except OutputParserException as e:
    raise OutputParserException("Context too big. Unable to parse jobs.")
  
  return response