"""
At-Risk Student Predictor
Uses scikit-learn to predict students likely to fail/drop out
based on attendance, grades, fee payment history
"""
import numpy as np
from typing import List, Dict
from loguru import logger

try:
    from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
    from sklearn.preprocessing import StandardScaler
    import joblib
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    logger.warning("scikit-learn not available — using rule-based fallback")


class AtRiskPredictor:
    """
    Predicts at-risk students using:
    - Attendance percentage
    - Average marks
    - Fee payment delays
    - Assignment submission rate
    - Parent engagement score
    """

    def __init__(self, model_path: str = None):
        self.model = None
        self.scaler = StandardScaler() if SKLEARN_AVAILABLE else None
        self.threshold = 0.6

        if model_path and SKLEARN_AVAILABLE:
            try:
                self.model = joblib.load(f"{model_path}/at_risk_model.pkl")
                self.scaler = joblib.load(f"{model_path}/at_risk_scaler.pkl")
                logger.info("At-risk model loaded from disk")
            except FileNotFoundError:
                logger.warning("Pre-trained model not found — will train on data")

    def _feature_vector(self, student_data: Dict) -> List[float]:
        """Extract feature vector from student data"""
        return [
            student_data.get("attendance_pct", 100),
            student_data.get("avg_marks", 75),
            student_data.get("fee_payment_delay_days", 0),
            student_data.get("assignments_submitted_pct", 100),
            student_data.get("parent_meetings_attended", 1),
            student_data.get("late_days", 0),
            student_data.get("absent_days", 0),
        ]

    def predict_risk(self, student_data: Dict) -> Dict:
        """
        Predict risk score for a single student.
        Returns: {risk_score, risk_level, risk_factors, recommendations}
        """
        features = self._feature_vector(student_data)

        if SKLEARN_AVAILABLE and self.model:
            arr = np.array([features])
            scaled = self.scaler.transform(arr)
            risk_score = float(self.model.predict_proba(scaled)[0][1])
        else:
            # Rule-based fallback
            risk_score = self._rule_based_score(student_data)

        risk_factors = self._identify_risk_factors(student_data)
        recommendations = self._generate_recommendations(risk_factors)

        return {
            "risk_score": round(risk_score, 3),
            "risk_level": "high" if risk_score > 0.7 else "medium" if risk_score > 0.4 else "low",
            "risk_factors": risk_factors,
            "recommendations": recommendations,
        }

    def _rule_based_score(self, student_data: Dict) -> float:
        """Simple rule-based scoring when ML model unavailable"""
        score = 0.0
        if student_data.get("attendance_pct", 100) < 75:
            score += 0.4
        if student_data.get("avg_marks", 100) < 40:
            score += 0.3
        if student_data.get("fee_payment_delay_days", 0) > 30:
            score += 0.15
        if student_data.get("assignments_submitted_pct", 100) < 60:
            score += 0.15
        return min(score, 1.0)

    def _identify_risk_factors(self, student_data: Dict) -> List[str]:
        factors = []
        if student_data.get("attendance_pct", 100) < 75:
            factors.append(f"Low attendance: {student_data['attendance_pct']:.1f}%")
        if student_data.get("avg_marks", 100) < 50:
            factors.append(f"Below average marks: {student_data['avg_marks']:.1f}%")
        if student_data.get("fee_payment_delay_days", 0) > 30:
            factors.append("Fee payment delay > 30 days")
        if student_data.get("assignments_submitted_pct", 100) < 60:
            factors.append("Low assignment submission rate")
        if student_data.get("absent_days", 0) > 20:
            factors.append(f"High absences: {student_data['absent_days']} days")
        return factors

    def _generate_recommendations(self, risk_factors: List[str]) -> List[str]:
        recs = []
        for factor in risk_factors:
            if "attendance" in factor.lower():
                recs.append("Schedule parent-teacher meeting to discuss attendance")
                recs.append("Enable attendance alert SMS to parents")
            if "marks" in factor.lower():
                recs.append("Enroll in remedial/extra coaching sessions")
                recs.append("Assign AI homework helper for weak subjects")
            if "fee" in factor.lower():
                recs.append("Check fee waiver/installment eligibility")
            if "assignment" in factor.lower():
                recs.append("Faculty to provide additional support and extensions")
        return list(set(recs))

    def batch_predict(self, students: List[Dict]) -> List[Dict]:
        """Predict risk for multiple students"""
        return [
            {"student_id": s.get("student_id"), **self.predict_risk(s)}
            for s in students
        ]
