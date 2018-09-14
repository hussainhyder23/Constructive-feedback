##use search() function
# coding: utf-8

# In[1]:


import nltk
from nltk import word_tokenize
import nltk
from nltk.corpus import stopwords


# In[2]:


stopwords = list(set(stopwords.words('english')))


# In[3]:


feedback=[

'Can someone post the series of events happening from past November or December to till now in the chronological order so that alumni can know what has happened till now and support what ever the way they can.',

'''To me CBIT is the best gift I had, where I learnt life, earned friends for life despite cultural, regional disparities. Whatever stress I might be under, watching Happy Days relieves that. That's the extent am attached to this lovely institute. Can't see this much hatred from many of you
Coming to the point, been going through the recent confessions from my sub sub sub sub... Juniors of the same college from past few months and seen news about the fee hike issue. I understand any management/manager thinks of cost cutting and REVENUE generation, but to what level.
Certain questions management should answer:
1. How fair is it to ask a student who joined assuming certain fee to pay the revised fee at the mid point of his academic tenure???
2. CBES has been receiving good amount of donations from NRI category seats, do we have any deficit in CBES funds/accounts??
3. You mean to say that faculty salaries are burdening you, for which fee is been revised with HC order?? Is it a valid fact. Can you please publicise at least to the institute committee the expenditures of last few financial years
To my Juniors, never give up on your protest. It's valid. I Know the pain of paying such abnormal fees. Education is not a business and it should never be. Stay strong, stay unite. If someone threatens you, just complain to higher authorities (may be Dept of Tech Education or State government). I guess you can get contact easily''',

'''why aren't the protest videos ,photos coming up on social media ?
I request people to come out of shy feelings and start posting on social media. Use social media as a tool and intensify the protest. we should learn from bits guys how intense they have protested against the fee hike both in college and social media and have garnered the support from alumni across the world. Just shouting in front of the main block will not give results.''',

'''I have seen a faculty member opened his mobile camera as if he is recording to intimidate students but he is actually not(maybe lack of storage capacity)''',

'''NOTE: Just another POV
As far as I remember, all the B-cat students had to sign on a bond paper that clearly states that you will have to pay the fee when increased. All of us chose to pay extra fee when we and our parents signed on that bond unlike A-cat who weren't given a bond. It was also clearly mentioned on the website during admission process that there will be fee hike. Those who cannot afford please go and talk to the management. Strikes will only bring down the little name that CBIT is left with and will only be a problem to us students without placements.''',

'''To all those who are blaming IT-2(3/4). First of all, a big SORRY. We admit that we wrote exam on 23rd ,but we didnt do it on purpose. We felt more bad than anyone else. We took all the blame. We realised our mistake and majority of us participated in the strike on 24th. But the point is,what are you doing? Constantly blaming someone even after realising their mistake? Grow up guys,have some shame and sense. Well, We are not ashamed of being in IT-2(3/4), you be ashamed to scold an IT -2(3/4)guy without a reason!''',

'''hi everyone, when i was in my 1st year, seniors were made a protest with us in favor to one of the faculty from so called IT department in order to make his job permanent. But now, only that so called IT department faculty is threatening the students more than the HOD and princi that they will be going to mark zero for all the mid exams if u are not going to attend the mid exams.Even other department HOD's are planning for retest but in so called IT department they are threatening the students and i got some info that IT3/4 students are facing this problem with their class teachers. I think this is one of the reason why they r not actively participating in the protest. I saw that no other department faculty is dividing the unity among the students except so called IT dept. They will say that we r favoring to our students it's not yet all true.keep it in your mind that at one time your children will also get this kind of situation. U will say that we r like your children but are u treating us in the same way?? shame on u. we have to protest for your jobs and increments but y u r not supporting us?? u r may be thinking that u may lost your job but at the time of protest for your jobs and increments we did that without thinking about our future. Are u thinking that by supporting to the management u may be promoted?? not yet all. I heard that one of the new joined faculty is telling to the students that "y u r wasting your money and time by doing all of this?? and your parents will pay y r u doing this thats their issue". Our parents are not rich to pay whatever and whenever the management will ask to pay the fee''',
'''Think twice before making false accusations on people. When ur pulling the whole of IT 3/4 into this, you’re blaming as many as 150 students and you don’t even know who wrote exams and who didn’t. If one section chooses to write( assuming they didn’t voluntarily choose to go write exams, even if they did they regret it now fosho) and the other doesn’t and also gave its full support in the protest, you’re still blaming all of them blatantly. And one sheep say some shit like this and all the others follow? even after all this, they’re still supporting. There’s a good chance of you losing their support if this continues. ''',
'''Dear crush,
you looked so pretty in the strike today. I couldnt control myself to like you. i love the way you smile without the conscious of surroundings, the confindence in you when you talk,move and act. Im a peace loving person,a backbencher , a daydreamer dreaming about you all the day. I just want you to know that i really like you.
You are my woman , my dream, my desire. You are as beautiful as the rising of sun , My face exhibits beautiful smile at the sight of you.
Im a bit scared to talk to you directly and to give you an eye contact. You are the one I wanted to find, to tell that i need you all my life.Having you by my side is what completes me.
Longlive my crush
Longlive students unity
Longlive CBIT strike
Hope this strike screws the management and brings down the hiked fee.
Hope my love accepts me.
Love you a lot .''',
'''To all the faculty members giving free advises "If you are too much concerned about us then give up your 1 year salary maybe give it to the students who are protesting then you will know the value of money that our parents are spending.Don't forget that we have seen many of you protesting at the principal chamber for obvious reasons. If you have right to protest then why can't we?” ''',
'''Why does the fee payment circular(16-8-18) say "The annual fee of Rs.1,13,500/- other than increased fee of Rs.86,500/- can be paid......" for the A cat students ? they haven't completely waived off the increment for A cat too, what if they ask A cat students to pay all of that increased fee in the final year? why such vague circulars ?''',
'''We IT students are really sorry for the issue but only the people from IT2 wrote the exams.
None of us from IT1 have attended the exams.
Please don't blame the entire IT Dept.
Thank you''',
''' Just in. Heard that students from ECE 3/4 have been brainwashed to write the mid exam in a way to respect the opinion of their HOD. Great to see how easy it is to break something like unity which we boasted about for all these days, and how hard it is to build trust!''',
''' Hello guys 
Don't try to listen to the management until and unless an official letter is released,we already trusted them once now untill the official letter comes we don't need to stop the strike.''',
'''Hello guys 
The stupid fkng management has displayed some of the students photos in the main block,if they do any suspension for those people then we guys have to not only fight against fee hike but aslo against the suspension of the student. ''',
'''To the principal of CBIT and the faculty
The students of CBIT have shownimmense patience in expecting a written circular stating the issue being addressed. The reason is we are no more 
try trusting ur words as you have failed to stick on to them. Sorry to say that we are no more trusting on this. For the money offew people,you have lost the 35years of legacy. Being more professional, if you had addressed the students about the issue the very first day would you think this situation would have arised? 
The lack of clarity in circular shows the commitment and integrity shown you all. when u know that ambiguous statements are also a death call why haven't you been clear?? The students of CBITdo have right question about the reason and whereabouts of our money. we need the entire money allocation as to where and how is this extra money going to?? The notice you have uploaded on the website saying that disciplinary actions will be taken, just think once why someone would do that? Have you not seen the ddesperation of us that the extra money is an extra burden for our parents. Think from a point of view of parents, dont you think its unfair. and u think we standing for our parents is wrong. The students neither damaged any property nor hurt someone then why the police force arrived? Isn't it our college issue? Do you really think forced suppresal will help the situation?! The students have no intention in causing chaos. Ifquestioning the injustice is injustice, what a shame to a 72 year old country!!! Lack of trust on you has made us all doubt that u are not going to exempt any student. What kind of guareentee is helping us that we are not asked to pay at the final year? What is the proof that no student from other Category is exempted ? When you have a right to demand us the money , we have even more right ask you that what are we gaining from it ?? 
oh wait are you send us to mars!? At moment we need an answer with CLARITY IN THOUGTH. When all the parents are not willing to pay why waste time on talking with each parent? Money greed had inhibited the functioning of minds?! 
Till now we had respect towards 
each faculty. But we don't think it is any longer existing. 
Yes we will question u abt things which you need to answer?? Why it is 86500? Do u guys have a specific reason to collect this amount? Give us a detailed list of what is happening to the money already paid and why u need an excess amount?? When u are in a position to answer us our questions, u will be in a position to question us??
The decision is still in ur hands but we don't trust you anylonger. ''',
''' Guys, it's too far now to stop the protest. Don't let this fade. This must continue. If this continues, the management won't have a choice but to decrese the fee at the end.
The situation doesn't really have a solution. Either the management or the students must compromise on the issue.
We shouldn't.
We won’t.''',
''' The students have given up and are not going to do any protest tomorrow. As they have agreed with the conditions of the faculty & management.
ADMIN: Dear Faculty Member Can you please tell us what sort of improvements can we do?? as you said "Needs some improvements''',
'''Tomorrow, Every one are gonna submit their letters for fee hike. & respectively write the mids.''',
'''when principal ,police ,faculty are following the page there cannot be any discussions done by the students in this page .I think it’s time to realise the importance of having Facebook groups which are rightly moderated like every top college in the country has .They bring all the students into a single platform.we can have one official group for all the club updates and official discussions of the clubs and student activities and Another group where informal discussions like these ,student interaction,opinion sharing and other kind of interactions take place.Give a like to the confession if you like the idea.I will anonymously create and moderate these Facebook groups''',
''' I am sad that todays protest was flop.
Principal was ahead of time and he made every other neccessary arrangement to make protest a flop and he succeded.Indeed he is brilliant .People used to say Dr.Ravinder reddy is best faculty cbit ever had ofcourse he is and he is best principal which he proved today,right from seating arrangement plans i.e separating final years and other guys , to calling police everything was perfectly planned.Hatsoff sir.
Coming to us We just barked we want justice for a while and then chilled down.Nothing else is going to happen.Damn sure.''',
''' Guys to stop the exams we just need not lock the CLS rooms,just think once if we lock AEC there isn't any chance of conducting the exam.job done''',
''' I dnt think u have a license ur smile drove me crazy this morning at the library''',
''' Hello, how to create an student email with @cbit.ac.in ? I need it for some internship purposes .Please respond ASAP''',
''' CBIT is amazing. I mean, they have answers for all the students questions and I love that.
Why did you increase our fees?
Management - we're spending it on the new R&D building
Why is the bus fee increased?
Management - We're building a new R&D building
Why wer the supplementary exams conducted before the reval results?
Management - We're building a new R&D building and it's important that you let us focus on that.
Is the 86,000₹ that B Cat needs to pay applied for the last year as well or only from this semester?
Mgmt - Yes
Is this a system bug that we're not able to pay through net banking or are you doing this to avoid bank to bank transaction?
Mgmt - Yes''',
''' You found another one
But I am the better one
I won't let you forget me
I still see your shadows in my room
Can't take back the love that I gave you
It's to the point where I love and I hate you
And I cannot change you, so I must replace you, oh
Easier said than done
I thought you were the one
Listenin' to my heart instead of my head''',
'''Today we received a circular naming fee payment for 3 and 5 semester... CBIT management don't even know how to write a circular about anything... They stated some circular dated ....... There is no Clarity in the amount of fee to be payed... according to management b category people need to pay increased amount of 86,000 with this year fee which is inclusive of increased amount (2,00,000)... There is no clarity for a category either.. they just mentioned "other than that" what other than that ?! At the strike time they said there is no increase in fee ... And now after 8 months ... No change in increase of fee... Why did you say that there is no change in fee and again release a circular with increase in fee ''',
'''To dear Sr*****a of D2
I’m so scared that today will one day become an yestered time
I’m scared that tomorrow will some day become the present
I’m scared , not that time is getting passed 
But , because a day comes when I’ve to define our relationship
A day might come when I’ve to fight with those yestered hours 
I’m so scared not to define our relationship
But , an another from you
I’m so scared not to fight with those yestered hours
But , to fight time without you...
I think it’s high time I defined our relationship
To not feel the regret of not being in time
I love you
From your admirer''',
'''To that once existed family of D2 2/4
This is one of those , who was so jealous of your sweet gang which seems exist anymore... There wasn’t a day I got into my bus , without feeling sad for not having one like yours.
I now feel so sad for all of you , for not being like you all were
I remember , the way you all were together in all prospects, say in bunking a class or to help each other or what not...
You may say , you all are the same , but you aren't , bunk a few classes sit retrospect, decide.
You 'll now not realize what you guys are going to miss , I know how tough it is ... This is in no way asking you to get together again , but it’s to say the love I had for yours.. 
From a secret admirer (Mechanical -1) ''',
'''Hi Sr**ya - 4/4 CSE3 You are Cute, Intelligent, Natural, Bold, always cheerful and sportive. Your eyes are really attractive. I like your character a lot. You are beautiful inside and outside. <3 You have all the qualities that a girl should have. You were my secret crush since first year, will always be my crush and its high to confess now. I really like you and respect you. Hope i get a chance to meet you and talk to you. A guy from B.E-4/4 ''',
'''CBIT sudhee is known as one of worst managed and conducted fests in and around Hyderabad. No college as such big organizing team and that worse events. There is need of having unified team from all branches together with people who have enough skills and capabilities manage the fest. Time has come for the management to realize the reality and change the way the fest is conducted. ''',
'''this is a cringy confession with a lot of edge. Skip this if you aren't into those. I just wanted to be loved by someone. Everything I did for the past year was that I could have someone who will never leave me. I was under the impression that the more weird you are, the more lovable you are. A complete blind shot in the dark really. I thought I will never survive this alone. Now, it became a complete mess. Being hated used to scare me. That's why I always kept to myself. Now it feels like everyone hates me. I thought it would be hard to survive this. But now I can stop pretending to be someone I am not. It's just one more year. I will avoid you whenever I can. Bear with me. I probably won't be in contact with anyone from college after this. I will walk this road alone and someday I will be strong to protect the things I hold dear. This is the path I choose and I am fine with it. I thought I needed someone to love me but ahh, duck it. I will just love myself. I don't need anyone anyway.''',
'''I hope this 3rd year chemical senior will acknowledge my presence in college. Still waiting for him to catch me staring at him in bus bay ''',
'''esson learnt in CBIT.
Most of us have too much of technical stuff, but we don't really speak up during interviews. Why? Because our lazy asses are accustomed to speaking Telugu. Communication skills in English are more important than any other frigging technical skills to get that dream job. I know most of you take a chill-pill feeling that you can do way better in life than your absolutely-rubbish English speaking professors in CBIT. Let me break it to you, you need to speak brilliantly (no matter what you speak) to ace your placements. Good written communication helps you weave shit stories in your answer sheet and eventually get an S Grade. When in doubt, confuse with extraordinary vocabulary. Try it, because it helps. So instead of wasting your time ogling at that hot chick near CSE block, do something worthwhile or you will never get to her. 
No offense, but this is for your own benefit. ''',

]


