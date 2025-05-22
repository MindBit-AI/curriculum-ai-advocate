"""
PII Guardrails for LLM Calls

This module demonstrates how to implement guardrails to prevent Personal Identifiable
Information (PII) from being sent to LLMs. This helps protect user privacy and comply
with data protection regulations.

Requirements:
- Python 3.8+
- openai
- re (standard library)
"""

import re
import os
from typing import Dict, List, Optional, Union
import openai

# Configure your OpenAI API key (in a real app, use environment variables)
# openai.api_key = os.environ.get("OPENAI_API_KEY")

class PIIGuardrail:
    """
    A guardrail to detect and redact Personal Identifiable Information (PII)
    before sending text to an LLM.
    """
    
    def __init__(self):
        # Define regex patterns for common PII
        self.patterns = {
            # TODO: Add your own pattern to detect names (e.g., "John Smith", "Dr. Jane Doe")
            # Hint: Consider titles (Mr., Mrs., Ms., Dr., Prof.) and proper name capitalization

            # Email addresses
            "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            
            # Phone numbers (various formats)
            "phone": r'\b(\+\d{1,3}\s?)?(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}\b',
            
            # Social Security Numbers (US)
            "ssn": r'\b\d{3}[-]?\d{2}[-]?\d{4}\b',
            
            # Credit card numbers
            "credit_card": r'\b(?:\d{4}[- ]?){3}\d{4}\b',
            
            # Physical addresses (simplified pattern)
            "address": r'\b\d+\s+[A-Za-z0-9\s,]+(?:Avenue|Ave|Street|St|Road|Rd|Boulevard|Blvd|Drive|Dr|Lane|Ln|Court|Ct|Way)[,.\s].*?\b',
            
            # Dates of birth
            "dob": r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b'
        }
        
        # Compile all regex patterns for efficiency
        self.compiled_patterns = {
            pii_type: re.compile(pattern) 
            for pii_type, pattern in self.patterns.items()
        }
    
    def detect_pii(self, text: str) -> Dict[str, List[str]]:
        """
        Detect PII in the given text.
        
        Args:
            text: The input text to check for PII
            
        Returns:
            A dictionary mapping PII types to lists of detected instances
        """
        results = {}
        
        for pii_type, pattern in self.compiled_patterns.items():
            matches = pattern.findall(text)
            if matches:
                # Convert all matches to strings
                string_matches = [str(match) for match in matches]
                results[pii_type] = string_matches
        
        return results
    
    def redact_pii(self, text: str) -> str:
        """
        Redact (replace with placeholders) all PII found in the text.
        
        Args:
            text: The input text containing possible PII
            
        Returns:
            The text with PII replaced by type-specific placeholders
        """
        redacted_text = text
        
        for pii_type, pattern in self.compiled_patterns.items():
            # Replace each match with a placeholder
            redacted_text = pattern.sub(f"[REDACTED {pii_type.upper()}]", redacted_text)
        
        return redacted_text
    
    def has_pii(self, text: str) -> bool:
        """
        Check if the text contains any PII.
        
        Args:
            text: The input text to check
            
        Returns:
            True if PII is found, False otherwise
        """
        for pattern in self.compiled_patterns.values():
            if pattern.search(text):
                return True
        return False


def safe_llm_call(prompt: str, model: str = "gpt-4o-mini-2024-07-18") -> Optional[str]:
    """
    Make a safe LLM call after applying PII guardrails.
    
    Args:
        prompt: The user prompt that might contain PII
        model: The LLM model to use
        
    Returns:
        The LLM response or None if blocked due to PII
    """
    # Initialize the guardrail
    guardrail = PIIGuardrail()
    
    # Check if the prompt contains PII
    if guardrail.has_pii(prompt):
        # Identify the specific PII found
        pii_found = guardrail.detect_pii(prompt)
        
        print("⚠️ PII detected in your prompt:")
        for pii_type, instances in pii_found.items():
            print(f"  - {pii_type.upper()}: {len(instances)} instance(s)")
        
        # Option 1: Block the request entirely
        print("⛔ Request blocked to protect your personal information.")
        return None
        
        # Option 2: Redact the PII and proceed (uncomment to use)
        # redacted_prompt = guardrail.redact_pii(prompt)
        # print(f"✓ PII redacted. Proceeding with modified prompt.")
        # return call_llm_with_redacted_prompt(redacted_prompt, model)
    
    # No PII detected, proceed with the original prompt
    print("✓ No PII detected. Proceeding with your request.")
    return call_llm(prompt, model)


def call_llm(prompt: str, model: str) -> str:
    """
    Call the LLM API with the given prompt.
    
    Args:
        prompt: The user prompt
        model: The LLM model to use
        
    Returns:
        The LLM response
    """
    
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def call_llm_with_redacted_prompt(redacted_prompt: str, model: str) -> str:
    """
    Call the LLM with a redacted prompt where PII has been removed.
    
    Args:
        redacted_prompt: The prompt with PII redacted
        model: The LLM model to use
        
    Returns:
        The LLM response
    """
    return call_llm(redacted_prompt, model)


# Example usage
if __name__ == "__main__":
    # Example 1: Prompt with no PII
    safe_prompt = "What are the best practices for cooking pasta?"
    result = safe_llm_call(safe_prompt)
    print(f"Result: {result}\n")
    
    # Example 2: Prompt with PII
    unsafe_prompt = "My name is John Doe and my email is john.doe@example.com. Can you help me understand my credit card bill from 1234 5678 9012 3456?"
    result = safe_llm_call(unsafe_prompt)
    print(f"Result: {result}\n")
    
    # Example 3: Test with different types of PII
    pii_test = "Please send the documents to Sarah Johnson at 123 Main St, Anytown, CA 94321 or call her at (555) 123-4567."
    guardrail = PIIGuardrail()
    detected = guardrail.detect_pii(pii_test)
    print("PII Detection Test:")
    for pii_type, instances in detected.items():
        print(f"  - {pii_type}: {instances}")
    
    redacted = guardrail.redact_pii(pii_test)
    print(f"Redacted: {redacted}") 