"""
HR Policy Bot — Knowledge Base
12 documents covering core HR policy topics (100–500 words each).
Each document covers ONE specific topic for sharp, accurate retrieval.
"""

DOCUMENTS = [
    {
        "id": "doc_001",
        "topic": "Annual Leave and Casual Leave Policy",
        "text": (
            "Employees are entitled to 18 days of annual leave (also called earned leave or privilege leave) "
            "per calendar year. Annual leave accrues at 1.5 days per month and can be carried forward up to "
            "a maximum of 45 days into the next year. Any balance beyond 45 days lapses automatically on "
            "January 1st of the new year. "
            "Annual leave must be applied for at least 3 working days in advance through the HR portal. "
            "Approvals are at the discretion of the reporting manager and depend on team requirements. "
            "Casual leave is meant for short, unplanned absences such as personal errands or minor illness. "
            "Employees receive 8 casual leave days per year. Casual leave cannot be carried forward — any "
            "unused casual leave lapses at the end of December 31st. "
            "Casual leave can be applied on the same day if the absence is unexpected. A maximum of 3 "
            "consecutive casual leave days is permitted. For longer absences, employees must apply for "
            "annual leave or sick leave as appropriate. "
            "Leave without pay (LWP) is granted when all paid leave balances are exhausted. LWP requires "
            "manager and HR approval and affects monthly salary proportionally. "
            "Employees joining mid-year receive pro-rated leave. Those joining between the 1st and 15th of "
            "a month get credit for that month; those joining after the 15th do not."
        ),
    },
    {
        "id": "doc_002",
        "topic": "Sick Leave and Medical Leave Policy",
        "text": (
            "Employees are entitled to 12 days of sick leave per calendar year. Sick leave is intended "
            "solely for personal illness, injury, or medical procedures and cannot be used for any other purpose. "
            "Sick leave up to 2 consecutive days does not require a medical certificate. For absences of "
            "3 or more consecutive days, employees must submit a medical certificate from a registered "
            "medical practitioner within 48 hours of returning to work. "
            "Sick leave does not carry forward and lapses on December 31st. It cannot be encashed. "
            "Employees undergoing a planned medical procedure (surgery, hospitalisation) should inform HR "
            "and their manager as early as possible. In such cases, up to 30 days of extended sick leave "
            "may be considered by HR on a case-by-case basis, subject to medical documentation. "
            "Maternity leave is separate from sick leave and is governed by the Maternity Benefits Policy. "
            "If an employee exhausts all sick leave and requires further time off for medical reasons, "
            "annual leave will be used next; after that, leave without pay applies. "
            "The company covers medical insurance for all full-time employees and their dependents under "
            "the Group Health Insurance Policy, with a sum insured of Rs. 5,00,000 per family per year."
        ),
    },
    {
        "id": "doc_003",
        "topic": "Maternity and Paternity Leave",
        "text": (
            "Maternity Leave: Female employees with at least 80 days of service in the 12 months preceding "
            "the expected date of delivery are entitled to 26 weeks of fully paid maternity leave under the "
            "Maternity Benefit (Amendment) Act, 2017. "
            "For a third child onwards, maternity leave is 12 weeks. "
            "In the case of adoption of a child below 3 months of age, the adoptive mother is entitled to "
            "12 weeks of maternity leave. "
            "Maternity leave can start up to 8 weeks before the expected delivery date. Employees must "
            "submit a medical certificate indicating the expected date of delivery at least 6 weeks in advance. "
            "During maternity leave, the employee's salary and benefits continue unchanged. "
            "A crèche facility is available at offices with 50 or more employees. New mothers are permitted "
            "4 visits to the crèche per working day during the first year after returning from maternity leave. "
            "Paternity Leave: Male employees and same-sex partners of a birthing parent are entitled to "
            "5 days of paid paternity leave, to be availed within 6 months of the child's birth or adoption. "
            "Paternity leave can be combined with annual leave for a longer period. "
            "Miscarriage or medical termination of pregnancy: the employee is entitled to 6 weeks of paid "
            "leave with a medical certificate."
        ),
    },
    {
        "id": "doc_004",
        "topic": "Work From Home and Hybrid Work Policy",
        "text": (
            "The company follows a hybrid work model. Employees in non-field roles are required to work "
            "from the office a minimum of 3 days per week (typically Tuesday, Wednesday, and Thursday). "
            "Monday and Friday may be work-from-home days subject to manager approval and role requirements. "
            "Work from home is a privilege, not a right. It can be temporarily withdrawn by a manager if "
            "business or team needs require full in-office presence. "
            "To be eligible for WFH, employees must: have completed their probation period, maintain a "
            "dedicated and distraction-free workspace at home, have reliable internet (minimum 20 Mbps), "
            "and be reachable on all company communication tools during core hours (10 AM – 6 PM IST). "
            "Employees on WFH days must be available for video calls and must not be caring for a child or "
            "dependent without other childcare arrangements in place. If childcare is the reason for WFH, "
            "casual leave or annual leave should be applied for instead. "
            "For extended WFH beyond the policy (e.g., relocating to a different city temporarily), written "
            "approval from the department head and HR is required for stays beyond 30 days. "
            "International remote work is not permitted without prior approval from HR and Legal, as it may "
            "trigger tax and compliance obligations in the foreign jurisdiction."
        ),
    },
    {
        "id": "doc_005",
        "topic": "Salary Structure, Payroll, and Payslip",
        "text": (
            "Salaries are processed on the last working day of every month. The salary is credited directly "
            "to the bank account registered with HR. Employees must ensure their bank details on the HR "
            "portal are current; any incorrect bank details causing a failed transfer are the employee's "
            "responsibility to rectify before the 20th of the month. "
            "The salary structure consists of: Basic Pay (40% of CTC), House Rent Allowance — HRA (50% of "
            "Basic for metro cities, 40% for non-metro), Special Allowance (the balance component), and "
            "performance-based variable pay paid quarterly. "
            "Provident Fund (PF): 12% of Basic Pay is deducted from the employee's salary and an equal "
            "12% is contributed by the employer, both credited to the EPF account. "
            "Professional Tax is deducted as per the applicable state slab. "
            "TDS (Tax Deducted at Source) is deducted monthly based on the employee's projected annual "
            "income and the investment declarations submitted in April. Employees should submit Form 12BB "
            "with supporting documents by April 15th to avoid excess TDS deductions. "
            "Payslips are generated by the 3rd of the following month and are accessible on the HR portal "
            "under the 'Payroll' section. For any salary discrepancy, employees must raise a ticket on the "
            "HR helpdesk within 15 days of the payslip being generated."
        ),
    },
    {
        "id": "doc_006",
        "topic": "Performance Appraisal and Increment Policy",
        "text": (
            "The company follows an annual performance review cycle. The appraisal year runs from April 1st "
            "to March 31st. "
            "Goal-setting happens in April each year. Employees must set 4–6 SMART goals in collaboration "
            "with their managers on the HR portal by April 30th. Mid-year check-ins take place in October. "
            "The final appraisal discussion is held in March. "
            "Performance ratings are on a 5-point scale: 5 – Outstanding, 4 – Exceeds Expectations, "
            "3 – Meets Expectations, 2 – Needs Improvement, 1 – Unsatisfactory. "
            "Salary increments are effective from April 1st and are communicated by March 31st. "
            "The increment percentage is linked to the performance rating and the company's overall business "
            "performance that year. Indicative increments: Rating 5 → 20–25%, Rating 4 → 12–18%, "
            "Rating 3 → 6–10%, Rating 2 → 0–4%, Rating 1 → 0% (PIP initiated). "
            "Employees who join between October and March are not eligible for an increment in the "
            "immediately following April cycle; they are eligible from the next cycle. "
            "A Performance Improvement Plan (PIP) is a structured 60–90 day plan for employees rated 1 or 2. "
            "HR and the manager jointly draft the PIP. Successful completion clears the rating; "
            "failure to meet PIP targets may result in termination."
        ),
    },
    {
        "id": "doc_007",
        "topic": "Code of Conduct and Workplace Ethics",
        "text": (
            "All employees are expected to maintain the highest standards of professional conduct at all times. "
            "Core principles include integrity, respect, accountability, transparency, and confidentiality. "
            "Conflicts of interest must be disclosed to HR and the reporting manager immediately. Examples "
            "include: holding a financial interest in a competitor, having a close relative as a direct report, "
            "or receiving gifts above Rs. 1,000 from vendors or clients. "
            "Employees must not share confidential company information — including client data, financial "
            "results, product roadmaps, or salary information — with any external party or on social media. "
            "Any breach of data confidentiality is treated as gross misconduct and can result in immediate termination. "
            "Use of company assets (laptops, software licenses, internet) for personal commercial activities "
            "is prohibited. Incidental personal use of the internet is permitted within reasonable limits. "
            "Discrimination, harassment, or bullying of any kind — based on gender, caste, religion, "
            "nationality, disability, sexual orientation, or age — is a zero-tolerance violation. "
            "Any such complaint must be reported to the Internal Complaints Committee (ICC) or HR. "
            "Violations are investigated under the company's POSH Policy (Prevention of Sexual Harassment). "
            "Substance abuse on company premises or during company events is strictly prohibited and is "
            "grounds for immediate termination."
        ),
    },
    {
        "id": "doc_008",
        "topic": "Resignation, Notice Period, and Full and Final Settlement",
        "text": (
            "Resignation must be submitted in writing (email to the reporting manager and HR is acceptable). "
            "The notice period is 60 days for all employees who have completed their probation period. "
            "Employees in senior roles (Manager and above) serve a 90-day notice period. "
            "During probation (first 3 months), the notice period is 30 days. "
            "Notice period buyout: if the employee cannot serve the full notice period, they may pay the "
            "company an amount equivalent to the shortfall in days' salary (Basic + DA component). "
            "Similarly, the company may request early release of the employee, in which case salary for "
            "the remaining notice period is paid out. "
            "Handover of duties, return of company assets (laptop, access card, SIM), and completion of "
            "the exit clearance checklist on the HR portal are mandatory before the last working day. "
            "Full and Final (F&F) Settlement: all dues — including pending salary, leave encashment "
            "(for earned leave balance), and reimbursements — are processed within 45 working days of the "
            "last working day. "
            "Leave encashment at separation: only unused annual (earned) leave is encashed at the time of "
            "F&F. Casual leave and sick leave are not encashed. "
            "The relieving letter and experience certificate are issued after the F&F is cleared and all "
            "clearances are obtained."
        ),
    },
    {
        "id": "doc_009",
        "topic": "Reimbursements: Travel, Food, and Business Expenses",
        "text": (
            "Employees incurring business expenses are reimbursed as per the approved expense policy. "
            "All reimbursement claims must be submitted on the HR/Finance portal within 30 days of incurring "
            "the expense, along with original receipts or e-invoices. Claims submitted beyond 30 days will "
            "not be processed. "
            "Travel reimbursement: for outstation travel, flight bookings must be done through the company's "
            "travel desk (or approved travel portal) at least 7 days in advance for economy class. "
            "Hotel stay is reimbursed up to Rs. 4,000/night for Tier-1 cities (Mumbai, Delhi, Bangalore, "
            "Hyderabad, Chennai, Pune) and Rs. 2,500/night for other cities. "
            "Local conveyance (taxi/auto) is reimbursed at actuals with receipts. Personal vehicle use for "
            "official travel is reimbursed at Rs. 6/km for two-wheelers and Rs. 10/km for four-wheelers. "
            "Meal allowance during outstation travel: Rs. 500/day for Tier-1, Rs. 350/day for others. "
            "Internet reimbursement for WFH: Rs. 500/month flat reimbursable against a bill, applicable "
            "to employees in confirmed WFH roles or those approved for hybrid work. "
            "Mobile phone bill reimbursement: employees in client-facing or field roles are eligible for "
            "up to Rs. 1,000/month against original bill. Others are not eligible unless specifically stated "
            "in their offer letter."
        ),
    },
    {
        "id": "doc_010",
        "topic": "Onboarding, Probation, and Confirmation",
        "text": (
            "New employees begin their tenure with a 3-month probation period. The probation period may "
            "be extended by up to 3 additional months if performance is below expectations. "
            "During probation, the notice period is 30 days on either side. Benefits such as annual leave "
            "accrue during probation but cannot be availed until confirmation, except in genuine emergencies "
            "with manager approval. "
            "Onboarding week: the first week consists of company orientation, IT setup, compliance training "
            "(POSH, data security, code of conduct), and team introductions. Attendance is mandatory. "
            "Employees must complete all mandatory compliance modules on the LMS (Learning Management System) "
            "within 15 days of joining. Failure to do so may delay confirmation. "
            "The confirmation process: the manager submits a probation review form on the HR portal by "
            "the end of the 3rd month. HR processes the confirmation letter and the employee's status "
            "changes from 'Probation' to 'Permanent' in the system. "
            "Post-confirmation, the employee gets access to all full benefits: health insurance for "
            "dependents, higher leave balances, and eligibility for the annual increment cycle. "
            "Background verification is initiated on day 1 and covers: educational qualification check, "
            "previous employment verification (last 2 employers), and criminal record check. "
            "Discrepancies in the background check may result in offer withdrawal or termination."
        ),
    },
    {
        "id": "doc_011",
        "topic": "Training, Learning, and Development Policy",
        "text": (
            "The company is committed to continuous learning. Every employee has an annual Learning & "
            "Development (L&D) budget of Rs. 15,000 for external courses, certifications, or conferences. "
            "The L&D budget must be approved by the manager and HR before the expense is incurred. "
            "Reimbursement requires a completion certificate or proof of attendance. "
            "The internal LMS hosts mandatory compliance courses and optional skill-building modules. "
            "Employees are encouraged to complete at least 40 learning hours annually, tracked on the LMS. "
            "Sponsored certifications: for high-value certifications above Rs. 15,000 (e.g., AWS, PMP, CFA), "
            "the company may fully sponsor the cost under a bond: the employee must remain with the company "
            "for at least 1 year after completing the certification. If the employee leaves before that, "
            "a pro-rated amount is recovered in the F&F settlement. "
            "Internal mobility: after completing 18 months in a role, employees can apply for open internal "
            "positions. The hiring manager must inform current manager before extending an offer. "
            "Mentorship programme: a structured 6-month pairing of junior employees with senior leaders. "
            "Applications open in January each year. "
            "Leadership development programme: high-performers (Rating 4 or 5) are nominated by managers "
            "for the annual leadership cohort. This includes 3 offsite workshops, a live business project, "
            "and executive coaching."
        ),
    },
    {
        "id": "doc_012",
        "topic": "Grievance Redressal and HR Helpdesk",
        "text": (
            "Every employee has the right to raise a grievance without fear of retaliation. "
            "The grievance process has 3 levels. Level 1: the employee discusses the issue directly with "
            "their reporting manager. This should be the first step for most workplace concerns. "
            "Level 2: if unresolved within 7 working days, the employee escalates to the HR Business Partner "
            "(HRBP) assigned to their department. The HRBP will acknowledge within 2 working days and "
            "resolve within 15 working days. "
            "Level 3: if still unresolved, the employee can escalate to the Head of HR. The Head of HR's "
            "decision is final for all HR-related matters. "
            "The HR Helpdesk is available on the intranet portal and handles queries related to: payslips, "
            "leave balances, reimbursement status, policy clarifications, and IT access requests. "
            "Helpdesk SLA: queries are acknowledged within 1 business day and resolved within 5 business days. "
            "Complaints related to harassment, discrimination, or misconduct bypass the grievance levels "
            "and go directly to the Internal Complaints Committee (ICC). The ICC is a statutory body under "
            "the POSH Act and operates independently of the HR chain of command. "
            "Anonymous feedback can be submitted via the anonymous feedback form on the intranet. While "
            "anonymous submissions limit follow-up, HR reviews all feedback and takes systemic action "
            "where patterns are identified. "
            "Whistleblower protection: employees reporting policy violations or unethical conduct in good "
            "faith are protected from retaliation under the company's Whistleblower Policy."
        ),
    },
]
