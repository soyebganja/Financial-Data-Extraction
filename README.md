# Financial Data Extractor 💰

A powerful Streamlit web application that uses Large Language Models (LLM) to extract structured financial data from text paragraphs. The application intelligently identifies and extracts key financial metrics including Revenue and Earnings Per Share (EPS) with their estimated and actual values.

![Screenshot from 2025-06-27 17-04-08](https://github.com/user-attachments/assets/6c48ed62-4f4b-410b-8380-5c71f3ba22d2)

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Features

- **Intelligent Text Processing**: Uses LLM to extract financial data from unstructured text
- **Clean User Interface**: Modern, responsive Streamlit interface
- **Structured Output**: Displays results in an organized table format
- **Debug Mode**: View raw LLM responses and processed data
- **Flexible Input**: Handles various text formats and financial reporting styles
- **Real-time Processing**: Instant extraction with visual feedback

## 🚀 Demo

The application provides a simple three-step process:
1. **Input**: Enter financial text containing revenue and EPS information
2. **Extract**: Click the extract button to process with LLM
3. **Results**: View extracted data in a structured table

### Expected Output Format
| Measure | Estimated | Actual |
|---------|-----------|--------|
| Revenue | $25.37 billion | $25.18 billion |
| EPS | $1.60 | $1.64 |

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/soyebganja/Financial-Data-Extraction.git
   cd Financial-Data-Extraction
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run financial_extractor.py
   ```

5. **Access the app**
   Open your browser and navigate to `http://localhost:8501`

## 📦 Dependencies

```
streamlit>=1.28.0
pandas>=1.3.0
regex>=2022.1.18
```

## 🔧 Configuration

### LLM Integration

The application is designed to work with any LLM that returns the following JSON format:

```json
{
    "revenue_actual": "$25.18 billion",
    "revenue_expected": "$25.37 billion", 
    "eps_actual": "$1.64",
    "eps_expected": "$1.60"
}
```

To integrate your LLM:

1. Replace the `simulate_llm_response()` function in `financial_extractor.py`
2. Add your LLM API credentials to environment variables
3. Install additional dependencies for your chosen LLM provider

### Example LLM Integration

```python
def simulate_llm_response(text):
    # Replace with your actual LLM API call
    # response = openai.chat.completions.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": f"Extract financial data: {text}"}]
    # )
    # return response.choices[0].message.content
    
    # Current implementation returns mock data
    return {
        'revenue_actual': '$25.18 billion',
        'revenue_expected': '$25.37 billion',
        'eps_actual': '$1.64',
        'eps_expected': '$1.60'
    }
```

## 📝 Usage Examples

### Input Text Examples

The application can process various formats of financial text:

**Example 1: Standard Format**
```
The company reported actual revenue of $125.5 million compared to estimated revenue of $120 million. EPS was $2.45 actual versus $2.30 estimated.
```

**Example 2: News Article Style**
```
XYZ Corp exceeded revenue expectations with $5.2 billion in actual revenue against $5.0 billion expected. However, EPS fell short at $1.85 actual compared to $1.90 estimated.
```

**Example 3: Financial Report Style**
```
Q3 results: Revenue came in at $890M vs consensus of $875M. Earnings per share of $3.20 beat estimates of $3.15.
```

## 🏗️ Architecture

```
Financial Data Extractor
├── Input Layer (Streamlit UI)
├── Processing Layer (LLM Integration)
├── Data Processing (JSON to Table Conversion)
└── Output Layer (Structured Display)
```

### Key Components

- **Frontend**: Streamlit web interface
- **Backend**: Python-based text processing
- **LLM Integration**: Configurable LLM provider
- **Data Processing**: JSON parsing and validation
- **Output**: Pandas DataFrame display

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Include error handling
- Test with various input formats
- Update documentation for new features

## 📊 Supported Financial Metrics

| Metric | Description | Supported Formats |
|--------|-------------|-------------------|
| Revenue | Company total revenue | Millions, Billions, with/without $ |
| EPS | Earnings Per Share | Dollar amounts with decimals |
| Status | Estimated vs Actual | Various keywords supported |

### Supported Keywords
- **Estimated**: estimated, expected, consensus, forecast
- **Actual**: actual, reported, came in, delivered

## 🐛 Troubleshooting

### Common Issues

**Issue**: Application won't start
```bash
# Solution: Check Python version and dependencies
python --version
pip install -r requirements.txt
```

**Issue**: No data extracted
- Ensure input text contains financial keywords
- Check LLM response format in debug section
- Verify text includes both estimated and actual values

**Issue**: Incorrect extraction
- Review input text formatting
- Check debug information for LLM response
- Consider adjusting LLM prompt engineering

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the web interface
- Utilizes various LLM providers for intelligent text processing
- Inspired by the need for automated financial data analysis

## 📞 Contact

**Soyeb Ganja** - [LinkedIN Profile](https://linkedin.com/in/soyeb-ganja), [GitHub Profile](https://github.com/soyebganja)

Project Link: [https://github.com/soyebganja/Financial-Data-Extraction](https://github.com/soyebganja/Financial-Data-Extraction)

---

⭐ **Star this repository if you find it helpful!**
