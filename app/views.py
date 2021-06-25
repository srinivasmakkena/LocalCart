from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.models import User
from .forms import OrderForm,ProductForm
locationlist=["Addanki","Bommanampadu","Chakrayapalem","Chinakothapalli","Dharmavaram","Dhenuvakonda","Gopalapuram","Gowada","Jarlapalem","Kalavakuru","Kotikalapudi","Kunkupadu","Manikeswaram","Modepalli","Mylavaram","Nagulapadu","Perayapalem","Ramayapalem","Sankavarappadu","Singarakondapalem","Timmayapalem","Uppalapadu","Vangapadu","Velamuripadu","Vemparala","Venkatapuram","Vipparlavaripalem","Ardhaveedu","Ayyavaripalli","Bogole","Bollupalli","Donakonda","Gannepalli","Kakarla","Maguturu","Mohiddinpuram","Nagulavaram","Papinenipalli","Peddakandukuru","Rangapuram","Velagalapaya","Yachavaram","Ambadipudi","Ballikurava","Chennupalli","Gorrepadu","Guntupalli","K.rajupalem","K.v.palem","Konidena","Kopperapadu","Kopperapalem","Kothuru","Kukatlapalli","Mallayapalem","Mukteswaram","N.b.padu","S.l.gudipadu","Uppumaguluru","Vallapalli","Velamavaripalem","Vemavaram","Vydena","Akkapalli","Basinepalli","Bestavaripeta","Ch.obinenipalli","Chetticherla","Galijerugulla","J.b.k.puram","J.c.agrahram","Khajipuram","Konapalli","M.p.cheruvu","Mokshagundam","Nekunambad","P.b.puram","P.obinenipalli","Pandillapalli","Pitikayagulla","Pusalapadu","Salakalaveedu","Ambavaram","AmbavaramKothapalli","Anikalapalli","Arivemula","Ayyalurivaripalle","Boyamadugula","Chandrasekhara Puram","Chennapanayunipalli","Cherlopalli","Chintapudi","D.g.peta","K.agraharam","Kambhampadu","Kovilampadu","Nallamadugula","Pedarajupalem","PeddaGollapalli","ullagurapalli","R.k.palli","Regulachilaka","Uppalapadu","V.bayalu","Venganagunta","Bandlamudi","Budawada","Busarapalli","Chandrapadu","Chimakurthy","Chinaravipadu","Devarapalem","E.v.palem","Gadiparthivaripalem","Gonugunta","Ilapavuluru","K.v.palem","M.v.palem","Manchikalapadu","Nekunambadu","Nippatlapadu","P.nayudupalem","Pallamalli","Pidathalapudi","Pulikonda","R.c.puram","R.l.puram","Torragudipadu","Yarragudipadu","Chinnaganjam","Chinthagumpalli","Gonasapudi","Kadavakuduru","Kothapalem","Motupalli","Munnamvaripalem","Neelayapalem","Pallepalem","Pedaganjam","R.b.palem","Santharavuru","Chirala Municipality","Chirala Census Town","Gavinivari Palem","Ipuru Palem","Bandiveligandla","Basireddypalli","Botlapalem","Chandaluru","Darsi","Devavaram","East","Chavatapalem","East","Veerayapalem","East","Venkatapuram","Jamukuladinne","Korlamadugu","Kothapalli","Lankojanapalli","Mareddypalli","Papireddypalem","Peda","Vuyyalawada","Pothakamuru","Pothavaram","Rajampalli","Ramachandrapuram","Samanthapudi","T.s.puram","Tanamchintala","Tummedalapadu","Venkatachalampalli","Yarraobanapalli","Aravallipadu","Bhumanapalli","Chandavaram","Donakonda","Gangadevipalli","Indlacheruvu","Kocherlakota","Mallampeta","Manginapudi","P.venkatapuram","Peddannapalem","Polepalli","Ramapuram","Rudrasamudram","Sangapuram","Tellabadu","Vaddipadu","WestLakshmipuram","Chinna Dornala","Chinna Gudipadu","Dornala","Jammidornala","Katakanipalli","Nallaguntla","P.bommalapuram","Y.cherlopalli","Yadavalli","Adimurthipalli","Ambavaram","Ghadikota","Giddaluru","Jayarampuram","K.s.palli","Kanchipalli","Kommunuru","Kongalaveedu","Kothakota","Mundlapadu","Narava","Obulapuram","Podalakondapalli","Sanjevaraopeta","Tamballapalli","Timmapuram","Vuyyalawada","Yellupalli","Adavirajupalem","Ammavaripalem","Basireddypalem","Chevuru","Chimidithapadu","Chinalatarapi","Dappalampadu","Darakanipadu","Gudepalem","Gudluru","Kothapeta","Mocherla","Mogalluru","Nayudupalem","Pajarla","Parakondapadu","Potluru","Puretipalli","Ravuru","Salipeta","Swarnajipuram","Venkampeta","Yelurupadu","Dasallapalli","Dasaripalli","Doddichinthala","Gayamvaripalli","H.m.padu","HanumanthuniPadu","Hanumathapuram","Hazeepuram","Kistampalli","Kondareddypalli","Kutagundla","Lingamgunta","Mahammadapuram","Mittapalem","Muppallapadu","Nallagandla","Nandanavanam","PedaGollapalli","Seetharampuram","Timmareddypalli","Ummanapalli","Valicherla","Veeraramapuram","Vemulapadu","Bheemavaram","Duddukuru","Gangavaram","Idupulapadu","Inkollu","Koniki","Nagandla","Nakkalapalem","Pavulur","Pusapadu","Subbareddypalem","Sudivaripalem","Vankayalapadu","Alavalapadu","Arikatlavaripalem","Bhagavanrajupalem","Budawada","Bytamanjuluru","Chandaluru","Chinamallavaram","Jagarlamudivaripalem","Janakavaram","Kallamvaripalem","Kasyapuram","Kondamanjuluru","Kondamuru","Kotapadu","Muppavaram","Nujellapalli","Panguluru","Ramakuru","Renangivaram","T.kopperapadu","T.takkellapadu","Anadapuram","Ananthasagaram","Balijapalem","Divivaripalem","G.mekapallem","Jillellamudi","K.m.palem","Kammavaripalem","Kancharagunta","Kondikandukur","Kovuru","Machavaram","Mahadevapuram","Mopadu","Narisettyvaripalem","Oguru","Palukur","Paluru Dondapadu","Pandalapadu","Srirangarajapuram","Baduguleru","Ballipalli","Bommireddypalli","Chakirala","Challagirigala","Cheerladinne","China","Alavalapadu","China","Irlapadu","Dirisavancha","Ganugapenta","Gosulaveedu","Gudipadu","Guravajipeta","Jammalamadaka","Kanigiri","Kasipuram","Krishnapuram","Machavaram","N.gollapalli","Peramgudipalli","Polavaram","Punugodu","Sankhavaram","Takkellapadu","Thallur","Tummagunta","Vangapadu","Yadavalli","Audipudi","Daggubadu","J.b.v.palem","K.v.palem","Karamchedu","Kesavarappadu","Kunkalamarru","Nayuduvaripalem","Potinavaripalem","R.n.v.palem","Swarna","Swarnapalem","Timidithapadu","Yarramvaripalem","Allinagaram","Badinenipalli","Brahmanapalli","Chintalapalli","Daddawada","Edamakallu","Komarole","Muktapuram","Nallaguntla","Pullareddypalli","Rajupalem","Reddycherla","Suravaripalli","Taticherla","Batchalakurapadu","Chinamanagundam","Chinarikatla","Chinthagunta","Edurallapadu","Ganivanipadu","Garimanapenta","Garladinne","Gotlagattu","Irasalagundam","Katragunta","Konakanametla","Mangapuram","Munagapadu","Nagampalli","Nagarajukunta","Nagireddypalli","Pedarikatla","Regumanipalli","Salanuthala","Siddavaram","Tuvvapadu","Vaddimadugu","Vagemadugu","Veligandla","Vinjavarthipadu","Ankarlapudi","Chinakandlagunta","Chinavenkannapalem","Chodavaram","Goginenivaripalem","Gurrapadiya","Ilavara","K.uppalapadu","Kattubadipalem","Kondapi","Mittapalem","Mugachintala","Mupparajupalem","Muppavaram","Nennurupadu","Pedakandlagunta","Peridepi","Petluru","Vennuru","Anamanamuru","Ballavarappadu","Bodduvanipalem","Dyvalaravuru","Korisapadu","Kurravanipalem","Medarametla","P.gudipadu","Pamidipadu","Prasangulapadu","Rachapudi","Ravinuthala","Thammavaram","Timmanapalem","Yerrabalem","Alluru","Alooru","Ethamukkala","Gadepalem","Gamallapalem","Gundamala","K.pallepalem","Kothapatnam","Madanuru","Motumala","Padarthi","Rajupalem","Rangayapalem","Sankuvanigunta","Alavalapadu","Avulamanda","Bayyavaram","Bodanampadu","Dekanakonda","Ganga Donakonda","Kalluru","Kurichedu","Namassivayapuram","Peddavaram","Potlapadu","West Gangavaram","West Kasipuram","West Naidupalem","West Veerayapalem","Anneboinapalli","Chinapavani","Gangapalem","Lingasamudram","Malakondarayunipalem","Mogilicherla","Mutyalampadu","Pentrala","Racheruvu","Rajupalem","Thimmareddipalem","Veera","Raghavunikota","Viswanadhapuram","Yerrareddypalem","Annangi","Basavannapalem","Doddavaram","Doddavarappadu","Garlapadu","Ghadiyapudi","Gundlapalli","Inamanamelluru","Keerthipadu","Kolachanakota","Lingamgunta","Maddipadu","Mallavaram","Nagannapalem","Nandipadu","Nelaturu","Pedakothapalli","Rachavaripalem","Seetharampuram","Vellampalli","Yedugundlapadu","Markapur Municipality","Akkacheruvu","Badekhanpeta","Bhupathi Palle","Bondala Padu","Chintakunta","Gajjala Konda","Goguladinne","Gottipadia","Idupur","Jammana Palle","Kolabhimunipadu","Malyavanthuni Padu","Markapur","Narasimha Puram","Nikaram Palle","Peda Nagulavaram","Peda Yachavaram","Rayavaram","Sivaram Puram","Thippaya Palem","Vemula Kota","A.r.palem","Ankepalli","Chilamkur","Chimata","Dharmavaram","Garlapeta","Gundlasamudram","Juvvigunta","Kakarla","Kellampalli","Kuchipudi","Marripudi","Narasarajupalem","Pannur","Ramayapalem","Ravillavaripalem","Regalagadda","Tangella","Vallayapalem","Vemavaram","Venkatakrishnapuram","Bobbepalli","Bollapalli","Chimmiribanda","Darsi","Degaramudi","Dronadula","Jonnathali","Kolalapudi","Konanki","Martur","Nagarajupalli","Rajugaripalem","Rajupalem","Tativaripalem","Valaparla","B.v.palem","Bheemavaram","East","Kambhampadu","Edara","Jammalamadaka","Kellampalli","Marella","Mundlamur","Naidupalem","Nuzellapalli","Pasupugallu","Peda","Ullagallu","Polavaram","Pulipadu","Purimetla","Sankarapuram","Singanapalem","Umamaheswarapuram","Vemula","Ammanabrolu","Ch.uppalapadu","Chadalawada","Chavatapalem","Chekurapadu","Edumudi","H.nidamanuru","K.takkellapadu","Kanaparthi","Kandlagunta","Kothakota","M.muppalla","Machavaram","Maddiralapadu","Mattigunta","N.g.padu","Naguluppala","Padu","Obannapalem","Ommevaram","Pothavaram","Raparla","Timmasamudram","Uppugunduru","Vinodarayunipalem","Chejerla","Cheruvu Kommu Palem","Devaram Padu","Gudimella Padu","Karavadi","Koppolu","Kothamamidipalem","Mangaladri Puram","Mukthinutala Padu","Narasa Puram","Pelluru","Sarvereddy Palem","Throvagunta","Ulichi","Vengamukka Palem","Yerajerla","Ayyanakota","Ayyavaripalli","Balijapalem","Bodawada","Botlaguduru","Bukkapuram","Chilamkur","Chintalapalem","Dadireddypalli","Dubagunta","East","Kattakindapalli","East","Kodigudlapadu","Inimerla","Kambaladinne","Kodigumpala","Lakshminarasapuram","Markondapuram","Mopadu","Narramarella","Nuchupoda","Pamur","Raviguntapalli","Vaggampalli","Veerabadrapuram","West","Kattakindapalli","A.b.v.palem","Adusumalli","B.mandagunta","Bhushayapalem","Ch.b.palem","Cherukuru","China","Nandipadu","Chintaguntapalem","Devarapalli","East","Peddivaripalem","Edubadu","Garnepudi","Gollapudi","Inagallu","K.m.v.palem","Kollavaripalem","Kothapalem","Nagulapalem","Nuthalapadu","Parchur","Potukatla","Ramanayapalem","Tanniruvaripalem","Timmarajupalem","Upputuru","Veerannapalem","B.cherlopalli","Badveedu","Boyadagumpala","Chatlamitta","Devarajugattu","Goburu","Gundamcherla","Kalanuthala","Kambhampadu","Maddalakatta","Peda","Araveedu","Peddaraveedu","Putchakayalapalli","Ramayapalem","Regumanipalli","S.kothapalli","Sanikavaram","Sunkesula","Tangiralapalli","Tokapalli","Bettupalli","Chinavarimadugu","Chintagumpalli","Chowtagogulapalli","Gudevaripalem","Guntupalli","Lakshmakkapalli","Marella","Muddapadu","Murugummi","Neredupalli","Peda Alavalapadu","Pedacherlopalli","Pedairlapadu","Pothavaram","Talakondapadu","Vengalayapalli","Vepagumpalli","Akkacheruvu","Amudalapalli","Annavaram","Egalapadu","Juvvaleru","Kambhalapadu","Kuchepalli","Madalavaripalem","Mallavaram","Mugachintala","Nandipalem","Obulakkapalli","Pamulapadu","Podili","Sudanagunta","Talamalla","Thummagunta","Uppalapadu","Yeluru","Boganampadu","Chennipadu","Cherukur","Chowtapalem","Ippagunta","K.agraharam","Kotapadu","M.m.palem","Malepadu","Muppalla","Nagireddypalem","P.v.palem","Ponnalur","Pyreddipalem","Rajolupadu","Ravulakollu","S.b.palem","S.r.palem","Thimmapalem","Uppaladinne","Vellatur","Vempadu","Venkupalem","Z.mekapadu","Chapalamadugu","Gangavaram","I.t.varam","Kavalakuntla","Komarole","Mallapalem","Manepalli","Marrivemula","Mutukula","Nayudupalem","Pidikitivanipalli","Pullalacheruvu","Rachakonda","Sathakodu","Yandrapalli","Akaveedu","Anumalapalli","Chinaganipalli","Chollaveedu","Gowthavaram","Gudimetta","J.p.cheruvu","Kaluvapalli","Oddulavagupalli","Palakaveedu","Racharla","Satyavolu","Somidevipalli","Yadavall","Adavipalem","Bandivaripalem","Chavatipalem","Gurijepalli","Kamepalli","Kommalapadu","Kopparam","Kunduru","Makkenavaripalem","Mamillapalli","Minnekallu","Paritialavaripalem","Pathamaguluru","Pathepuram","Puttavaripalem","Sajjapuram","Santhamagulur","Tangedumalli","Vellalacheruvu","Yelchuru","Bodduvanipalem","Chandrapalem","Chilakapadu","Endluru","Enikapadu","Gummalampadu","Guravareddypalem","Kamepallivaripalem","Konaganivaripalem","M.vemulapadu","Madduluru","Mangamuru","Mynampadu","P.gudipadu","P.takkellapadu","Pernametta","R.l.puram","Rudravaram","S.n.padu","Santhanuthala","Padu","Binginapalli","Kalikivaya","Kanumalla","Mulaguntapadu","Old","S.konda","Pakala","Sanampudi","Singarayakonda","Somarajupalli","Woollapalem","Bellakondavaripalem","Boddikurapadu","Dosakayalapadu","Eastgangavaram","Korrapativaripalem","Lakkavaram","Madhavaram","Mannepalli","Nagambotlapalem","Rajanagaram","Ramabhadrapuram","Sivarampuram","Tallur","Turakapalem","Veluguvaripalem","Vitalapuram","Alakurapadu","Ananthavaram","Jammulapalem","Jayavaram","Kakuturivaripalem","Kanduluru","Karumanchi","Konijedu","M.nidamanuru","Mallavarappadu","Marlapadu","Ponduru","Surareddyaplem","T.nayudupalem","Tangutur","Valluru","Vasepallipadu","Velagapudi","Chennareddypalli","Ganugapenta","Gollapalli","Jagannadhapuram","Kalujuvvalapadu","Kethagudipi","Mangalakunta","Meerjapeta","Nagellamudupu","Pothalapadu","Ragasamudram","Seethanagulavaram","Surepalli","Tadivaripalli","Tarlupadu","Thummalacheruvu","D.v.n.colony","Dupadu","Endurivaripalem","G.ummadivaram","Ganapavaram","Gollapalli","K.annasamudram","Kankanalapalli","Kesinenipalli","Lellapalli","Medapi","Miriyampalli","Mittapalem","Mudivemula","Nadigadda","Oddupalem","P.annasamudram","Rajupalem","Ramasamudram","Somepalli","Tripuranthakam","Vellamapalli","Viswanadhapuram","Atmakuru","Baddipudi","Bheemavaram","Chagollu","Chakicherla","Karedu","Krishnapuram","Mannetikota","Pedapattapupalem","Ramayapatnam","Ulavapadu","Veerepalli","Ballavaram","Chodavaram","Gannavaram","Gokulam","Gudipatipalli","Hussanpuram","Immadicheruvu","Jallapalem","Kankanampadu","Kotalapalli","Marapaguntla","Mogallur","Motupalli","Nagireddypalli","P.n.varam","P.rallapalli","Panduva","Ramagopalapuram","Ramalingapuram","Vedullacheruvu","Veligandla","Akkayapalem","Challareddypalem","Desaipeta","Kothapeta","Pandillapalli","Papayapalem","Pullaripalem","Ramannapeta","Vetapalem","Ammapalem","Ankabhupalapuram","Ayyavaripalli","Badevaripalem","Chundi","Kakutur","Kalavalla","Kondareddypalem","Kondasamudram","Lingapalem","Naladalapur","Nekunampuram","Nukavaram","Pokur","Polinenicheruvu","Polinenipalem","Sakhavaram","Sameerapalem","Singamanenipalli","Voletivaripalem","Ananthavaram","Chimatavaripalem","Gannavaram","Jagarlamudi","Munnangivaripalem","Poluru","Punuru","Suravarapupalli","Syamalavaripalem","Tanuboddivaripalem","Vinjanampadu","WestPedivaripalem","Yaddanapudi","Yanamadala","YddanaPudi","Amanigudipadu","Boyalapalli","Gangapalem","Ganjivaripalli","Gollavidipi","Gurijepalli","Gurrapusala","Kolukula","Mogullapalli","Muraripalli","Narasayapalem","Tammadapalli","Vadampalli","Veerabhadrapuram","Venkatadripalem","Yarragondapalem","Akkacheruvupalem","Chatukupadu","Chintalapalem","Chirrikurapadu","Davaguduru","K.bitragunta","Kamepalli","N.n.kandrika","Nandanavanam","Narisingolu","Paletipadu","Patchava","Pydipadu","R.c.puram","Reddypalem","Thumadu","Vardhinenipalem","Vaviletipadu","Yedlurupadu","Zarugumalli","Chinna kambham","Kambham","Darga","H.","gudem","Jangamguntla","Kandulapuram","L.kota","Lingapuram","Narsireddypalli","Owrangabad","Peddanallakalva","Ravipadu","Turimella","Yarrabalem"]
categorylist=[]
try:
    for i in Category.objects.all():categorylist.append(i.name)
