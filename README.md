## 7. Design Decision Log

### D1. Where does the two-hour rule live?
The two-hour cancellation rule belongs in the Appointment class because it controls appointment status transitions. We considered placing it in Clinic, but this would mix appointment-specific rules with clinic management responsibilities.

### D2. Why is the Clock design testable?
The system uses an injected Clock object with a now() method instead of reading the computer's system time directly. This allows tests to control time and simulate different cancellation scenarios.

### D3. What changed when Pharmacist was added?
We created Pharmacist as a subclass of Staff and implemented its role() and fee() methods. The existing polymorphic fee loop did not need modification. This demonstrates extensibility.

### D4. MedicalLecturer fee and inheritance
MedicalLecturer uses the Doctor fee calculation. For patient ID 77, the fee is 40 + 5 × (77 mod 5) = 50. Python multiple inheritance allows MedicalLecturer to inherit from Doctor and Lecturer. Since Lecturer does not inherit from Person, the Person constructor runs only once.

### D5. What happens if writing to or closing the log fails?
Logging failures should be handled as errors rather than silently ignored. The application should preserve the original operation error where possible and ensure resources are closed safely.

### D6. Design decisions for the twist
- The Clinic owns the waiting list because it manages appointments and available slots.
- Confirmed appointments cannot be bumped because they have already been accepted.
- Staff buffer hours are obtained through the staff object's gap_hours property rather than type checks.
- Patient discounts are determined by the patient's type through the discount_rate() method.

---

