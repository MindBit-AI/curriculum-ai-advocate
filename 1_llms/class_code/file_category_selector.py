from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os

# Initialize LangChain chat model
llm = ChatOpenAI(
    model="gpt-4-0125-preview",  # GPT-4-mini model
    temperature=0.3
)

def classify_file_type(file_content):
    """Determine if a file is claims, membership, or cag type using GPT"""
    try:
        # Create prompt template with few-shot examples
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a pharmaceutical data analyst. Classify files as 'claims', 'membership', or 'cag' based on their content.
            Here are some examples:
            File content: MemberID,EnrollDate,PlanType,Gender,DOB
            Classification: membership
            File content: ClaimID,DateOfService,NDC,Quantity,PrescriberNPI
            Classification: claims
            File content: GroupID,ContractType,BenefitYear,FormularyCode
            Classification: cag
            """),
            ("user", "File content: {file_content}")
        ])

        # Format prompt with file content
        chain = prompt | llm
        
        # Get classification
        response = chain.invoke({"file_content": file_content})
        
        return response.content
    except Exception as e:
        return f"Error classifying file: {str(e)}"

def main():
    # Sample file contents for testing
    file1 = "PatientID,RxNumber,PharmacyID,DrugName,DaysSupply"
    file2 = "SubscriberID,EffectiveDate,TermDate,RelationshipCode"
    file3 = "ContractID,BenefitDesign,CopayTier,NetworkType"

    # Test the classifier with different files
    print(f"File 1 type: {classify_file_type(file1)}")
    print(f"File 2 type: {classify_file_type(file2)}")
    print(f"File 3 type: {classify_file_type(file3)}")

if __name__ == "__main__":
    main() 