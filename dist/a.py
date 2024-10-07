import qrcode

list_of_employees = """
43992102	#	Aarti Govil	#	8860082339	#	Technical Assistant	@@@@@
95815884	#	Abhilash Pandey	#	8957878484	#	Technical Assistant	@@@@@
35404939	#	Agneesh Pratim Das	#	7321060674	#	Technical Officer 'B'	@@@@@
33112747	#	AKSHAY SHANKAR	#	9068343269	#	Research Associate	@@@@@
5189961	#	Aman Deep	#	8979105361	#	Technical Assistant	@@@@@
42978114	#	AMIT KUMAR SAGAR	#	8826171394	#	Technical Assistant	@@@@@
20210897	#	Amita	#	9811625099	#	Technical Officer 'A'	@@@@@
32190036	#	Anil Kumar	#	9899360735	#	Scientist F	@@@@@
13122299	#	Anil Kumar Keena	#	8505023022	#	Technical Assistant	@@@@@
63085946	#	Anil Kumar Verma	#	8851860901	#	MTS ( Technical )	@@@@@
19292772	#	Anit Singh Malik	#	9999094925	#	Consultant	@@@@@
39118196	#	Anoop Devi	#	9958902890	#	MTS (Gen)	@@@@@
77221319	#	Anuj Kumar	#	9717406388	#	Scientist - C	@@@@@
91406950	#	ANURAG	#	9882164926	#	Technical Assistant	@@@@@
58242408	#	ARCHANA SINGH	#	9927500622	#	Social Worker	@@@@@
89438334	#	Ashu	#	9540840849	#	Technical Officer 'A'	@@@@@
5151653	#	Avinash Malhotra	#	9873584595	#	U. D. Clerk	@@@@@
8237667	#	Ayurshi Patil	#	7721837622	#	JRF	@@@@@
6612359	#	Bansi Lal	#	7889639887	#	Driver	@@@@@
39821245	#	Binayak Kumar	#	9650800642	#	Senior Research Fellow	@@@@@
23293339	#	Chandan Govind	#	7541914804	#	Research Assistant	@@@@@
90541183	#	Chander Prakash Yadav	#	7983921806	#	Scientist - C	@@@@@
6788012	#	Chandresh	#	9891561199	#	Technical Officer 'A'	@@@@@
7171048	#	Deepali Chanu Sanasam	#	7303669368	#	Project SC. B	@@@@@
54972012	#	Dharmendra Kumar Sharma	#	9634042202	#	Tech-I	@@@@@
86598028	#	Dheeraj Rajaura	#	9758575056	#	Staff Car Driver-Grade-I	@@@@@
42208111	#	DHIRENDRA KUMAR SHARMA	#	8410756601	#	L. D. Clerk	@@@@@
7964530	#	Diksha Saini	#	8078651630	#	JRF	@@@@@
7073888	#	DINESH KUMAR	#	9467411025	#	Scientist - C	@@@@@
69632991	#	Dipakraj R Paunikar	#	9868552956	#	Account Officer	@@@@@
84622327	#	Divya Sharma	#	7906214166	#	Project Officer	@@@@@
73454613	#	Divyam Singh	#	7838673360	#	Senior Research Fellow	@@@@@
58045384	#	Dolly	#	9958935927	#	Technical Assistant	@@@@@
32909537	#	Dr. Ekta Gupta	#	9871562794	#	Scientist - E	@@@@@
32072606	#	Dr. Mausumi Bharadwaj	#	9811860996	#	Scientist F	@@@@@
36661091	#	Dr. Ruchika Gupta	#	9811756937	#	Scientist - C	@@@@@
53300944	#	Dr. Showket Hussain	#	9811446808	#	Scientist - C	@@@@@
79014120	#	Dr.Subhash M.Agarwal	#	9811741691	#	Scientist - D	@@@@@
88760043	#	Ganesh Dass	#	9419206039	#	L. D. Clerk	@@@@@
46189408	#	Gaurab Kumar Jha	#	9304492698	#	Research Assistant	@@@@@
92206115	#	Gaurav Sharma	#	9997528581	#	MTS ( Technical )	@@@@@
83827281	#	Geetika Ahuja	#	7982971714	#	Assistant	@@@@@
74299270	#	Himanshu Rohilla	#	9650421616	#	Technical Officer 'B'	@@@@@
10174631	#	Himanshu Sharma	#	8376068212	#	Project Officer	@@@@@
23667497	#	Isha Joshi	#	8826255650	#	Project Officer	@@@@@
75038864	#	Izazul Hasan	#	9927887621	#	Project Officer	@@@@@
51528763	#	Jahanvi	#	7905879511	#	Technical Assistant	@@@@@
8063165	#	Jigisha Chaudhary	#	9818210177	#	Research Associate	@@@@@
42769269	#	Jitendra Singh	#	8860247891	#	Tech-I	@@@@@
18320190	#	Jyoti	#	9968230193	#	Assistant	@@@@@
38076459	#	Jyoti Rani	#	9582045836	#	SEANOR RESEARCH FELLOW	@@@@@
94458231	#	Kailash Kumawat	#	8432063170	#	Staff Car Driver-Grade-I	@@@@@
88168170	#	Kakoli Borkotoky	#	9930640862	#	Scientist - C	@@@@@
18532561	#	Kalpana Verma	#	9013021200	#	Technical Officer 'A'	@@@@@
37083611	#	Kamran Manzoor	#	9999236157	#	Senior Research Fellow	@@@@@
66203466	#	Krishna Magoo	#	9811505438	#	PA	@@@@@
43536162	#	Kulvinder Kour	#	9086035313	#	Medical Social Worker	@@@@@
55535158	#	Lata Joshi	#	8130643108	#	Research Assistant	@@@@@
69351680	#	Latha Sriram	#	9871972558	#	Technical Officer 'C'	@@@@@
71045285	#	Mahboob Ali	#	8506031138	#	Lab Attendant	@@@@@
79614711	#	Malasha Kumari	#	9818416520	#	Scientist - C	@@@@@
8861199	#	Mamta Patel	#	9454216258	#	Assistant	@@@@@
18259801	#	Manu Bhardwaj	#	8860565767	#	Technical Officer 'B'	@@@@@
50055411	#	Manu Chaudhary	#	9810842906	#	Project Technician-A	@@@@@
59452319	#	MANUPAL CHOUDHARY	#	9024343890	#	Technical Officer 'B'	@@@@@
38496332	#	Mayank Maheshwari	#	8840127141	#	JRF	@@@@@
6740937	#	Mehreen Aftab	#	8826537860	#	Research Assistant	@@@@@
96704813	#	Mohammad Sajid	#	6386916812	#	Research Associate	@@@@@
76487466	#	Mohammad Shahid	#	9582692599	#	Project Officer	@@@@@
64646632	#	Mohd Mabood Khan	#	9873825682	#	Senior Research Fellow	@@@@@
24888853	#	Monu Sharma	#	9034220055	#	Assistant	@@@@@
42188279	#	Mr. PRAMOD KUMAR	#	8989142856	#	Account Officer	@@@@@
32648256	#	Mritunjay Kumar	#	9968477254	#	Tech-I	@@@@@
41433687	#	Mrs.Reena Dwivedi	#	9582121169	#	Technical Officer 'A'	@@@@@
40663647	#	Nasera Firdausi	#	7004360680	#	Research Assistant	@@@@@
83220910	#	Naveen Kumar	#	8285184804	#	U. D. Clerk	@@@@@
30807978	#	Nazneen Arif	#	8802309195	#	Scientist - D	@@@@@
95807727	#	Neeta Sawhney	#	9419189144	#	Project SC. B	@@@@@
19970131	#	Neha Kaushik	#	8882322142	#	L. D. Clerk	@@@@@
19766818	#	Nishant Kumar Saurabh	#	9472251595	#	Senior Research Fellow	@@@@@
95509864	#	Om Kant Mishra	#	7011123433	#	Tech-I	@@@@@
33391253	#	Pankaj Asopa	#	9660842104	#	Tech-I	@@@@@
24756650	#	Paras	#	8447445538	#	U. D. Clerk	@@@@@
30887060	#	Payal Singh	#	9999339310	#	Technical Officer 'A'	@@@@@
29076248	#	Pragya Sharma	#	9997016337	#	Technical Officer 'C'	@@@@@
93203899	#	Pramod Kumar	#	9650437970	#	Scientist - C	@@@@@
86257975	#	Prashant Kumar Singh	#	9560462996	#	Scientist - D	@@@@@
30055317	#	Pratibha Agnihotri	#	9958724043	#	Senior Research Fellow	@@@@@
69761332	#	Priyanka	#	9711772865	#	Staff Nurse	@@@@@
28007766	#	Puneet Kumar	#	7015805294	#	Technical Assistant	@@@@@
9394664	#	Pushparani Khwairakpam	#	7085915919	#	Project SC. B	@@@@@
85450047	#	R Suresh Kumar	#	8826253499	#	Scientist - D	@@@@@
93984037	#	Raj Narain	#	9868120166	#	Scientist - D	@@@@@
52726944	#	Rajesh	#	9990451695	#	Medical Social Worker	@@@@@
70607146	#	Rajesh Kumar	#	9891454597	#	MTS ( Technical )	@@@@@
53580026	#	Rajpal Suman	#	9760015935	#	Tech-I	@@@@@
17436471	#	Rajshree	#	9911155621	#	Technical Officer 'A'	@@@@@
83885244	#	Rajveer Kumar Raut	#	9555129930	#	Tech-I	@@@@@
40493854	#	Rajveer Singh	#	9873311584	#	Section Officer	@@@@@
48399052	#	Ranjana Prajapati	#	9315121260	#	Medical Social Worker	@@@@@
96737580	#	Ravi Kumar Yadav	#	8368735693	#	Project Technician-A	@@@@@
50629057	#	Rekha Saxena	#	9868510208	#	Scientist G	@@@@@
32265811	#	Rinki Bhadana	#	8750265640	#	Tech-I	@@@@@
46065554	#	Rubby Raina	#	9419103267	#	Project SC. B	@@@@@
3641471	#	Rupal Jain	#	8373918323	#	Project Officer	@@@@@
36043223	#	Sagarika Rout	#	7278347623	#	Project SC. B	@@@@@
39331551	#	Sakshi Tiwari	#	9953538699	#	Technical Assistant	@@@@@
38757502	#	Samim Ali	#	9140131932	#	Research Assistant	@@@@@
31680003	#	Sanchita Roy Pradhan	#	9749245717	#	Project SC. B	@@@@@
59589542	#	Sanchita Singh	#	7023358421	#	Scientist - D	@@@@@
55257017	#	Sandeep	#	9910104190	#	Project Officer	@@@@@
39930265	#	Sandeep Kumar	#	9050116347	#	Scientist - B	@@@@@
63346178	#	Sandeep Sharma	#	9910495257	#	MTS (Gen)	@@@@@
4840528	#	Sandeep Singh	#	7042247022	#	MTS (Gen)	@@@@@
16212382	#	Sandeep Sisodiya	#	9758624686	#	Project Associate-II	@@@@@
83904427	#	Sanjeev Kumar	#	9968442405	#	PS	@@@@@
70812400	#	Sant Ram	#	9910557376	#	U. D. Clerk	@@@@@
5633944	#	Sarika	#	9467559887	#	Technician C	@@@@@
28427117	#	Shagufta	#	9889945453	#	Senior Research Fellow	@@@@@
13227638	#	Shalini Singh	#	9811615561	#	Director	@@@@@
67805920	#	Shamsuz Zaman	#	9582046313	#	Scientist - D	@@@@@
42569932	#	SHASHANK LAKHERA	#	7062456044	#	Computer Progammer	@@@@@
19959416	#	Shefali Awana	#	8076317071	#	Assistant	@@@@@
70418499	#	Shivam	#	9996783050	#	Technical Assistant	@@@@@
27093551	#	SHIVANI BANSAL	#	8448732698	#	Research Assistant	@@@@@
526399	#	Shivesh Yadav	#	8126891015	#	Technical Assistant	@@@@@
60530850	#	Shoryaan	#	9821646219	#	Technical Assistant	@@@@@
9869870	#	Shruti Mishra	#	8887571694	#	JRF	@@@@@
73136792	#	Shubradip Ghosh	#	7278144483	#	Technical Assistant	@@@@@
76747673	#	Smita Asthana	#	9810622149	#	Scientist - D	@@@@@
9226436	#	Sonam Tulsyan	#	9695335511	#	Research Assistant	@@@@@
65388432	#	Soni Kumari	#	7376563498	#	Senior Research Fellow	@@@@@
89077072	#	SRISTY SHIKHA	#	9316178872	#	Research Associate	@@@@@
98072594	#	Sudhir Tanwar	#	7988830713	#	Scientist - B	@@@@@
72451535	#	Suman Kumari	#	8053223607	#	Technical Assistant	@@@@@
4284978	#	Sunil Kumar	#	9717381211	#	Assistant	@@@@@
80718715	#	SUNIL SINGH	#	9410032467	#	Driver	@@@@@
2441619	#	Surender Kumar	#	9419150806	#	Project SC. B	@@@@@
19298600	#	Suresh T.Hedau	#	9810589186	#	Scientist - D	@@@@@
79890623	#	Suryanshi Guleriya	#	9557170871	#	Technical Assistant	@@@@@
11282033	#	SWETA YADAV	#	9568026207	#	Project SC. B	@@@@@
88029190	#	SYED AKHTAR ALI	#	9897444786	#	Scientist - B	@@@@@
1901235	#	Tara Chand Gurjar	#	8700496768	#	Staff Car Driver-Grade-I	@@@@@
94679402	#	Upma Sharma	#	9911101918	#	Research Assistant	@@@@@
85995572	#	Vandana Tamrakar	#	7836071060	#	Project Scientist C	@@@@@
59319727	#	Varsha Pandey	#	9711016467	#	Project SC. B	@@@@@
29897708	#	Vijay	#	8059342178	#	Assistant	@@@@@
78440543	#	Vijesh Kumar	#	7015485840	#	Admin. Officer	@@@@@
39357365	#	Vikas Kumar	#	9992186148	#	U. D. Clerk	@@@@@
82977404	#	Vikram Singh Meena	#	9560474170	#	Technical Assistant	@@@@@
54645491	#	Vipin Kaushik	#	8700386074	#	MTS ( Technical )	@@@@@
48786376	#	Vishakha Kasherwal	#	8605853314	#	Senior Research Fellow	@@@@@
1056326	#	Vishal Lohan	#	9467313433	#	Technical Assistant	@@@@@
45637628	#	VISHVAJEET DUTTA	#	9557291145	#	Scientist - C	
"""

emps = list_of_employees.split("@@@@@")

# List of employee IDs
employee_ids = [
#     "59452319",
#     "12345678",
#     "87654321",
#     # Add more employee IDs as needed
]

emp_json = []
for e in emps:
    ee = e.split("#")
    employee_ids.append(str(ee[0]).strip())
    emp_json.append({
        "id" : str(ee[0]).strip(),
        "name" : str(ee[1]).strip(),
        "mobile" : str(ee[2]).strip(),
        "post" : str(ee[3]).strip()
    })

print(employee_ids)

# Function to generate QR code
def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

# Generate QR codes for all employees
for emp_id in employee_ids:
    e = emp_id
    if len(emp_id) == 8:
        e = emp_id

    if len(emp_id) == 7:
        e = "0" + str(emp_id)

    
    if len(emp_id) == 6:
        e = "00" + str(emp_id)

    if len(emp_id) == 5:
        e = "000" + str(emp_id)

    file_name = f"qrcodes/qr_code_{e}.png"
    generate_qr_code(e, file_name)
    print(f"Generated QR code for employee ID {emp_id} and saved as {file_name}")

print("----"*20)
print(emp_json)