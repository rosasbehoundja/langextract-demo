# Langextract Demo - Text Analysis with AI

A Python project demonstrating text analysis capabilities using Google's Langextract library for sentiment analysis, emotion detection, and topic classification.

## 🚀 Features

- **Sentiment Analysis**: Determines if text sentiment is positive, negative, or neutral
- **Emotion Detection**: Identifies specific emotions like disappointment, frustration, confusion, etc.
- **Topic Classification**: Extracts and categorizes main topics from text
- **Batch Processing**: Analyze multiple texts at once
- **Structured Output**: Returns organized results as Python dictionaries

## Prerequisites

- Python 3.12 or higher
- A Langextract API key

## Installation

1. **Clone the repository** (or download the project files):
   ```bash
   git clone https://github.com/rosasbehoundja/langextract-demo
   cd langextract-demo
   ```

2. **Install dependencies using uv** (recommended):
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install langextract>=1.0.5
   ```

## API Key Setup

Before running the project, you need to set up your Langextract API key:

### Option 1: Environment Variable (Recommended)
```bash
export LANGEXTRACT_API_KEY="your_api_key_here"
```

### Option 2: Create a .env file
Create a `.env` file in the project root:
```env
LANGEXTRACT_API_KEY=your_api_key_here
```

### Option 3: Set in your shell profile
Add to your `~/.bashrc`, `~/.zshrc`, or equivalent:
```bash
export LANGEXTRACT_API_KEY="your_api_key_here"
```

### Getting an API Key
1. Visit the [Langextract github repository](https://github.com/google/langextract)
2. Sign up for an account
3. Navigate to your dashboard to generate an API key

## 🏃‍♂️ Quick Start

### Basic Usage

1. **Set your API key** (see above)

2. **Run the demo**:
   ```bash
   python main.py
   ```

3. **Expected output**:
   ```json
   {
     "text": "Good day\n My car was in an accident...",
     "sentiment": "negative",
     "emotions": ["disappointment", "frustration", "confusion"],
     "topics": ["Insurance Claims", "Customer Service", "Vehicle Maintenance"]
   }
   ```

### Custom Text Analysis

Modify the text in `main.py` or use the function programmatically:

```python
from main import main

# Analyze your own text
result = main("I love this new product! It's amazing and works perfectly.")
print(result)
```

## How It Works

The project uses a few-shot learning approach with examples to guide the AI model:

1. **Prompt Definition**: Specifies what to extract (sentiment, emotions, topics)
2. **Example Training**: Provides high-quality examples to guide the model
3. **Text Processing**: Analyzes input text using Google's Gemini 2.5 Flash model
4. **Structured Output**: Returns organized results

### Example Structure

The code demonstrates analysis of customer feedback text, extracting:
- **Sentiment**: Overall emotional tone (positive/negative/neutral)
- **Emotions**: Specific feelings (disappointment, regret, confusion, etc.)
- **Topics**: Main subjects discussed (Customer Service, Pricing, etc.)

## 🔧 Configuration

### Changing the AI Model

The project uses `gemini-2.5-flash` by default. You can modify this in `main.py`:

```python
result = lx.extract(
    text_or_documents=text,
    prompt_description=prompt,
    examples=examples,
    model_id="your-preferred-model",  # Change this
)
```

### Customizing Extractions

To modify what gets extracted, update the prompt and examples in `main.py`:

```python
prompt = textwrap.dedent("""\
    Extract sentiment and custom_category in order of appearance.
    Use exact text for extractions.""")
```

## Other Features (Commented Code)

The project includes commented code for additional features:

- **JSONL Export**: Save results to structured files
- **HTML Visualization**: Generate visual reports
- **Batch Processing**: Analyze multiple documents

Uncomment the code at the bottom of `main.py` to enable these features.

## Troubleshooting

### Common Issues

1. **API Key Error**:
   ```
   Error: API key not found
   ```
   **Solution**: Ensure `LANGEXTRACT_API_KEY` is properly set in your environment.

2. **Import Error**:
   ```
   ModuleNotFoundError: No module named 'langextract'
   ```
   **Solution**: Install dependencies with `uv sync` or `pip install langextract>=1.0.5`

3. **Rate Limit Error**:
   ```
   Error: Rate limit exceeded
   ```
   **Solution**: Wait a moment and try again, or check your API plan limits.

### Debug Tips

- Verify your API key: `echo $LANGEXTRACT_API_KEY`
- Check Python version: `python --version`
- List installed packages: `pip list | grep langextract`

## 📁 Project Structure

```
langextract-demo/
├── main.py              # Main application code
├── pyproject.toml       # Project dependencies
├── uv.lock             # Dependency lock file
└── README.md           # This file
```

## 🤝 Contributing

1. Fork the project
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request


## Next Steps

- Try analyzing different types of text (reviews, social media, emails)
- Experiment with different AI models
- Build a web interface for the analysis
- Integrate with your existing applications

---

**Happy analyzing!** 🎉
