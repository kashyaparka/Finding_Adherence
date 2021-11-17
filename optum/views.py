from django.shortcuts import render,HttpResponse
import joblib

# Create your views here.
race = {
 'white': 0.4674593605314334,
 'asian': -2.5855348901151984,
 'black': -1.8222863274535406,
 'native': -1.0590377647918825,
 'other': -0.2957892021302246
 }
county={
 'Worcester': 1.337772903251873,
 'Bristol': -1.4957973594943426,
 'Middlesex': 0.04978642018541139,
 'Suffolk': 1.0801756066385806,
 'Norfolk': 0.564981013411996,
 'Franklin': -0.7230054696544655,
 'Hampshire': -0.20781087642788093,
 'Hampden': -0.4654081730411732,
 'Dukes': -1.2382000628810501,
 'Essex': -0.9806027662677579,
 'Plymouth': 0.8225783100252884,
 'Barnstable': -2.0109919527209272,
 'Berkshire': -1.7533946561076348,
 'Nantucket': 0.3073837167987037
 }
country={'US': 0.2451505779899407,
 'VN': 0.8047309977180014,
 'PE': -0.8740102614661807,
 'DO': -4.231492779834545,
 'IT': -2.2729613107863322,
 'HT': -2.832541730514393,
 'MX': -1.4335906811942412,
 'DM': -4.511282989698575,
 'IN': -2.5527515206503626,
 'VE': 0.524940787853971,
 'CR': -5.070863409426636,
 'FR': -3.9517025699705144,
 'PR': -0.5942200516021503,
 'CL': -5.910234039018727,
 'CN': -5.6304438291546965,
 'DE': -4.7910731995626055,
 'GR': -3.671912360106484,
 'PA': -1.153800471330211,
 'RU': -0.31442984173811994,
 'HN': -3.1123319403784233,
 'GT': -3.3921221502424537,
 'JM': -1.9931711009223019,
 'KR': -1.7133808910582715,
 'SV': -0.034639631874089624,
 'CO': -5.350653619290666}
gender={
 'F': -0.8202802674980424, 
 'M': 1.2188528665495406
 } 

ethinicty={
  'nonhispanic': 0.3223546403468008, 
  'hispanic': -3.101555958178205
 }      

def index(request):
    return render(request,'index.html')

def models(request):
    return render(request,'models.html')

def project(request):
    return render(request,'project.html')

def result(request):
    lis = []
    cls = joblib.load('Final_model')

    #res.append(request.GET[])
    get_country=request.POST.get('Dropdown')
    get_ethnicity=request.POST.get('Dropdown1')
    get_county=request.POST.get('Dropdown2')
    get_race=request.POST.get('Dropdown3')
    get_gender=request.POST.get('Dropdown4')
    get_age=request.POST.get('Number')
    get_country = country[get_country]
    get_ethnicity = ethinicty[get_ethnicity]
    get_county = county[get_county]
    get_race = race[get_race]
    get_age = get_age
    get_gender = gender[get_gender]

    lis.append(get_gender)
    lis.append(get_ethnicity)
    lis.append(get_race)
    lis.append(get_county)
    lis.append(get_country)
    lis.append(int(get_age))
    
    print(lis)
    ans = cls.predict([lis])
    print(ans[0])
    if ans[0]==0:
      k="Adherent"
    else:
      k="Non-Adherent"
    return render(request,'result.html',context={"ans":k})