except:pass
def home(request):
    cat=Category.objects.all()
    slide=slides.objects.all()
    return render(request,'index.html',{'title':'Home Page','year':datetime.now().year,'category':cat,'slides':slide,'sliden':range(len(slide)-1),})

def category(request,pk_test):
    cat=Seller.objects.all()
    cati=[]
    slide=slides.objects.all()
    for i in cat:
        if(i.category):
            if(str(i.category.id)==str(pk_test) and i.location==Customer.objects.get(name=request.user).location):
                cati.append(i)
    return render(request,'category.html',{'title':'Home Page','year':datetime.now().year,'product':cati,'slides':slide,'sliden':range(len(slide)-1),})

def shops(request,pk_test):
    cat=Seller.objects.get(id=pk_test)
    products=Product.objects.filter(seller=cat)
    for i in Product.objects.all():
        print(i.seller,cat)
    return render(request,'shops.html',{'title':'Home Page','year':datetime.now().year,'product':products})

def dashboard(request):   
    customer=set()
    user=request.user
    orders=Order.objects.all()
    order=[]
    for i in orders:
        if str(i.seller)==str(request.user):
            order.append(i)
            customer.add(i.customer)
    return render(request,'accounts/dashboard.html',{'title':'Home Page','year':datetime.now().year,'customers':customer,'orders':order})

