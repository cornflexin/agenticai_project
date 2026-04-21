"""
HR Policy Bot — Knowledge Base (v2 — expanded for richer context)
12 documents, each much more detailed so the bot can give complete,
specific answers without sounding vague.
"""

DOCUMENTS = [
    {
        "id": "doc_001",
        "topic": "Annual Leave and Casual Leave Policy",
        "text": (
            "Annual Leave (also called Earned Leave or Privilege Leave): "
            "Every confirmed employee gets 18 days of annual leave per calendar year. "
            "This accrues at 1.5 days per month — so if you've worked for 4 months you've earned 6 days. "
            "You can carry forward unused annual leave, but only up to a maximum of 45 days total. "
            "Anything above 45 days is automatically cancelled on January 1st — it does not get paid out, it just disappears. "
            "To apply for annual leave, you must submit a request on the HR portal at least 3 working days before the leave starts. "
            "Your manager approves or rejects it based on team workload. During busy project periods, managers can defer leave. "
            "There is no minimum or maximum number of annual leave days you must take in a year, but HR recommends taking at least 10 days for wellbeing. "
            "If you resign or are terminated, your remaining annual leave balance is encashed in the Full and Final settlement at your basic daily rate. "
            "Employees who join between the 1st and 15th of a month get leave credit for that month. Those joining after the 15th don't get credit for that month. "
            "Annual leave can be clubbed with public holidays and weekends to extend your time off. "
            "Casual Leave: "
            "You get 8 casual leave days per year for unplanned, short absences — things like a family emergency, personal errand, or feeling slightly unwell. "
            "Casual leave cannot be carried forward at all. Whatever you haven't used by December 31st is gone — it does not get paid out either. "
            "You can apply for casual leave on the same day, even after the fact, if the absence was truly unplanned. "
            "You cannot take more than 3 consecutive days of casual leave. If you need more than 3 days off in a row, you must apply for annual leave or sick leave instead. "
            "Casual leave cannot be combined with annual leave in the same application. "
            "Leave Without Pay (LWP): If you have exhausted both annual and casual leave, you can apply for LWP. "
            "LWP requires approval from both your manager and HR. Your salary is reduced proportionally — for each LWP day, one day's salary (basic + DA) is deducted. "
            "Summary of leave entitlements per year: Annual Leave = 18 days (carry forward up to 45), Casual Leave = 8 days (no carry forward), Sick Leave = 12 days (see sick leave policy), plus all national and regional public holidays."
        ),
    },
    {
        "id": "doc_002",
        "topic": "Sick Leave and Medical Leave Policy",
        "text": (
            "Sick Leave Entitlement: Every employee gets 12 days of sick leave per calendar year. "
            "Sick leave is strictly for personal illness, injury, surgery, or medical procedures. You cannot use it for anything else. "
            "Sick leave does NOT carry forward to the next year — unused sick leave lapses on December 31st. It also cannot be encashed when you resign. "
            "Medical Certificate Rules: For sick leave of 1 or 2 consecutive days, no medical certificate is required. You just apply on the portal and inform your manager. "
            "For 3 or more consecutive days of sick leave, you must submit a medical certificate from a registered doctor. The certificate must be submitted within 48 hours of your return to work. "
            "If you do not submit the certificate on time, those days may be converted to Leave Without Pay. "
            "Extended Medical Leave: If you need more than 12 sick days due to a serious illness, surgery, or hospitalisation, HR can approve up to 30 additional days of extended medical leave on a case-by-case basis. "
            "This requires detailed medical documentation — hospital discharge summary, doctor's recommendation for rest, etc. "
            "What Happens When Sick Leave Runs Out: Once your 12 sick days are used up, any further sick absence will first use your annual leave balance, then casual leave, and finally leave without pay. "
            "Group Health Insurance: The company provides group health insurance to all full-time confirmed employees. The cover is Rs. 5,00,000 per family per year. "
            "This covers the employee, their spouse, up to 2 dependent children, and dependent parents. "
            "Maternity-related medical leave is covered under the separate Maternity Leave policy, not this sick leave policy. "
            "Mental health leave: The company treats mental health conditions the same as physical illness. If you need time off for therapy, psychiatric treatment, or a mental health crisis, sick leave applies. "
            "You are not required to specify the exact mental health condition on the leave form — 'medical reasons' is sufficient."
        ),
    },
    {
        "id": "doc_003",
        "topic": "Maternity and Paternity Leave",
        "text": (
            "Maternity Leave: Female employees are entitled to 26 weeks (roughly 6 months) of fully paid maternity leave. "
            "This is governed by the Maternity Benefit (Amendment) Act, 2017 and applies to employees who have worked at the company for at least 80 days in the 12 months before their due date. "
            "The 26 weeks can start up to 8 weeks before the expected delivery date, meaning you can take 8 weeks before birth and 18 weeks after, or any split that totals 26 weeks. "
            "For a third child or beyond, maternity leave is reduced to 12 weeks. "
            "Adoptive mothers who adopt a child below 3 months of age get 12 weeks of maternity leave. "
            "What you need to do: Submit a maternity leave application at least 6 weeks before your expected leave start date, along with a medical certificate from your doctor showing the expected delivery date. "
            "During maternity leave, your full salary, PF contributions, and all benefits continue unchanged. "
            "Creche facility: If your office has 50 or more employees, a creche is available. After returning from maternity leave, you are allowed 4 creche visits per working day during the child's first year. "
            "Miscarriage or medical termination of pregnancy: You are entitled to 6 weeks of fully paid leave. A medical certificate is required. "
            "Paternity Leave: Male employees and same-sex partners of a birthing parent get 5 days of fully paid paternity leave. "
            "These 5 days must be availed within 6 months of the child's birth or adoption. "
            "Paternity leave can be combined with casual leave or annual leave if you need a longer break. "
            "Adoption leave for primary caregiver fathers: If you are the primary caregiver in an adoption, speak to HR — extended leave options may be considered on a case-by-case basis."
        ),
    },
    {
        "id": "doc_004",
        "topic": "Work From Home and Hybrid Work Policy",
        "text": (
            "The company follows a hybrid work model. Here is exactly how it works: "
            "Mandatory office days: You must be physically present in the office on Tuesday, Wednesday, and Thursday every week. These are non-negotiable unless you have approved leave. "
            "WFH days: Monday and Friday are work-from-home days by default, but this is subject to your manager's approval and your role requirements. Some roles (client-facing, lab, or operations) may require full in-office presence. "
            "WFH is a privilege, not a right. If your team has a critical deadline, client visit, or important meeting, your manager can require you to come in on a Monday or Friday. "
            "Eligibility for WFH: You must have completed your probation period (3 months). Employees still on probation are expected to come to the office all 5 days unless an exception is approved by HR. "
            "WFH requirements: You need a dedicated, distraction-free workspace at home. You must have reliable internet of at least 20 Mbps. You must be available on company communication tools within 15 minutes during core hours (10 AM to 6 PM IST). You must be ready for video calls with camera on when requested. "
            "WFH does NOT mean you can be caregiving at the same time. If you are home to look after a sick child or an elderly parent, you should apply for casual leave instead. "
            "Extended WFH or relocation: If you want to work remotely from a different city for more than 30 days, you need written approval from your department head AND HR. "
            "International remote work: Working remotely from another country is not permitted without prior approval from HR and Legal. It creates tax and compliance obligations in that country. "
            "Violations: Repeatedly being unavailable during WFH hours, attending personal appointments while marked as WFH, or ignoring WFH requirements can result in your WFH privilege being withdrawn. "
            "Internet reimbursement for WFH: Rs. 500 per month against your internet bill, applicable to employees in confirmed WFH or hybrid roles."
        ),
    },
    {
        "id": "doc_005",
        "topic": "Salary Structure, Payroll, and Payslip",
        "text": (
            "When is salary paid: Salary is credited to your bank account on the last working day of every month. "
            "If the last day is a public holiday or weekend, it is credited on the previous working day. "
            "How salary is structured: "
            "1. Basic Pay is 40% of your total CTC. This is the most important component because PF, gratuity, and leave encashment are all calculated on Basic Pay. "
            "2. House Rent Allowance (HRA) is 50% of Basic Pay if you are in a metro city (Mumbai, Delhi, Bangalore, Hyderabad, Chennai, Pune, Kolkata) and 40% of Basic Pay for non-metro cities. HRA is partially tax-exempt if you pay rent and submit rent receipts. "
            "3. Special Allowance is the balance amount after Basic and HRA. It is fully taxable. "
            "4. Variable Pay is a performance-linked component paid quarterly. The amount depends on your performance rating and company results. It is NOT guaranteed every quarter. "
            "Example: If your CTC is Rs. 10 LPA — Basic = Rs. 4 LPA, HRA (metro) = Rs. 2 LPA, Special Allowance = Rs. 4 LPA, Variable is separate and performance-linked. "
            "Deductions: PF — 12% of your Basic Pay is deducted monthly and the company also contributes 12%, both going into your EPF account. "
            "Professional Tax is deducted as per your state's slab (e.g. Rs. 200/month in Karnataka). "
            "TDS is deducted monthly based on your projected annual income. To reduce TDS, submit your investment declarations (Form 12BB) in April with supporting documents. "
            "Payslip: Generated by the 3rd of the following month and available on the HR portal under the Payroll section. "
            "Salary discrepancy: If your salary is wrong, raise a helpdesk ticket within 15 days of the payslip being generated. Corrections are processed in the next payroll cycle. "
            "Bank account: Ensure your bank details on the HR portal are correct before the 20th of each month."
        ),
    },
    {
        "id": "doc_006",
        "topic": "Performance Appraisal and Increment Policy",
        "text": (
            "Appraisal cycle: The performance year runs from April 1st to March 31st. "
            "Goal setting: In April, you and your manager set 4 to 6 SMART goals on the HR portal by April 30th. "
            "Mid-year review: In October, you have a progress check-in with your manager. "
            "Final appraisal: In March, you submit a self-assessment and have a formal discussion with your manager. "
            "Performance ratings on a 5-point scale: "
            "Rating 5 Outstanding means you consistently exceeded all goals and had significant impact beyond your role. "
            "Rating 4 Exceeds Expectations means you exceeded most goals with strong performance. "
            "Rating 3 Meets Expectations means you met all your goals consistently. "
            "Rating 2 Needs Improvement means you partially met goals and have clear gaps. "
            "Rating 1 Unsatisfactory means you failed to meet most goals. "
            "Salary increments effective from April 1st: "
            "Rating 5 gets 20% to 25% increment. "
            "Rating 4 gets 12% to 18% increment. "
            "Rating 3 gets 6% to 10% increment. "
            "Rating 2 gets 0% to 4% increment. "
            "Rating 1 gets 0% increment and a Performance Improvement Plan is initiated. "
            "These ranges also depend on the company's overall financial performance. "
            "New joiners who joined between October and March are not eligible for the upcoming April increment cycle. "
            "Performance Improvement Plan (PIP): If rated 1 or 2, a 60 to 90 day structured plan is created with your manager and HR. Meeting PIP targets closes the plan; failing may lead to termination. "
            "Promotions: Linked to the appraisal cycle but not guaranteed annually. Requires a role opening at the next level and endorsement from manager and skip-level manager."
        ),
    },
    {
        "id": "doc_007",
        "topic": "Code of Conduct and Workplace Ethics",
        "text": (
            "Core values every employee must uphold: integrity, respect, accountability, transparency, and confidentiality. "
            "Conflicts of interest must be disclosed to HR and your manager. Examples include: having a financial stake in a competitor, a close relative reporting to you directly, or receiving gifts above Rs. 1,000 from vendors or clients. Not disclosing a conflict is itself misconduct. "
            "Confidentiality: Never share company information externally without authorisation. This includes client data, financial numbers, product plans, and pricing. "
            "Discussing your own salary with colleagues is allowed. Accessing another employee's salary data from systems without authorisation is a violation. "
            "Data security: All company data must stay on approved systems. Using personal Google Drive, WhatsApp, or USB drives to store company data is prohibited. "
            "Social media: Do not post confidential company information online. Personal opinions are fine as long as you are clearly not speaking on behalf of the company. "
            "Use of company assets: Laptops, software, and internet are for professional use. Reasonable personal use during breaks is fine. Running a personal business on company equipment is not. "
            "Harassment and discrimination: Zero tolerance for any harassment or discrimination based on gender, religion, caste, nationality, age, disability, or sexual orientation. "
            "Complaints go directly to the Internal Complaints Committee (ICC) or HR. The ICC operates independently under the POSH Act. Retaliation against anyone who files a complaint is a serious violation in itself. "
            "Substance abuse: Being under the influence of alcohol or drugs on company premises or at company events is grounds for immediate termination. "
            "Violations of the code of conduct can result in written warnings, suspension without pay, or termination depending on the severity."
        ),
    },
    {
        "id": "doc_008",
        "topic": "Resignation, Notice Period, and Full and Final Settlement",
        "text": (
            "How to resign: Submit resignation in writing. An email to your manager with HR in CC is valid. Verbal resignations are not accepted. "
            "Notice periods by role level: "
            "During probation (first 3 months): 30 days notice from either side. "
            "After confirmation in non-managerial roles: 60 days notice. "
            "Manager level and above: 90 days notice. "
            "Your offer letter specifies your exact notice period. "
            "Notice period buyout: If you cannot serve the full notice period, you pay the shortfall amount calculated as Basic + DA per day multiplied by the number of days short. "
            "For example if your notice is 60 days and you serve only 40, you pay 20 days of Basic + DA. "
            "If the company releases you early, they pay you for the remaining days. "
            "Before your last working day you must: complete the exit clearance checklist on the HR portal, return your laptop, access card, and company SIM, get NOCs from IT, Finance, and Admin, and complete knowledge transfer to your team. "
            "Withdrawing resignation: Allowed within 3 working days. After that it needs department head and HR approval. "
            "Full and Final Settlement (F&F): Processed within 45 working days of your last day. "
            "F&F includes: remaining salary for days worked in the last month, encashment of unused annual leave at basic daily rate, pending reimbursements, minus any outstanding loans or advances. "
            "Only annual earned leave is encashed. Sick leave and casual leave balances are not paid out. "
            "Relieving letter and experience certificate are issued only after F&F is settled and all clearances are received. "
            "Absconding: If you stop reporting without notice, the company contacts you for 7 working days, after which it is treated as abandonment and you forfeit F&F dues."
        ),
    },
    {
        "id": "doc_009",
        "topic": "Reimbursements: Travel, Food, and Business Expenses",
        "text": (
            "All reimbursement claims must be submitted on the HR or Finance portal within 30 days of the expense. No exceptions after 30 days. Original receipts or e-invoices are mandatory for all claims. "
            "Flight travel: Book through the company's approved travel portal. Economy class only for domestic. Business class needs VP-level approval. Book at least 7 days in advance. "
            "Hotel stays for outstation travel: "
            "Tier-1 cities including Mumbai, Delhi, Bangalore, Hyderabad, Chennai, and Pune: up to Rs. 4,000 per night. "
            "All other cities: up to Rs. 2,500 per night. "
            "If you choose a more expensive hotel, you pay the difference yourself. "
            "Local transport during outstation travel: Taxi and auto fares reimbursed at actuals with receipts. Ola or Uber receipts are accepted. "
            "Using your own vehicle for official travel: Two-wheeler is Rs. 6 per km. Four-wheeler is Rs. 10 per km. Submit odometer readings or a map screenshot. "
            "Daily meal allowance during outstation travel: Rs. 500 per day in Tier-1 cities, Rs. 350 per day in other cities. This is a flat allowance and you do not need meal receipts. "
            "Internet reimbursement: Rs. 500 per month against your internet bill, only for employees in confirmed WFH or hybrid roles. "
            "Mobile phone reimbursement: Up to Rs. 1,000 per month against original bill, only for client-facing or field roles or if stated in your offer letter. "
            "Client entertainment: Meals or events with clients reimbursed at actuals with receipt and a note on attendees and business purpose. Alcohol is reimbursable only at client events, not internal team dinners. "
            "Travel advance: You can request up to Rs. 10,000 advance for outstation trips, to be settled within 7 days of return with receipts."
        ),
    },
    {
        "id": "doc_010",
        "topic": "Onboarding, Probation, and Confirmation",
        "text": (
            "Probation period: All new employees begin with a 3-month probation. Either side can end the contract with 30 days notice during probation. "
            "If performance is below expectations, HR can extend probation by up to 3 more months with written notice at least 2 weeks before the original end date. "
            "Benefits during probation: Salary and PF start from day one. Health insurance starts from day one. "
            "Annual leave accrues during probation but cannot be used until confirmation, except in genuine emergencies with manager approval. Casual and sick leave can be used normally from day one. "
            "Confirmation: At the end of 3 months, your manager submits a probation review on the HR portal. HR processes the confirmation letter within 5 working days. "
            "After confirmation you get: access to your accrued annual leave balance, health insurance extended to dependents, and eligibility for the annual increment cycle. "
            "Onboarding week: First week includes company orientation, IT setup for laptop and email, mandatory compliance training on POSH, data security, and the code of conduct, and team introductions. Attendance is compulsory. "
            "Mandatory e-learning: Complete all compliance modules on the LMS within 15 days of joining. Failing to complete them can delay your confirmation. "
            "Background verification: Started on day one. Covers all educational degrees, last 2 employers, and criminal record. "
            "Deliberate misrepresentation in your application — like claiming a degree you did not complete — can lead to termination even after you have joined. "
            "ID and access cards are issued on day one or two. Report any loss immediately to the Admin team."
        ),
    },
    {
        "id": "doc_011",
        "topic": "Training, Learning, and Development Policy",
        "text": (
            "Annual L&D budget: Every confirmed employee gets Rs. 15,000 per year for external learning — online courses, certifications, workshops, or conferences. "
            "How to use it: Get manager approval before enrolling. Submit course details and cost on the HR portal. After completing the course, submit your certificate and invoice for reimbursement. Unused budget lapses on March 31st and does not roll over. "
            "Sponsored certifications above Rs. 15,000: For high-value certifications like AWS, Azure, PMP, or CFA, the company may fully sponsor the cost with a service bond. You must stay with the company for at least 12 months after completing the certification. "
            "If you leave before 12 months, the cost is recovered proportionally in your F&F. For example if you leave 6 months after a Rs. 30,000 certification, Rs. 15,000 is recovered. "
            "Internal LMS: The company learning platform has courses on technical skills, leadership, communication, and compliance. All free for employees. HR tracks completion. "
            "Annual learning target: HR recommends at least 40 learning hours per year tracked on the LMS. This is a recommendation and is considered during appraisals. "
            "Internal mobility: After 18 months in your current role, you can apply for open internal positions. The hiring manager must inform your current manager before extending an offer. "
            "Mentorship programme: A 6-month structured programme pairing junior employees with senior leaders. Applications open in January each year. "
            "Leadership development programme: Open to employees rated 4 or 5 in the last appraisal and nominated by their manager. Includes 3 offsite workshops, a live business project, and executive coaching."
        ),
    },
    {
        "id": "doc_012",
        "topic": "Grievance Redressal and HR Helpdesk",
        "text": (
            "Every employee has the right to raise a concern without fear of retaliation. "
            "Level 1 — Talk to your manager first: For most workplace issues like workload, team dynamics, or role clarity, start with your reporting manager. Most issues are resolved here within 7 working days. "
            "Level 2 — HR Business Partner: If unresolved after 7 days, escalate to your HR Business Partner (HRBP). Each department has an assigned HRBP. The HRBP acknowledges within 2 working days and resolves within 15 working days. "
            "Level 3 — Head of HR: If the HRBP resolution is unsatisfactory, escalate to the Head of HR. Their decision is final for all HR matters. "
            "HR Helpdesk: For simpler queries — payslip issues, leave balance, reimbursement status, policy clarifications — use the helpdesk on the intranet portal. "
            "Helpdesk SLA: Acknowledged within 1 business day, resolved within 5 business days. "
            "POSH and harassment complaints bypass the regular grievance levels entirely and go directly to the Internal Complaints Committee (ICC). The ICC is a statutory body under the POSH Act 2013, operating independently of the HR chain of command. Complaints are confidential and both parties get a fair hearing. Retaliation against a complainant is a serious violation. "
            "Anonymous feedback: Submit via the anonymous feedback form on the intranet. HR reviews all submissions and takes systemic action where patterns are found. Individual follow-up is not possible for anonymous complaints. "
            "Whistleblower protection: Employees reporting financial fraud, safety violations, or serious policy breaches in good faith are protected from retaliation under the company Whistleblower Policy. Reports can go to the Head of HR or the Board Audit Committee."
        ),
    },
]