# In[14]:


def dict_search_words(feedback,stopwords):
    all_words=[]
    for i in range(0,len(feedback)):
        all_words += word_tokenize(feedback[i].lower())
    all_words=list(set(all_words))
    
    
    filtered_words = [w for w in all_words if not w in stopwords] 
    filtered_words.sort()
    
    all_words=[]
    for word in filtered_words:
        if word.isalpha():
            all_words.append(word)
    
    dict_words={}
    min_len_word=2
    if dict_words=={}:
        for word in all_words:
            if word[0] not in dict_words.keys():
                    dict_words[word[0]]=[]
            dict_words[word[0]].append(word)
    length=1
    while length < min_len_word:
        for key in dict_words.keys():
            temp_dict={}
            for word in dict_words[key]:
                if len(word) >length:
                    if word[length] not in temp_dict.keys():
                        temp_dict[word[length]]=[]
                    temp_dict[word[length]].append(word)
            dict_words[key]=temp_dict
        length+=1
    return dict_words


# In[16]:


def search():
    dict_search=dict_search_words(feedback,stopwords)
    string = input().lower()

    search_words=dict_search[string[0]]
    search_words=search_words[string[1]]
    length =2
    while(length<len(string)):
        remove=[]
        for word in range(0,len(search_words)):
            if search_words[word][length] !=string[length]:
                remove.append(search_words[word])
                
        length+=1

        for i in range(0,len(remove)):
            search_words.remove(remove[0])
            remove=remove[1:]
    return search_words


# In[17]:


search()