def customer(request, pk_test):
    return render(request, 'accounts/customer.html')


def logt(request):    
        logout(request)
        return redirect('home')

def location(request):
    if request.method=="GET":
        dist = request.GET.get('District')
        mand = request.GET.get('Mandal')
        vill = request.GET.get('Village')
        cat = request.GET.get('sel')
        categorylist=[i.name for i in Category.objects.all()]
        if cat in categorylist and Seller.objects.filter(name=request.user).exists():
            cat=Category.objects.get(name=cat)
            user=Seller.objects.get(name=request.user)
            user.location=vill
            user.category=cat
            user.save()
            sel=None
            cl=[]
            if Seller.objects.filter(name=request.user).exists():
                sel=1
                cl=Category.objects.all()
                cll=[]
                for i in cl:cll.append(i.name)
                user=Seller.objects.get(name=request.user)
                if str(user.category)in categorylist:
                    return redirect('dashboard')
                return render(request,'location.html',{'title':'Home Page','year':datetime.now().year,'seller':sel,'category':cl})
        elif vill in locationlist and Customer.objects.filter(name=request.user).exists():
            user=Customer.objects.get(name=request.user)
            user.location=vill
            user.save()
            return redirect('home')
    sel=None
    cl=[]
    if Seller.objects.filter(name=request.user).exists():
        sel=1
        user=Seller.objects.get(name=request.user)
        cl=Category.objects.all()
        if str(user.category)in categorylist:
            return redirect('dashboard')
    return render(request,'location.html',{'title':'Home Page','year':datetime.now().year,'seller':sel,'category':cl})

