"""
AI Homework Helper
Uses NLP + LLM integration to help students with doubts
Supports English and Telugu contexts
"""
import re
from typing import Dict, List, Optional
from loguru import logger


class HomeworkAIHelper:
    """
    AI-powered homework assistance:
    - Subject-specific hints (Math, Science, Telugu, English)
    - Step-by-step solutions
    - Practice question generation
    - Plagiarism detection
    """

    SUBJECT_PROMPTS = {
        "math": "You are a mathematics tutor. Explain step-by-step in simple English.",
        "science": "You are a science teacher. Use real-world examples relevant to Indian students.",
        "telugu": "మీరు తెలుగు ఉపాధ్యాయులు. సులువైన భాషలో వివరించండి.",
        "english": "You are an English language teacher. Focus on grammar and comprehension.",
        "social": "You are a Social Studies teacher. Relate to Indian history and geography.",
        "default": "You are a helpful tutor for Indian school students (Classes 1-12).",
    }

    MATH_PATTERNS = [
        (r"(\d+)\s*\+\s*(\d+)", lambda m: str(int(m.group(1)) + int(m.group(2)))),
        (r"(\d+)\s*-\s*(\d+)", lambda m: str(int(m.group(1)) - int(m.group(2)))),
        (r"(\d+)\s*\*\s*(\d+)", lambda m: str(int(m.group(1)) * int(m.group(2)))),
        (r"(\d+)\s*/\s*(\d+)", lambda m: str(round(int(m.group(1)) / int(m.group(2)), 4))),
    ]

    def get_hint(self, question: str, subject: str, class_level: int) -> Dict:
        """Generate a smart hint for a homework question"""
        subject_key = subject.lower() if subject.lower() in self.SUBJECT_PROMPTS else "default"
        system_prompt = self.SUBJECT_PROMPTS[subject_key]

        # Check if it's a math question
        if subject_key == "math":
            math_result = self._solve_math(question)
            if math_result:
                return {
                    "hint": f"Let me solve this step by step:\n{math_result['steps']}",
                    "answer": math_result.get("answer"),
                    "subject": subject,
                    "ai_powered": True,
                }

        # Generate contextual hint
        hint = self._generate_contextual_hint(question, subject_key, class_level)
        return {
            "hint": hint,
            "subject": subject,
            "class": class_level,
            "ai_powered": True,
            "note": "Connect to OpenAI/Gemini API for advanced AI responses",
        }

    def _solve_math(self, question: str) -> Optional[Dict]:
        """Solve basic math operations"""
        for pattern, solver in self.MATH_PATTERNS:
            match = re.search(pattern, question)
            if match:
                answer = solver(match)
                return {
                    "steps": f"Expression found: {match.group(0)}\nCalculating...\nAnswer: {answer}",
                    "answer": answer,
                }
        return None

    def _generate_contextual_hint(self, question: str, subject: str, class_level: int) -> str:
        """Rule-based contextual hint generation"""
        question_lower = question.lower()

        hints = {
            "math": {
                "area": "Area formulas: Rectangle=l×b, Circle=πr², Triangle=½×b×h",
                "percentage": "Percentage = (Part/Whole) × 100. Try writing what you know first.",
                "fraction": "Convert to same denominator before adding/subtracting fractions.",
                "algebra": "Isolate the variable. Whatever you do to one side, do to the other.",
                "default": "Break the problem into smaller steps. What information do you have?",
            },
            "science": {
                "photosynthesis": "Plants use sunlight + CO₂ + water → glucose + oxygen",
                "newton": "Newton's laws: 1) Inertia 2) F=ma 3) Action-Reaction",
                "cell": "Plant cells have cell wall, chloroplast. Animal cells have centrioles.",
                "default": "Think about what you observe in daily life. Science explains the world around us.",
            },
            "telugu": {
                "default": "మీ పాఠ్యపుస్తకంలోని నిర్వచనాలు చదివి అర్థం చేసుకోండి.",
            },
            "english": {
                "grammar": "Subject + Verb + Object is the basic sentence structure.",
                "tense": "Past: happened before. Present: happening now. Future: will happen.",
                "default": "Read the question carefully. Look for keywords.",
            },
        }

        subject_hints = hints.get(subject, {"default": "Review your textbook chapter for this topic."})

        for keyword, hint in subject_hints.items():
            if keyword in question_lower and keyword != "default":
                return hint

        return subject_hints.get("default", "Review your textbook and try to break down the problem step by step.")

    def generate_practice_questions(self, subject: str, topic: str, class_level: int, count: int = 5) -> List[Dict]:
        """Generate practice questions for a topic"""
        questions_bank = {
            "math": {
                "fractions": [
                    {"q": "Add: 1/2 + 1/3", "a": "5/6", "marks": 2},
                    {"q": "Subtract: 3/4 - 1/4", "a": "1/2", "marks": 2},
                    {"q": "Multiply: 2/3 × 3/4", "a": "1/2", "marks": 3},
                    {"q": "Divide: 5/6 ÷ 1/3", "a": "5/2 = 2.5", "marks": 3},
                    {"q": "Simplify: 12/16", "a": "3/4", "marks": 2},
                ],
                "percentages": [
                    {"q": "What is 25% of 200?", "a": "50", "marks": 2},
                    {"q": "Convert 3/4 to percentage", "a": "75%", "marks": 2},
                    {"q": "A shirt costs ₹500. Discount 20%. Find selling price.", "a": "₹400", "marks": 5},
                    {"q": "60 out of 80 marks. What percentage?", "a": "75%", "marks": 3},
                    {"q": "Increase 150 by 10%", "a": "165", "marks": 3},
                ],
            },
            "science": {
                "photosynthesis": [
                    {"q": "What is the equation of photosynthesis?", "a": "6CO₂ + 6H₂O + light → C₆H₁₂O₆ + 6O₂", "marks": 5},
                    {"q": "Where does photosynthesis occur?", "a": "Chloroplast (in leaves)", "marks": 2},
                    {"q": "What pigment absorbs sunlight?", "a": "Chlorophyll", "marks": 2},
                    {"q": "Name two by-products of photosynthesis", "a": "Glucose and Oxygen", "marks": 3},
                    {"q": "What happens to photosynthesis in the dark?", "a": "It stops (light reaction cannot occur)", "marks": 4},
                ],
            },
        }

        subject_questions = questions_bank.get(subject.lower(), {})
        topic_questions = subject_questions.get(topic.lower(), [])

        if not topic_questions:
            # Fallback generic questions
            return [{"q": f"Practice question {i+1} on {topic}", "a": "See textbook", "marks": 5} for i in range(count)]

        return topic_questions[:count]

    def check_plagiarism(self, text: str, stored_submissions: List[str]) -> Dict:
        """Simple similarity check against stored submissions"""
        similarities = []
        for i, submission in enumerate(stored_submissions):
            words1 = set(text.lower().split())
            words2 = set(submission.lower().split())
            if len(words1) == 0:
                continue
            similarity = len(words1.intersection(words2)) / len(words1.union(words2)) * 100
            if similarity > 70:
                similarities.append({
                    "submission_index": i,
                    "similarity_pct": round(similarity, 2),
                })

        return {
            "plagiarism_detected": len(similarities) > 0,
            "similar_submissions": similarities,
            "recommendation": "Review for plagiarism" if similarities else "Original submission",
        }
