# AI Training Requirements

## Datasets
- **Face Recognition**: Minimum 5 high-quality images per student (Front, Left-45, Right-45).
- **Academic Chatbot**: JSON format `{"instruction": "...", "context": "...", "response": "..."}`.
- **Analytics**: CSV export from Attendance and Exam modules.

## Resource Requirements
- **GPU**: NVIDIA T4 or better recommended for Face/NLP training.
- **Memory**: 16GB+ RAM.
- **Storage**: SSD with 50GB available for dataset caching.

## Execution
Run all training from the root of the `ai-services/training/scripts` folder using:
`python3 script_name.py`
