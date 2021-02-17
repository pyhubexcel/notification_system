rec_templates = [
    {
        "Doc_type" : "email",
        "for" : "when interview first round mail is sent",
        "message" : "Hi #name:,<div><br></div><div>Thank your for application for the role of #job_profile: with #company:</div><div><br></div><div>Your application for the<span>#job_profile: stood out to us and we would like to schedule your interview. on</span><span>#date: at the #venue:</span></div><div><br></div><div>Please confirm your availability for the same.</div><div><br> #hr_signature: </div>",
        "message_key" : "first_round",
        "message_origin" : "RECRUIT",
        "message_subject" : "#name: your interview for First round of #job_profile:",
        "recruit_details" : "Interview First Round Onsite",
        "version" : 1,
        "default" : True,
        "working" : True,
        "mobile_message" : "Hi #name: Your First round with #company: has been schedule on #date: at the #venue: for #job_profile:",
        "jobProfileId":None
    },
    {
        "Doc_type" : "email",
        "for" : "when candidate is hired",
        "message" : "<p>Dear #name: <br/> Greetings from #company: <br/>We are pleased to inform you that based on your subsequent interview and application; we are welcoming you to our organization #company: for the position of #job_profile: We look forward to you joining us from #date: at #time:. <br/> Please do not hesitate to call us for any information you may need.<br/>Kindly send your acceptance for the same.<br/> Congratulations! <br/> With Regards,<br/> #hr_signature: </p>",
        "message_key" : "interviewee_selection",
        "message_origin" : "RECRUIT",
        "message_subject" : "Job Offer For #job_profile:",
        "recruit_details" : "Interviewee Selection",
        "version" : 1,
        "default" : True,
        "working" : True,
        "mobile_message" : "Dear #name: Greetings from #company: We are pleased to inform you that based on your subsequent interview and application we are welcoming you to our organization #company: for the position of #job_profile: We look forward to you joining us from #date:.Please do not hesitate to call us for any information you may need Congratulations!With Regards",
        "jobProfileId":None
    },
    {
        "Doc_type" : "email",
        "for" : "when interview second round mail is sent",
        "message" : "Hi #name: ,<div><br></div><div>Based on the feedback on your previous interview, we would like to invite you for the next round of interview.</div><div><br></div><div> Your Second round with #company: has been schedule on #date: for #job_profile:</div><div><br></div><div>This is an online interview, you will be getting an invite for the same on your email.<br><br></div><div>Please confirm your availability for the same.</div><div><br></div><div> #hr_signature: </div>",
        "message_key" : "second_round",
        "message_origin" : "RECRUIT",
        "message_subject" : "#name: your interview for Second round for #job_profile: is scheduled",
        "recruit_details" : "Interview Second Round",
        "version" : 1,
        "default" : True,
        "working" : True,
        "mobile_message" : "#name! your interview for Second round for #job_profile: with #company:",
        "jobProfileId":None
    
    },
    {
        "Doc_type" : "email",
        "for" : "when interview third round mail is sent",
        "message" : "Hi #name:,<div><br></div><div>Based on the feedback on your previous interview, you have been further shortlisted for the final round of interview.<br><div><br></div><div> Your final round with #company: has been schedule on #date: at the #venue: for #job_profile:</div><div><br></div><div>Please confirm your availability for the same.<br><br></div><div> #hr_signature: </div></div> ",
        "message_key" : "third_round",
        "message_origin" : "RECRUIT",
        "message_subject" : "#name: your interview for Third round for #job_profile: is scheduled",
        "recruit_details" : "Interview Third Round",
        "version" : 1,
        "default" : True,
        "working" : True,
        "mobile_message" : "Hi,#name: Your Third round with #company: has been schedule on #date: at the #venue: for #job_profile:",
        "jobProfileId":None
    },
    {
        "message_key" : "chat_interested",
        "message" : "<p>Hi #name:,</p><p><br></p><p>How are you doing today!</p><p><br></p><p>Thank your for your job application for the role #job_profile: with our company #company:<br> <br>Just want to get in touch and see if you are still interested in this job profile.<br><br> Kindly reply to this mail and we will contact you on this same email for further details.</p><p><br>#hr_signature:</p>",
        "working" : True,
        "message_origin" : "RECRUIT",
        "message_subject" : "#name: Your application for #job_profile:",
        "version" : 1,
        "default" : True,
        "for" : "when candidate is shortlisted",
        "recruit_details" : "still interested?",
        "Doc_type" : "email",
        "mobile_message" :" Hi #name: Thank you for applying to the #job_profile: position at #company:. If you are interested for the role,kindly reply to this SMS and we will contact you on this same number for further details. #hr_signature:",
        "jobProfileId":None
    },
    {
        "message_key" : "chat_details",
        "message" : "<p>Hi #name:,</p><p><br></p><p>Thank your for your job application for the role #job_profile: with our company #company:<br><br>We did love to chat further with you regarding the role.<br><br></p><p>Kindly reply to this mail with your availability so we can contact you accordingly.</p><p><br>#hr_signature:</p>",
        "working" : True,
        "message_origin" : "RECRUIT",
        "message_subject" : "#name: Your application for #job_profile:",
        "version" : 1,
        "default" : True,
        "for" : "when candidate is shortlisted",
        "recruit_details" : "we would love to have a chat with you.",
        "Doc_type" : "email",
        "mobile_message" :"Hi #name: we would love to chat with you regarding #job_profile: from #company: Please kindly reply to this SMS with a suitable time, we would love to have a chat with you #hr_signature:",
        "jobProfileId":None
    },
    {
        "message" : "<div>Hi #name:,</div><div><br></div><div>In reference to your application for the #job_profile: with #company:</span></div><div><br></div><div>You're resume has been shortlisted for #job_profile:</div><div><br></div><div>Please reply to this mail for showing your interest, so we can further process your application.</div><div><br></div><div>#hr_signature:</div>",
        "message_key" : "shortlist_confirmation",
        "working" : True,
        "mobile_message" : "shortlisted for #job_profile: with #company:",
        "message_origin" : "RECRUIT",
        "message_subject" : "Shortlisted for #job_profile:",
        "version" : 1,
        "default" : True,
        "for" : "when candidate is shortlisted",
        "recruit_details" : "shortlist confirmation",
        "Doc_type" : "email",
        "jobProfileId":None
    },
    {
        "message" : "Hi #name:, <br/><br/> Regarding your job application for profile #job_profile: with #company: . <br/> Your interview for #round_name: has been reschedule to #date: #time: <br/><br/> #hr_signature:",
        "message_key" : "Interview_date_updated",
        "working" : True,
        "mobile_message" : "Hi #name:, \nRegarding your job application for profile #job_profile: with #company: . \nYour interview for #round_name: has been reschedule to #date: #time: \n #hr_signature:",
        "message_origin" : "RECRUIT",
        "message_subject" : "Interview rescheduled for #job_profile:",
        "version" : 1,
        "default" : True,
        "for" : "when candidate interview date updated",
        "recruit_details" : "interview date updated",
        "Doc_type" : "email",
        "jobProfileId":None
    },
    {
        "Doc_type" : "email",
        "for" : "when candidate is rejected",
        "message" : "<p>Dear Applicant <br/><br/> Thank you very much for taking the time to interview with us for the profile of #job_profile:. We regret to inform that you couldn't clear the subsequent rounds of the interview process but we do appreciate your interest in the company and the job.<br/><br/>We wish you all the best for future endeavors <br/><br/>Regards<br/> #hr_signature: </p>",
        "message_key" : "interviewee_reject",
        "message_origin" : "RECRUIT",
        "message_subject" : "Interview Rejection for #job_profile:",
        "mobile_message" : "Thank you very much for taking the time to interview with us for the profile of #job_profile:.",
        "recruit_details" : "Interviwee Reject",
        "version" : 1,
        "default" : True,
        "working" : True,
        "jobProfileId":None
    },
    {
        "Doc_type" : "email",
        "for" : "when candidate is registered",
        "message" : "Hi #name:, <br/><br/> Your account has been successfully created.<br/><br/>Your login details are as follows<br/> Email: #email: <br/> Password : #password: <br/> Role: #role: <br/><br/> You can login at #website_url:",
        "message_key" : "candidate_registered",
        "message_origin" : "RECRUIT",
        "message_subject" : "Account Created on recruit",
        "mobile_message" : "Hi #name: \n\nYour account has been successfully created.\n\nYour login details are as follows\nEmail: #email: \nPassword : #password: \nRole: #role: \nYou can login at #website_url:",
        "recruit_details" : "Candidate Registration",
        "version" : 1,
        "default" : True,
        "working" : True,
        "jobProfileId":None
    },
    {
        "Doc_type" : "email",
        "for" : "when password is changed",
        "message" : "Hi #name:, \n\n Your password has been changed to #password: ",
        "message_key" : "password_changed",
        "message_origin" : "RECRUIT",
        "message_subject" : "Password Changed",
        "mobile_message" : "Hi #name:, \n\nYour password has been changed to #password: ",
        "recruit_details" : "Password Changed",
        "version" : 1,
        "default" : True,
        "working" : True,
        "jobProfileId":None
    },
    {
    "message" : "#name: <br>you have completed round first,<br>congratulations!",
    "message_key" : "Interview Reminder",
    "working" : True,
    "mobile_message" : "#name: \nyou have completed round first, \ncongratulations!",
    "message_origin" : "RECRUIT",
    "message_subject" : "Interview Reminder",
    "version" : 1,
    "default" : True,
    "for" : "Interview_reminder",
    "recruit_details" : "Interview Reminder",
    "Doc_type" : "email",
    "jobProfileId":None
    },
    {
    "message" : "Hi #name:, <br><br> Thanks for your job application for #job_profile: with #company: <br><br> We could not find your resume, could you provide the same by replying on this email. <br><br> Thanks <br> #hr_signature:",
    "message_key" : "Resume_missing",
    "working" : True,
    "mobile_message" : "Hi #name:, \n\nThanks for your job application for #job_profile: with #company: \n\nWe could not find your resume, could you provide the same by replying on this email. \nThanks \n #hr_signature:",
    "message_origin" : "RECRUIT",
    "message_subject" : "Resume Missing for your job application #job_profile:",
    "version" : 1,
    "default" : True,
    "for" : "when candidate resume is missing",
    "recruit_details" : "Resume Missing",
    "Doc_type" : "email",
    "jobProfileId":None
    },
    {
    "message" : "Hi #name:, <br><br> You need to take interview of #candidate_name: for #round_name: on date #interview_date: #interview_time: and profile of candidate profile link is  <br> #candidate_link:",
    "message_key" : "candidate_interview",
    "working" : True,
    "mobile_message" : "Hi #name:, <br><br> You need to take interview of #candidate_name: for #round_name: on date #interview_date: #interview_time: and profile of candidate profile link is <br> #candidate_link:",
    "message_origin" : "RECRUIT",
    "message_subject" : "Candidate Interview Schedule",
    "version" : 1,
    "default" : True,
    "for" : "when need to take candidate interview",
    "recruit_details" : "Candidate interview",
    "Doc_type" : "email",
    "jobProfileId":None
    },
    {
    "message" : "Hi #name:, <br><br> How are you doing today! <br><br> Thank your for your job application for the role of #job_profile: with our company #company: <br><br> I wanted to get in touch with you to get to know more about skills and experience. <br><br> Let me know a suitable time and your contact information, so we can get on a call. <br><br> #hr_signature:",
    "message_key" : "ask_for_call_availability",
    "working" : True,
    "mobile_message" : "Hi #name:, <br><br> How are you doing today! <br><br> Thank your for your job application for the role of #job_profile: with our company #company: <br><br> I wanted to get in touch with you to get to know more about skills and experience. <br><br> Let me know a suitable time and your contact information, so we can get on a call. <br><br> #hr_signature:",
    "message_origin" : "RECRUIT",
    "message_subject" : "ask for call availability?",
    "version" : 1,
    "default" : True,
    "for" : "when need to ask candidate for call",
    "recruit_details" : "ask for call availability?",
    "Doc_type" : "email",
    "jobProfileId":None
    }
]





"""
    {
    "message" : "<div>Hi #name:,</div><div><br></div><div>You are on Hold for #job_profile: with #company:</div>",
    "message_key" : "Candidate Hold",
    "working" : True,
    "mobile_message" : "Candidate is on hold for #job_profile: with #company:",
    "message_origin" : "RECRUIT",
    "message_subject" : "Candidate Hold for #job_profile:",
    "version" : 1,
    "default" : False,
    "for" : "when candidate is on hold",
    "recruit_details" : "Candidate is on hold",
    "Doc_type" : "email",
    "jobProfileId":None
    }
"""