def flogin(request):
    if request.method=="POST":
        luname = request.POST.get('lname')
        lpwd = request.POST.get('lpwd')
        suname = request.POST.get('sname')
        spwd = request.POST.get('spwd')
        stel = request.POST.get('stel')
        smail =  request.POST.get('smail')
        sel = request.POST.get('sel')
        if(luname and lpwd):
            if authenticate(username=luname, password=lpwd):
                login(request,authenticate(username=luname, password=lpwd))
                return redirect('location')
            else:
                return render(request,'login.html',{'msg':"Wrong credentials.Try Again"})
        if(suname and spwd):
            try:
                user = User.objects.create_user(suname, smail, spwd)
                user.save()
                if sel=='1':
                    t=Seller()
                    t.name=suname
                    t.email=smail
                    t.phone=stel
                    t.save()
                    return render(request,'login.html',{'msg':"Seller Acoount Created successfully. Login to enjoy...."})
                else:
                    t=Customer()
                    t.name=suname
                    t.email=smail
                    t.phone=stel
                    t.save()
                    return render(request,'login.html',{'msg':"Customer Acoount Created successfully. Login to enjoy...."})
            except:
                return render(request,'login.html',{'msg':"UserName already taken Choose another.."})
    return render(request,'login.html')

def updateOrder(request, pk):
	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)
	if request.method == 'POST':
		form = OrderForm(request.POST,instance=order)
		if form.is_valid():
			prod = form.save()
			return redirect('dashboard')
	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def addproduct(request):
    user=request.user
    form = ProductForm(request.POST or None, request.FILES) 
    if form.is_valid():
        prod = form.save(commit=False)
        prod.seller = Seller.objects.get(name=request.user)
        prod.category = Seller.objects.get(name=request.user).category
        prod.save()
        return redirect('products')
    context = {'form':form}
    form.errors['name'] = None
    form.errors['price'] = None
    form.errors['img'] = None
    return render(request, 'accounts/product_form.html',context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('dashboard')
	context = {'item':order}
	return render(request, 'accounts/delete.html', context)

def error(request):
    return render(request,'404.html',{'title':'Home Page','year':datetime.now().year,})

def product(request):
    return render(request,'product-details.html',{'title':'Home Page','year':datetime.now().year,})

def products(request):
    user=request.user
    product=Product.objects.all()
    pl=[]
    for i in product:
        if str(i.seller)==str(request.user):
            pl.append(i)
    return render(request,'accounts/products.html',{'title':'Home Page','year':datetime.now().year,'products':pl,})

def deleteproduct(request, pk):
	order = Product.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('products')
	context = {'item':order}
	return render(request, 'accounts/delete.html', context)

def checkout(request):
    if request.method=="GET":
        if str(request.GET.get('Name'))!='None':
            print(request.GET.get('Name'))
            add=''
            for i in request.GET.keys():
                add+=i+':'+request.GET[i]+','
            for i in Cart.objects.filter(customer=Customer.objects.get(name=request.user)):
                t=Order()
                t.customer=Customer.objects.get(name=request.user)
                t.status='Pending'
                t.product=i.product
                t.seller=i.product.seller
                t.address=add
                t.save()
            for i in Cart.objects.filter(customer=Customer.objects.get(name=request.user)):
                i.delete()
                return redirect('home')
    ord=[]
    price=0
    for i in Cart.objects.filter(customer=Customer.objects.get(name=request.user)):
        ord.append(i.product)
        price+=i.product.price
    return render(request,'checkout.html',{'title':'Home Page','year':datetime.now().year,'orders':ord,'price':price,})


def cart(request,pk):
    try:
        if Product.objects.filter(name=pk).exists():
            ord=Product.objects.get(name=pk)
        else:
            ord=Product.objects.get(name=pk)
        t=Cart()
        t.product=ord
        t.customer=Customer.objects.get(name=request.user)
        t.save()
    except:
        pass
    ord=[]
    price=0
    for i in Cart.objects.filter(customer=Customer.objects.get(name=request.user)):
        ord.append(i.product)
        price+=i.product.price
    return render(request,'cart.html',{'title':'Home Page','year':datetime.now().year,'orders':ord,'price':price,}
    )
def cartdel(request,pk):
    ord=Product.objects.get(id=pk)
    for i in list(Cart.objects.filter(product=ord))[:1]:
        i.delete()
    ord=[]
    price=0
    for i in Cart.objects.filter(customer=Customer.objects.get(name=request.user)):
        ord.append(i.product)
        price+=i.product.price
    return render(request,'cart.html',{'title':'Home Page','year':datetime.now().year,'orders':ord,'price':price,}
    )
def orders(request,pk):
    if pk:
        Order.objects.filter(id=pk).delete()
    orders=Order.objects.filter(customer=Customer.objects.get(name=request.user))
    ol=[]
    for i in orders:
        product=Product.objects.get(name=i.product)
        ol.append({'id':i.id,'name':product.name,'price':product.price,'status':i.status,'img':product.img})
    return render(request,'orders.html',{'orders':ol})
def seller(request):
    return render(request,'seller.html',{'title':'Home Page','year':datetime.now().year,})
