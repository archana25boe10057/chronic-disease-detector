# --- 1. Knowledge Representation (The Logic Module) ---
# Define a simple knowledge base (Rules) for chronic disease diagnosis
# The keys are symptoms, values are diseases associated with a minimum number of those symptoms.

KNOWLEDGE_BASE = {
    "Diabetes": {
        "required_symptoms": ["Polyuria (frequent urination)", "Polydipsia (excessive thirst)"],
        "trigger_count": 2, # Requires at least 2 of the specific symptoms
        "risk_factors": ["High BMI", "Family History"]
    },
    "Hypertension (High BP)": {
        "required_symptoms": ["Frequent Headaches", "Dizziness", "Fatigue"],
        "trigger_count": 2,
        "risk_factors": ["Smoking", "High Sodium Intake"]
    },
    "Asthma": {
        "required_symptoms": ["Wheezing", "Shortness of Breath", "Coughing"],
        "trigger_count": 2,
        "risk_factors": ["Allergies", "Environmental Pollutants"]
    }
}

# --- 2. Data Input & Processing Module ---

def get_patient_data():
    """Simulates getting symptom data from the user."""
    print("--- Chronic Disease Symptom Checker ---")
    
    # User selects symptoms
    patient_symptoms = []
    print("\nPlease select symptoms/risk factors (type 'done' when finished):")
    
    # List of all possible symptoms/risk factors across all diseases
    all_inputs = set()
    for disease in KNOWLEDGE_BASE.values():
        all_inputs.update(disease["required_symptoms"])
        all_inputs.update(disease["risk_factors"])

    # Loop for user input
    for i, item in enumerate(sorted(list(all_inputs))):
        print(f"[{i+1}] {item}")

    user_choices = input("Enter the numbers corresponding to the symptoms you have (e.g., 1, 3, 5): ")
    
    try:
        chosen_indices = [int(i.strip()) for i in user_choices.split(',') if i.strip()]
        for index in chosen_indices:
            if 1 <= index <= len(all_inputs):
                patient_symptoms.append(sorted(list(all_inputs))[index-1])
        return patient_symptoms
    except ValueError:
        return []

# --- 3. Inference and Reporting Module ---

def diagnose(symptoms):
    """Uses the knowledge base rules to infer a diagnosis."""
    diagnosis_results = {}
    
    for disease, rules in KNOWLEDGE_BASE.items():
        matched_symptoms = 0
        for symptom in symptoms:
            # Check if the patient symptom is in either the required list or the risk list
            if symptom in rules["required_symptoms"] or symptom in rules["risk_factors"]:
                matched_symptoms += 1
        
        # Check against the trigger count
        if matched_symptoms >= rules["trigger_count"]:
            diagnosis_results[disease] = f"Potential High Risk ({matched_symptoms} matching factors found)."

    return diagnosis_results

# --- Main Execution ---

if __name__ == "__main__":
    
    # 1. Get data from the patient
    patient_inputs = get_patient_data()
    
    if not patient_inputs:
        print("\nNo valid input received. Exiting.")
    else:
        # 2. Run the logic engine
        final_diagnosis = diagnose(patient_inputs)
        
        # 3. Report the results
        print("\n" + "=" * 50)
        print("FINAL DIAGNOSTIC REPORT")
        print("=" * 50)
        print(f"Symptoms Reported: {', '.join(patient_inputs)}")
        print("-" * 50)
        
        if final_diagnosis:
            print("Potential Chronic Diseases Identified:")
            for disease, status in final_diagnosis.items():
                print(f"  - {disease}: {status}")
        else:
            print("No chronic diseases matched the rules. Consider consulting a specialist for a definitive diagnosis.")
        print("=" * 50)