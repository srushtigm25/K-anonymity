# K-anonymity
Implemented 3-anonymity using concepts like generalization and suppression in Python for the following data such that the Hospital can use it to provide service for patients with Cancer, Cardiac and pulmonary-related health issues. (The hospital cannot provide services if the type of health issue is not known)

Patient ID	Name	Gender	Postcode	Age	Disease
1	Amber	Female	57678	29	Cardiac
2	Bill	Male	57678	22	Cardiac
3	Carol	Female	57678	27	Cardiac
4	David	Male	57905	43	Pulmonary
5	Elaena	Female	57909	52	Pulmonary
6	Frank	Male	57906	47	Pulmonary
7	Garry	Male	57605	30	Cardiac
8	Hendrik	Male	57673	36	Cancer
9	Immanuel	Male	57607	32	Cancer
10	Jim	Male	57607	42	Pulmonary
11	Kimberly	Female	57906	27	Cardiac
12	Ken	Male	57907	23	Cardiac
13	Mike	Male	57908	37	Cancer
14	Merry	Female	57678	54	Pulmonary
15	Nancy	Female	57678	57	Pulmonary

K=3, so K-1 = 2 (Choose 1 piece of data, guarantee we can find 2 other user with same data)
Generalization: Hides critical privacy data with generic data
Suppression: Removes or suppresses the critical privacy
Disease: Cannot be null or suppressed
Age: Generalization (age range)
Patient_ID, Name & Postcode: Suppression (Null)
