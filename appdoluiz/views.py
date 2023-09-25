from django.shortcuts import render, redirect
from .models import GlobalProblem, AIAlignmentSkill
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
  global_problems = GlobalProblem.objects.all().order_by('ranking_80000_hours')
  ai_alignment_skills = AIAlignmentSkill.objects.all()
  return render(request, "home.html", context={"global_problems": global_problems, "ai_alignment_skills":ai_alignment_skills})

def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(request.POST["username"],request.POST["email"], request.POST["password"])
    user.save()
    return redirect("home")
  return render(request, "register.html", context={"action":"Adicionar"})

def login_user(request):
  if request.method == "POST":
    user = authenticate(username=request.POST["username"],password=request.POST["password"])
    if user is not None:
      login(request,user)
    else:
      return render(request, "login.html",context={"error_msg":"Usuário não existe"})
    
    if request.user.is_authenticated:
      login(request,user)
      return redirect("home")
    return render(request, "login.html",context={"error_msg":"Usuário não pôde ser logado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")
  
@login_required
def create_globalproblem(request):
  if request.method == "POST":
    GlobalProblem.objects.create(
      title=request.POST["title"],
      description=request.POST["description"],
      ranking_80000_hours=request.POST["ranking_80000_hours"],
      pub_date=request.POST["pub_date"],
    )
    return redirect("home")
  return render(request, "globalproblem_forms.html", context={"action":"Criar"})

@login_required
def update_globalproblem(request, id):
  globalproblem = GlobalProblem.objects.get(id=id)
  
  if request.method == "POST":
    globalproblem.title = request.POST["title"]
    globalproblem.description = request.POST["description"]
    globalproblem.ranking_80000_hours = request.POST["ranking_80000_hours"]
    globalproblem.pub_date = request.POST["pub_date"]
    globalproblem.save()
    
    return redirect("home")
  return render(request, "globalproblem_forms.html", context={"globalproblem":globalproblem, "action":"Atualizar"})

@login_required
def delete_globalproblem(request, id):
  globalproblem = GlobalProblem.objects.get(id=id)
  
  if request.method == "POST":
    if "confirm" in request.POST:
      globalproblem.delete()
    
    return redirect("home")
  return render(request, "areyousure_problem.html", context={"globalproblem":globalproblem})

@login_required
def create_aiskill(request):
  if request.method == "POST":
    AIAlignmentSkill.objects.create(
      title=request.POST["title"],
      difficulty=request.POST["difficulty"],
      importance=request.POST["importance"],
      how_to_learn=request.POST["how_to_learn"],
    )
    return redirect("home")

  difficulties = AIAlignmentSkill.difficulty.field.choices
  ways_to_learn = AIAlignmentSkill.how_to_learn.field.choices
  return render(request, "aiskill_forms.html", context={"action":"Criar", "difficulties":difficulties, "ways_to_learn":ways_to_learn})

@login_required
def update_aiskill(request, id):
  aiskill = AIAlignmentSkill.objects.get(id=id)
  
  if request.method == "POST":
    aiskill.title = request.POST["title"]
    aiskill.difficulty = request.POST["difficulty"]
    aiskill.importance = request.POST["importance"]
    aiskill.how_to_learn = request.POST["how_to_learn"]
    aiskill.save()
    
    return redirect("home")

  difficulties = AIAlignmentSkill.difficulty.field.choices
  ways_to_learn = AIAlignmentSkill.how_to_learn.field.choices
  return render(request, "aiskill_forms.html", context={"aiskill":aiskill, "action":"Atualizar", "difficulties":difficulties, "ways_to_learn":ways_to_learn})

@login_required
def delete_aiskill(request, id):
  aiskill = AIAlignmentSkill.objects.get(id=id)
  
  if request.method == "POST":
    if "confirm" in request.POST:
      aiskill.delete()
    
    return redirect("home")
  return render(request, "areyousure_aiskill.html", context={"aiskill":aiskill})