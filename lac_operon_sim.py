def simulate_lac_operon(lactose_present, glucose_present):
    print("\n🧬 NCERT BIO-LOGIC: THE LAC OPERON")
    print("="*40)
    
    # Logic based on NCERT:
    # 1. Glucose is the preferred carbon source.
    # 2. Lac Operon is only 'ON' when Lactose is present AND Glucose is absent.
    
    repressor_active = not lactose_present
    
    print(f"Lactose: {'✅' if lactose_present else '❌'}")
    print(f"Glucose: {'✅' if glucose_present else '❌'}")
    
    if repressor_active:
        print("\n🚫 STATUS: Repressor is BOUND to the Operator.")
        print("❌ RESULT: RNA Polymerase blocked. No Transcription.")
    else:
        print("\n🔓 STATUS: Lactose (Inducer) inactivated the Repressor.")
        if not glucose_present:
            print("🚀 RESULT: Operon is ON. z, y, a genes are producing enzymes!")
        else:
            print("⚠️ RESULT: Operon is ON, but Glucose is present. Transcription is LOW.")

if __name__ == "__main__":
    # Test Scenario: You just ate a meal with ONLY Lactose
    simulate_lac_operon(lactose_present=True, glucose_present=False)
