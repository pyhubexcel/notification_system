rec_templates = [
    {
        "Doc_type" : "email",
        "for" : "when interview first round mail is sent",
        "message" : "Hi,#name: <br/> Your First round with #company: has been schedule on #date: at the #venue: for #job_profile: <br/> #hr_signature: ",
        "message_key" : "first_round",
        "message_origin" : "RECRUIT",
        "message_subject" : "#name!,your interview for First round of #job_profile: is scheduled",
        "recruit_details" : "Interview First Round",
        "version" : 1,
        "default" : False,
        "working" : True,
        "mobile_message" : "Hi,#name: Your First round with #company: has been schedule on #date: at the #venue: for #job_profile:"
    },
    {
        "Doc_type" : "email",
        "for" : "when candidate is hired",
        "message" : "<p>Dear #name: <br/> Greetings from #company: <br/>We are pleased to inform you that based on your subsequent interview and application; we are welcoming you to our organization #company: for the position of #designation: We look forward to you joining us from #date: at #time:. <br/> Please do not hesitate to call us for any information you may need.<br/>Kindly send your acceptance for the same.<br/> Congratulations! <br/> With Regards,<br/> #hr_signature: </p>",
        "message_key" : "interviewee_selection",
        "message_origin" : "RECRUIT",
        "message_subject" : "interviewee selected",
        "recruit_details" : "Interviewee Selection",
        "version" : 1,
        "default" : True,
        "working" : True,
        "mobile_message" : "Dear #name: Greetings from #company: We are pleased to inform you that based on your subsequent interview and application we are welcoming you to our organization #company: for the position of #designation: We look forward to you joining us from #date:.Please do not hesitate to call us for any information you may need Congratulations!With Regards"
    },
    {
        "Doc_type" : "email",
        "for" : "when interview second round mail is sent",
        "message" : "Hi,#name: <br/> Your Second round with #company: has been schedule on #date: at the #venue: for #job_profile: <br/> #hr_signature: ",
        "message_key" : "second_round",
        "message_origin" : "RECRUIT",
        "message_subject" : "#name!,your interview for Second round for #job_profile: is scheduled",
        "recruit_details" : "Interview Second Round",
        "version" : 1,
        "default" : True,
        "working" : True,
        "mobile_message" : "Hi,#name: Your Second round with #company: has been schedule on #date: at the #venue: for #job_profile:"
    },
    {
        "Doc_type" : "email",
        "for" : "when interview third round mail is sent",
        "message" : "Hi,#name: <br/> Your Third round with #company: has been schedule on #date: at the #venue: for #job_profile: <br/> #hr_signature: ",
        "message_key" : "third_round",
        "message_origin" : "RECRUIT",
        "message_subject" : "#name!,your interview for Third round for #job_profile: is scheduled",
        "recruit_details" : "Interview Third Round",
        "version" : 1,
        "default" : True,
        "working" : True,
        "mobile_message" : "Hi,#name: Your Third round with #company: has been schedule on #date: at the #venue: for #job_profile:"
    },
    {
        "message_key" : "chat_interested",
        "message" : "<p>\n  Hi #name: if you are interested for this Job offer from #company: <br/> <br/> Please kindly reply to this mail and we will contact you on this same email for further details.<br/>#hr_signature:\n</p>",
        "working" : True,
        "message_origin" : "RECRUIT",
        "message_subject" : "confirmation from #company:",
        "version" : 1,
        "default" : False,
        "for" : "when candidate is shortlisted",
        "recruit_details" : "still interested?",
        "Doc_type" : "email",
        "mobile_message" : "null"
    },
    {
        "message_key" : "chat_details",
        "message" : "<p>\n  Hi #name: if you are interested for this Job offer from #company: <br/> <br/> Please kindly reply to this email we would love to have a chat with you \n.<br/>#hr_signature:\n</p>",
        "working" : True,
        "message_origin" : "RECRUIT",
        "message_subject" : "confirmation from #company:",
        "version" : 1,
        "default" : False,
        "for" : "when candidate is shortlisted",
        "recruit_details" : "we would love to have a chat with you.",
        "Doc_type" : "email",
        "mobile_message" : "null"
    },
    {
        "message" : "<div>Hi&#160;</div><div>You're resume has been shortlisted for #jobProfile:&#160;</div><div>Please reply to this mail for showing your interest.</div><div><br></div><div>#hr_signature:</div><div>#company:</div><div>#date:&#160;&#160;</div>",
        "message_key" : "shortlist_confirmation",
        "working" : True,
        "mobile_message" : "shortlist confirmation message #date:",
        "message_origin" : "RECRUIT",
        "message_subject" : "Shortlist confirmation mail from #company:",
        "version" : 1,
        "default" : True,
        "for" : "when candidate is shortlisted",
        "recruit_details" : "shortlist confirmation",
        "Doc_type" : "email"
    },
    {
    "message" : "<font face=\"Arial\">#name:<br>#date:<br>#jobProfile:<br>#email:<br>#phone:</font>",
    "message_key" : "Test_Shortlist",
    "working" : True,
    "mobile_message" : "#name: #date: #jobProfile: #email: #phone:",
    "message_origin" : "RECRUIT",
    "message_subject" : "Test Shortlist",
    "version" : 1,
    "default" : False,
    "for" : "when candidate is shortlisted",
    "recruit_details" : "Test Shortlist",
    "Doc_type" : "email"
    },
    {
    "message" : "#name<br>#email<br>#date",
    "message_key" : "Custom_Message_Test",
    "working" : True,
    "mobile_message" : "#name #email #date",
    "message_origin" : "RECRUIT",
    "message_subject" : "Custom Message Test",
    "version" : 1,
    "default" : False,
    "for" : "when candidate is shortlisted",
    "recruit_details" : "Custom Message Test",
    "Doc_type" : "email"
    },
    {
    "message" : "#name:<br>#email:<br>#date:",
    "message_key" : "Custom_Test",
    "working" : True,
    "mobile_message" : "#name: #email #date:",
    "message_origin" : "RECRUIT",
    "message_subject" : "Custom Test",
    "version" : 1,
    "default" : False,
    "for" : "when candidate is shortlisted",
    "recruit_details" : "Custom Test",
    "Doc_type" : "email"
    },
    {
    "message" : "#name&#160;<br>you have completed round first,<br>congratulations!",
    "message_key" : "First_Round_Completed",
    "working" : True,
    "mobile_message" : "First Round Completed",
    "message_origin" : "RECRUIT",
    "message_subject" : "First Round Completed",
    "version" : 1,
    "default" : False,
    "for" : None,
    "recruit_details" : "First Round Completed",
    "Doc_type" : "email"
    },
    {
    "message" : "#name&#160;<br>you have cometed roud first,<br>congratulations!",
    "message_key" : "Interview Reminder",
    "working" : True,
    "mobile_message" : "Interview Reminder",
    "message_origin" : "RECRUIT",
    "message_subject" : "Interview Reminder",
    "version" : 1,
    "default" : False,
    "for" : None,
    "recruit_details" : "Interview Reminder",
    "Doc_type" : "email"
    },
    {
    "message" : "#name:<br>#interview_date:<br>#interview_time:<br>",
    "message_key" : "First_Round",
    "working" : True,
    "mobile_message" : "#name: #interview_date: #interview_time:",
    "message_origin" : "RECRUIT",
    "message_subject" : "First Round",
    "version" : 1,
    "default" : False,
    "for" : "undefined",
    "recruit_details" : "First Round",
    "Doc_type" : "email"
    },
    {
    "message" : "#name:<br>#interview_date:<br>hi there",
    "message_key" : "First_round_interview",
    "working" : True,
    "mobile_message" : "#name: #interview_date:",
    "message_origin" : "RECRUIT",
    "message_subject" : "First round interview",
    "version" : 1,
    "default" : True,
    "for" : "when interview first round mail is sent",
    "recruit_details" : "First round interview",
    "Doc_type" : "email"
    },
    {
    "message" : "test",
    "message_key" : "test",
    "working" : True,
    "mobile_message" : "test",
    "message_origin" : "RECRUIT",
    "message_subject" : "test",
    "version" : 1,
    "default" : False,
    "for" : "when interview first round mail is sent",
    "recruit_details" : "test",
    "Doc_type" : "email"
    },
    {
    "message" : "#date:<br>#name:",
    "message_key" : "Shortlist_confirmation",
    "working" : True,
    "mobile_message" : "#date: #name:",
    "message_origin" : "RECRUIT",
    "message_subject" : "shortlist confirmation",
    "version" : 1,
    "default" : False,
    "for" : "when candidate is shortlisted",
    "recruit_details" : "Shortlist confirmation",
    "Doc_type" : "email"
    },
    {
    "Doc_type" : "email",
    "for" : "when candidate is rejected",
    "message" : "<p>Dear Applicant <br/> Thank you very much for taking the time to interview with us for the profile of #job_profile:. We regret to inform that you couldn't clear the subsequent rounds of the interview process but we do appreciate your interest in the company and the job.<br/>We wish you all the best for future endeavors <br/>Regards<br/> #hr_signature: </p>",
    "message_key" : "interviewee_reject",
    "message_origin" : "RECRUIT",
    "message_subject" : "interviewee Rejection",
    "recruit_details" : "Interviwee Reject",
    "version" : 1,
    "default" : True,
    "working" : True
    }
]

