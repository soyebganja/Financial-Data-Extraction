import streamlit as st
import pandas as pd
import re

from dataExtracter import extract

def simulate_llm_response(text):
    """
    Simulate LLM response - in real implementation, this would call your LLM
    Returns the expected JSON format
    """
    # This is a placeholder - replace with actual LLM API call
    # For demonstration, using regex extraction similar to before
    text_lower = text.lower()
    
    # Initialize response format
    llm_response = {
        'revenue_actual': None,
        'revenue_expected': None,
        'eps_actual': None,
        'eps_expected': None
    }
    
    # Revenue patterns
    revenue_actual_patterns = [
        r'revenue.*?actual.*?(\$[\d,]+\.?\d*\s*(?:billion|million|b|m)?)',
        r'actual.*?revenue.*?(\$[\d,]+\.?\d*\s*(?:billion|million|b|m)?)',
        r'revenue.*?reported.*?(\$[\d,]+\.?\d*\s*(?:billion|million|b|m)?)',
        r'reported.*?revenue.*?(\$[\d,]+\.?\d*\s*(?:billion|million|b|m)?)'
    ]
    
    revenue_expected_patterns = [
        r'revenue.*?estimated.*?(\$[\d,]+\.?\d*\s*(?:billion|million|b|m)?)',
        r'revenue.*?expected.*?(\$[\d,]+\.?\d*\s*(?:billion|million|b|m)?)',
        r'estimated.*?revenue.*?(\$[\d,]+\.?\d*\s*(?:billion|million|b|m)?)',
        r'expected.*?revenue.*?(\$[\d,]+\.?\d*\s*(?:billion|million|b|m)?)'
    ]
    
    eps_actual_patterns = [
        r'eps.*?actual.*?(\$[\d,]+\.?\d*)',
        r'actual.*?eps.*?(\$[\d,]+\.?\d*)',
        r'eps.*?reported.*?(\$[\d,]+\.?\d*)',
        r'reported.*?eps.*?(\$[\d,]+\.?\d*)'
    ]
    
    eps_expected_patterns = [
        r'eps.*?estimated.*?(\$[\d,]+\.?\d*)',
        r'eps.*?expected.*?(\$[\d,]+\.?\d*)',
        r'estimated.*?eps.*?(\$[\d,]+\.?\d*)',
        r'expected.*?eps.*?(\$[\d,]+\.?\d*)'
    ]
    
    # Extract values
    for pattern in revenue_actual_patterns:
        matches = re.findall(pattern, text_lower)
        if matches:
            llm_response['revenue_actual'] = matches[0].strip()
            break
    
    for pattern in revenue_expected_patterns:
        matches = re.findall(pattern, text_lower)
        if matches:
            llm_response['revenue_expected'] = matches[0].strip()
            break
    
    for pattern in eps_actual_patterns:
        matches = re.findall(pattern, text_lower)
        if matches:
            llm_response['eps_actual'] = matches[0].strip()
            break
    
    for pattern in eps_expected_patterns:
        matches = re.findall(pattern, text_lower)
        if matches:
            llm_response['eps_expected'] = matches[0].strip()
            break
    
    return llm_response

def process_llm_response(llm_response):
    """
    Convert LLM response format to display format
    """
    results = {
        'Revenue': {
            'Estimated': llm_response.get('revenue_expected', 'N/A') or 'N/A',
            'Actual': llm_response.get('revenue_actual', 'N/A') or 'N/A'
        },
        'EPS': {
            'Estimated': llm_response.get('eps_expected', 'N/A') or 'N/A',
            'Actual': llm_response.get('eps_actual', 'N/A') or 'N/A'
        }
    }
    return results

def main():
    # Page configuration
    st.set_page_config(
        page_title="Financial Data Extractor",
        page_icon="💰",
        layout="wide"
    )
    
    # Title
    st.title("💰 Financial Data Extractor")
    st.markdown("---")
    
    # Input section
    st.subheader("📝 Input Financial Text")
    input_text = st.text_area(
        "Enter a paragraph containing financial information (Revenue and EPS data):",
        placeholder="Example: The company reported actual revenue of $125.5 million compared to estimated revenue of $120 million. EPS was $2.45 actual versus $2.30 estimated.",
        height=150
    )
    
    # Extract button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        extract_button = st.button("🔍 Extract", type="primary", use_container_width=True)
    
    # Results section
    if extract_button:
        if input_text.strip():
            st.markdown("---")
            st.subheader("📊 Extracted Financial Data")
            
            # Simulate LLM call and get response
            with st.spinner("🤖 Processing with LLM..."):
                # llm_response = simulate_llm_response(input_text)
                llm_response = extract(input_text)
            
            # Process LLM response for display
            extracted_data = process_llm_response(llm_response)
            
            # Create DataFrame for display
            df_data = []
            for measure in ['Revenue', 'EPS']:
                df_data.append({
                    'Measure': measure,
                    'Estimated': extracted_data[measure]['Estimated'],
                    'Actual': extracted_data[measure]['Actual']
                })
            
            df = pd.DataFrame(df_data)
            
            # Display table
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Measure": st.column_config.TextColumn(
                        "Measure",
                        width="small",
                    ),
                    "Estimated": st.column_config.TextColumn(
                        "Estimated",
                        width="medium",
                    ),
                    "Actual": st.column_config.TextColumn(
                        "Actual",
                        width="medium",
                    ),
                }
            )
            
            # Show LLM response and processed data for debugging
            with st.expander("🔍 Debug Information"):
                st.subheader("LLM Response:")
                st.json(llm_response)
                st.subheader("Processed Data:")
                st.json(extracted_data)
                
        else:
            st.warning("⚠️ Please enter some text to extract financial data.")
    
    # Instructions
    st.markdown("---")
    st.subheader("📋 Instructions")
    st.markdown("""
    **How to use:**
    1. Enter a paragraph containing financial information in the text area above
    2. The text should include Revenue and/or EPS (Earnings Per Share) data
    3. Include keywords like 'estimated', 'expected', 'actual', or 'reported' for better extraction
    4. Click the 'Extract' button to process the text with LLM
    5. View the extracted data in the table below
    
    **Expected LLM Response Format:**
    ```json
    {
        'revenue_actual': '$25.18 billion',
        'revenue_expected': '$25.37 billion', 
        'eps_actual': '$1.64',
        'eps_expected': '$1.60'
    }
    ```
    
    **Example text formats:**
    - "Revenue was $150M actual vs $145M estimated"
    - "The company reported EPS of $1.25 compared to expected EPS of $1.20"
    - "Actual revenue came in at $2.5 billion while estimated revenue was $2.3 billion. EPS actual was $3.45 versus EPS estimated of $3.30"
    """)
    # **Note:** The current implementation uses a simulated LLM response. Replace the `simulate_llm_response()` function with your actual LLM API call.    

if __name__ == "__main__":
    main()