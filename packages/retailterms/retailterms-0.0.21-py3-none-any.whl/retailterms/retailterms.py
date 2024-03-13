import re
import pandas as pd
from string import punctuation
import warnings
warnings.filterwarnings("ignore")
import spacy
from pkg_resources import resource_filename
filepath = resource_filename('retailterms', 'rt.xlsx')

def get_retail_entities(text):
    global company_list
    global output
    company_list=[]
    type_list=[]
    data=pd.read_excel(filepath)
    
    company_list = data["Entity Name"].to_list()
    for i in range(len(company_list)):
        company_list[i] =company_list[i].lower()
        
    type_list=data["type"].to_list()
    for i in range(len(type_list)):
        type_list[i] = type_list[i].lower()
       
    nlp=spacy.load("en_core_web_sm")
    
    tokens=[]
    doc=nlp(text)
    for ent in doc:
        tokens.append(ent)
        
    tokens=list(map(str,tokens))
    for i in range(len(tokens)):
        tokens[i] =tokens[i].lower()
        
    set1 = set(company_list)
    set2 = set(tokens)
    
    common_elements=set1.intersection(set2)
    common_elements_list= list(common_elements)
    
    data["Entity Name"] = data["Entity Name"].apply(str.lower)
    positions = data.loc[data["Entity Name"].isin(common_elements_list), 'Entity Name'].index.values
    data_copy =pd.read_excel(filepath)
    output=data_copy.loc[positions,:]
    return print(output.to_string(index=False))


